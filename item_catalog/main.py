# flask imports
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response
from flask_bootstrap import Bootstrap

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


app = Flask(__name__)
bootstrap = Bootstrap(app)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()


# AUTH GOES HERE


# API ENDPOINTS GO HERE


# CATEGORY ROUTES GO HERE

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
    pass


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
    pass


@app.route("/item/<int:id>/delete/", methods=['GET', 'POST'])
def deleteItem(id=id):
    """delete an item from the database"""
    pass












if __name__ == '__main__':
    app.run(debug=True)
