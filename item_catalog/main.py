# flask imports
from flask import Flask, render_template, session, request, redirect, url_for, flash, jsonify, make_response
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# database imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Category, Item

# auth imports
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

# misc imports
import httplib2
import json
import requests
import random
import string


app = Flask(__name__)
bootstrap = Bootstrap(app)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# AUTH GOES HERE


# API ENDPOINTS GO HERE




# temporary data until DB is connected - for testing
user = {'id':1, 'username':'jon', 'email':'jon@mail.com'}
category = {'id':1, 'name':'evergreen'}
item = {'id':1, 'name':'American Elm', 'photo_filename':'american_elm.png',
        'description':'American Elm (Ulmus americana) can grow to 60 feet tall and 3 feet in diameter.  The wood is strong and difficult to split, which makes it good for saddle trees, and veneer for baskets and crates.', 'category_id':2}
items = [{'id':1, 'name':'American Elm', 'photo_filename':'american_elm.png',
        'description':'American Elm (Ulmus americana) can grow to 60 feet tall and 3 feet in diameter.  The wood is strong and difficult to split, which makes it good for saddle trees, and veneer for baskets and crates.', 'category_id':2},
        {'id':2, 'name':'Bitternut Hickory', 'photo_filename':'bitternut_hickory.png', 'description':'Bitternut Hickory (Carya cordiformis) is a tall slender tree with a broad crown.  It can grow to 100 feet tall and 2 to 3 feet in diameter. The wood is strong and heavy, and reddish-brown in color.', 'category_id':2},
        {'id':3, 'name':'Black Oak', 'photo_filename':'black_oak.png', 'description':'Black Oak (Quercus velutina) can grow to 80 feet tall and 1 to 3 feet in diameter.  The wood is hard, stong, heavy, and checks easily.', 'category_id':2},
        {'id':4, 'name':'Black Hickory', 'photo_filename':'black_hickory.png', 'description':'Black Hickory (Carya texana) grows on hillsides and sandy uplands.  This tree can grow to 75 feet tall and 2 feet in diameter.  The wood is hard, but brittle, and makes good fuelwood.', 'category_id':2},
        {'id':5, 'name':'Honeylocust', 'photo_filename':'honeylocust.png', 'description':'Honeylocust (Gleditsia triacanthos) can grow to 75 feet tall and 30 inches in diameter.  The wood is course-grained, strong, and moderately durable.', 'category_id':2}
        ]


# CATEGORY ROUTES GO HERE

@app.route("/categories/")
def showCategories():
    """return all categories in the database"""
    pass


@app.route("/category/<int:category_id>/")
def getCategory(category_id):
    """return a specific category matching the category.id"""
    pass


@app.route("/category/new/", methods=['GET', 'POST'])
def newCategory():
    """create a new category in the database"""
    pass


@app.route("/category/<int:category_id>/edit/", methods=['GET', 'POST'])
def editCategory(category_id):
    """edit a category in the database"""
    pass


@app.route("/category/<int:category_id>/delete/", methods=['GET', 'POST'])
def deleteCategory(category_id):
    """delete a category from the database"""
    pass



# ITEM ROUTES GO HERE

@app.route("/category/<int:category_id>/items/")
def showItems(category_id):
    """return all items in the database for a given category"""
    category = session.query(Category).filter_by(category_id=category_id).first()
    return render_template('showItems.html', items=items, category=category)


@app.route("/item/<int:item_id>/")
def getItem(item_id):
    """return a specific item in the database"""
    pass


@app.route("/category/<int:category_id>/new/", methods=['GET', 'POST'])
def newItem(category_id):
    """create a new item in the database under a given category"""
    form = ItemForm()
    # handle the POST request
    if form.validate_on_submit():
        name = form.name.data
        photo = form.photo_filename.data
        description = form.description.data
        createdItem = Item(name=name, photo_filename=photo,
                           description=description, category_id=category_id)
        session.add(createdItem)
        session.commit()
        flash('New {} tree created!'.format(name))
        return redirect(url_for('showItems', id=id))
    # handle the GET request
    return render_template('newItems.html', form=form, user=user)


@app.route("/item/<int:item_id>/edit/", methods=['GET', 'POST'])
def editItem(item_id):
    """edit an item in the database"""
    # retrieve the item
    item = session.query(Item).filter_by(id=id).first()

    id = id - 1     # this is needed because we are retrieving the item by idx
    item = items[id]
    form = ItemForm()
    return render_template('editItems.html', item=item, user=user)


@app.route("/item/<int:item_id>/delete/", methods=['GET', 'POST'])
def deleteItem(item_id):
    """delete an item from the database"""
    item = items[item_id]
    return render_template('deleteItems.html', item=item, user=user)



# WTForms
class ItemForm(FlaskForm):
    """WTF class for the Item Form"""
    name = StringField('Enter the common name for the tree.', validators=[DataRequired()])
    photo_filename = StringField("Enter the filename and extension of the photo (ex: \'my_picture.jpg\').")
    descripton = StringField('Enter a short description of the tree...', validators=[DataRequired()])
    submit = SubmitField('Submit')









if __name__ == '__main__':
    app.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    app.run(debug=True)
