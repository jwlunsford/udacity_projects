from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# SETUP ABOVE

# API ENPOINTS --- JSON
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



# Resturant CRUD
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    # show all restaurants
    restaurants = session.query(Restaurant).all()
    return render_template('restaurant.html', restaurants=restaurants)


@app.route('/restaurant/new')
def newRestaurant():
    # add new restaurant using name supplied by user
    if request.method == 'POST':
        restaurant = Restaurant(name=request.form['name'])
        session.add(restaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html')


@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    # edit a restaurant
    editRestaurant = session.query(Restaurant).filter_by(restaurant_id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['rename']:
            editRestaurant.name = request.form['rename']
        session.add(editRestaurant)
        session.commit()
        flash("Restaurant name successfully changed to {}.".format(editRestaurant.name))
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html', restaurant_id=restaurant_id, restaurant)


@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    # delete a restaurant
    return "This page will delete a restaurant."


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
        flash('New menu item was created!')
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
        flash("Menu item was edited!")
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
        flash("Menu item was deleted!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', restaurant_id=restaurant_id, item=deleteItem)




if __name__ == '__main__':
    app.secret_key = 'Super_Strong_Secret_Key'
    app.debug = True
    app.run(host='localhost', port=5050)

