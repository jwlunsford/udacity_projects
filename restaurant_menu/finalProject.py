from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# imports for anti-forgery state token
from flask import session as login_session
import random, string

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# SETUP ABOVE

# API ENPOINTS --- JSON
@app.route('/restaurants/JSON')
def restaruantsJSON():
    # use jsonify to return a list of restaurants in the DB
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[r.serialize for r in restaurants])


@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    # use jsonify to return a list of serialized menu items
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantMenuItemJSON(restaurant_id, menu_id):
    # use jsonify to return a serialized menu item object
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=item.serialize)


# login route
@app.route('/login')
def show_login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    login_session['state'] = state
    return render_template('login.html')


# Resturant CRUD
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    # show all restaurants
    restaurants = session.query(Restaurant).all()
    return render_template('restaurant.html', restaurants=restaurants)


@app.route('/restaurant/new', methods=['GET', 'POST'])
def newRestaurant():
    # add new restaurant using name supplied by user
    if request.method == 'POST':
        restaurant = Restaurant(name=request.form['name'])
        session.add(restaurant)
        session.commit()
        flash("Restaurant {} was added.".format(restaurant.name))
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    # edit a restaurant
    thisRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['rename']:
            thisRestaurant.name = request.form['rename']
        session.add(thisRestaurant)
        session.commit()
        flash("Restaurant name successfully changed to {}.".format(thisRestaurant.name))
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html', restaurant_id=restaurant_id, restaurant=thisRestaurant)


@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    # delete a restaurant
    thisRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(thisRestaurant)
        session.commit()
        flash("Restauarant {} was deleted".format(thisRestaurant.name))
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleteRestaurant.html', restaurant=thisRestaurant)


# Menu CRUD
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menu.html', items=items, restaurant=restaurant)


# Task 1:  Create route for newMenuItem
@app.route('/restaurants/<int:restaurant_id>/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    # handle the post request
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash('New menu item {} was created!'.format(newItem.name))
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        # handle the GET request
        # //// If this doesn't work, check the variable passed in to render_template
        return render_template('newMenuItem.html', restaurant_id=restaurant_id)


# Task 2:  Create route for editMenuItem
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    # handle the POST request
    editItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['rename']:
            editItem.name = request.form['rename']
        session.add(editItem)
        session.commit()
        flash("Menu item {} was edited!".format(editItem.name))
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        # handle the GET request
        return render_template('editMenuItem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editItem)


# Task 3:  Create a route for deleteMenuItem
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deleteItem)
        session.commit()
        flash("Menu item {} was deleted!".format(deleteItem.name))
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', restaurant_id=restaurant_id, item=deleteItem)




if __name__ == '__main__':
    app.secret_key = 'Super_Strong_Secret_Key'
    app.debug = True
    app.run(host='localhost', port=5050)

