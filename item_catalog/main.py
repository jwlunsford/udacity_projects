# flask imports
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email

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


# CATEGORY ROUTES GO HERE

# temporary data until DB is connected - for testing
user = {'id':1, 'username':'jon', 'email':'jon@mail.com'}
category = {'id':1, 'name':'evergreen'}
item = {'id':1, 'name':'American Elm', 'photo_filename':'american_elm.png',
        'description':'American Elm (Ulmus americana) can grow to 60 feet tall and 3 feet in diameter.  The wood is strong and difficult to split, which makes it good for saddle trees, and veneer for baskets and crates.', 'category_id':2}
items = [{'id':1, 'name':'American Elm', 'photo_filename':'american_elm.png',
        'description':'American Elm (Ulmus americana) can grow to 60 feet tall and 3 feet in diameter.  The wood is strong and difficult to split, which makes it good for saddle trees, and veneer for baskets and crates.', 'category_id':2},
        {'id':2, 'name':'Bitternut Hickory', 'photo_filename':'bitternut_hickory.png', 'description':'Bitternut Hickory (Carya cordiformis) is a tall slender tree with a broad crown.  It can grow to 100 feet heigh and 2 to 3 feet in diameter. The wood is strong and heavy, and reddish-brown in color.', 'category_id':2},
        {'id':3, 'name':'Black Oak', 'photo_filename':'black_oak.png', 'description':'Black Oak (Quercus velutina) can grow to 80 feet high and 1 to 3 feet in diameter.  The wood is hard, stong, heavy, and checks easily.', 'category_id':2}
        ]

@app.route("/categories/")
def showCategories():
    """return all categories in the database"""
    pass


@app.route("/category/<int:id>/")
def getCategory(id):
    """return a specific category matching the category.id"""
    pass


@app.route("/category/new/", methods=['GET', 'POST'])
def newCategory():
    """create a new category in the database"""
    pass


@app.route("/category/<int:id>/edit/", methods=['GET', 'POST'])
def editCategory(id=id):
    """edit a category in the database"""
    pass


@app.route("/category/<int:id>/delete/", methods=['GET', 'POST'])
def deleteCategory(id=id):
    """delete a category from the database"""
    pass



# ITEM ROUTES GO HERE

@app.route("/category/<int:id>/items/")
def showItems(id):
    """return all items in the database for a given category"""
    return render_template('showItems.html', items=items, category=category)


@app.route("/item/<int:id>/")
def getItem(id):
    """return a specific item in the database"""
    pass


@app.route("/categories/<int:id>/new/", methods=['GET', 'POST'])
def newItem():
    """create a new item in the datasbase under a given category"""
    pass


@app.route("/item/<int:id>/edit/", methods=['GET', 'POST'])
def editItem(id=id):
    """edit an item in the database"""
    # retrieve the item by id
    id = id - 1     # this is needed because we are retrieving the item by idx
    item = items[id]
    form = ItemForm()
    return render_template('editItems.html', form=form, item=item, user=user)


@app.route("/item/<int:id>/delete/", methods=['GET', 'POST'])
def deleteItem(id=id):
    """delete an item from the database"""
    pass



# WTForms
class ItemForm(FlaskForm):
    """WTF class for the Item Form"""
    name = StringField('What is the item name?', validators=[Required()])
    photo_filename = StringField('Enter the filename, including extension, of the photo.')
    descripton = StringField('Enter a short description of the item.', validators=[Required()])
    submit = SubmitField('Submit')









if __name__ == '__main__':
    app.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    app.run(debug=True)
