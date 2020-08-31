from flask import Flask, request, jsonify, session, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from flask_bcrypt import Bcrypt
# from flask.ext.bcrypt import Bcrypt
from flask_cors import CORS


Base = declarative_base()

app = Flask(__name__)

CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SECRET_KEY'] = 'IM-SECRET'

def connect_db():
    DATABASE_URL = "postgres+psycopg2://postgres:priya@localhost/Ecommerce"
    return create_engine(DATABASE_URL)

db = connect_db()

bcrypt=Bcrypt(app)

from api import *

if __name__ == '__main__':
    app.run(debug=True)

    