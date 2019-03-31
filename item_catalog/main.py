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


# API ENDPOINTS GO HERE


@app.route("/")
def index():
    return render_template('showItems.html')


if __name__ == '__main__':
    app.run(debug=True)
