

from flask import Flask, request, jsonify,session
from sqlalchemy import create_engine


app = Flask(__name__)

app.config['SECRET_KEY'] = 'IM-SECRET'
def connect_db():
    DATABASE_URL = "postgres+psycopg2://postgres:priya@localhost/Ecommerce"
    return create_engine(DATABASE_URL)

db = connect_db()

from api import *
if __name__ == '__main__':
    app.run(debug=True)
