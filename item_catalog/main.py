import random
import string

# flask imports
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response
from flask import session as login_session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# database imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# auth imports
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

# misc imports
import httplib2
import json
import requests

from models import Base, User, Category, Item


app = Flask(__name__)
bootstrap = Bootstrap(app)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# AUTH GOES HERE

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "TreeCatalog"


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['email'] = data['email']

    # see if user exists, if not make a new User
    user_id = getUserId(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id


    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    flash("You are now logged in as %s" % login_session['username'],
          'alert alert-success')
    return output


@app.route('/logout/')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps(
            'Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print('In gdisconnect access token is {}'.format(access_token))
    print('User name is: {}'.format(login_session['username']))
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print('result is {}'.format(result))
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        # flash signout message and redirect to the landing page
        flash("Sign out successful.", 'alert alert-success')
        return redirect(url_for('showLandingPage'))
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# LOGIN ROUTE
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# API ENDPOINTS GO HERE - JSON
@app.route("/api/v1/category/<int:category_id>/items/JSON")
def categoryItemsJSON(category_id):
    """returns a serialized version of the items for a particular category."""
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route("/api/v1/item/<int:item_id>/JSON")
def itemJSON(item_id):
    """returns a serialized verions of a specific item."""
    item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(Item=item.serialize)


# ITEM ROUTES GO HERE
@app.route("/")
def showLandingPage():
    """return the index.html page."""
    return render_template('index.html')


@app.route("/category/<int:category_id>/items/")
def showItems(category_id):
    """return all items in the database for a given category"""
    category = session.query(Category).filter_by(id=category_id).first()
    items = session.query(Item).filter_by(category_id=category_id).all()
    # if the user is not logged in, show the publicItems page.
    if 'username' not in login_session:
        return render_template('publicItems.html', items=items,
                               category=category)
    return render_template('showItems.html', items=items, category=category)


@app.route("/item/<int:item_id>/")
def getItem(item_id):
    """return a specific item in the database"""
    pass


@app.route("/category/<int:category_id>/new/", methods=['GET', 'POST'])
def newItem(category_id):
    """create a new item in the database under a given category"""
    # check for user login
    if 'username' not in login_session:
        return redirect('/login')
    form = ItemForm()
    # handle the POST request
    user = session.query(User).filter_by(username=login_session['username']).one()
    if form.validate_on_submit():
        name = form.name.data
        photo = form.photo_filename.data
        description = form.description.data
        createdItem = Item(name=name, photo_filename=photo,
                           description=description, category_id=category_id)
        session.add(createdItem)
        session.commit()
        flash('New {} tree created!'.format(name), 'alert alert-warning')
        return redirect(url_for('showItems', category_id=category_id))
    # handle the GET request
    return render_template('newItems.html', form=form, user=user,
                           category=category_id)


@app.route("/category/<int:category_id>/<int:item_id>/edit/",
           methods=['GET', 'POST'])
def editItem(category_id, item_id):
    """edit an item in the database"""
    # retrieve the item
    item = session.query(Item).filter_by(id=item_id).first()
    user = session.query(User).filter_by(
                                         username=login_session['username']).one()
    form = ItemForm()
    # handle the POST request
    if form.validate_on_submit():
        # update the item data
        item.name = form.name.data
        item.photo_filename = form.photo_filename.data
        item.description = form.description.data
        # save the currently logged in user's id to the database with item
        item.user_id = login_session['user_id']
        # operation complete flash message to user
        flash("Tree {} has been updated!".format(item.name),
              'alert alert-warning')
        return redirect(url_for('showItems', category_id=category_id))
    # Handle the GET request
    # first check for user login, then check that they are authorized to edit
    if 'username' not in login_session:
        return redirect('/login')
    if item.user_id != login_session['user_id']:
        flash("""You are not allowed to edit this tree.
              You may only edit a tree that you created.""",
              'alert alert-danger')
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('editItems.html', item=item, user=user,
                               form=form)


@app.route("/category/<int:category_id>/<int:item_id>/delete/",
           methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    """delete an item from the database"""
    # check for user login
    if 'username' not in login_session:
        return redirect('/login')
    # get the item from the database
    item = session.query(Item).filter_by(id=item_id).first()
    user = session.query(User).filter_by(username=login_session['username']).one()
    # if this is a post action, delete the item, and redirect
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        # operation complete flash message to user
        flash("""Item: {} was successfully deleted from
              the database.""".format(item.name), 'alert alert-warning')
        return redirect(url_for('showItems', category_id=category_id))
    # Process GET request
    # first check for login, then check that they are authorized to delete
    if 'username' not in login_session:
        return redirect('/login')
    if item.user_id != login_session['user_id']:
        flash("""You are not allowed to delete this tree.
              You may only delete a tree that you created.""",
              'alert alert-danger')
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('deleteItems.html', item=item, user=user,
                               category_id=category_id)


def createUser(login_session):
    """add a new user to the database."""
    newUser = User(username = login_session['username'],
                   email= login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    """get a user from the database"""
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserId(email):
    """get a user's id using their email."""
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# WTForms: simplifies HTML form creation, and provides CSRF protection
class ItemForm(FlaskForm):
    """WTF class for the Item Form"""
    name = StringField('Enter the common name for the tree.',
                       validators=[DataRequired()])
    photo_filename = StringField(
        "Enter the filename and extension (ex: \'my_picture.jpg\').")
    description = StringField('Enter a short description of the tree...', validators=[DataRequired()])
    submit = SubmitField('Submit')


if __name__ == '__main__':
    app.config['SECRET_KEY'] = ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for x in range(32))
    app.run(debug=True)
