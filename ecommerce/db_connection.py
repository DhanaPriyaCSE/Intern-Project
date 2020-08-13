

from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import api

app = Flask(__name__)

app.config['SECRET_KEY'] = 'IM-SECRET'
def connect_db():
    DATABASE_URL = "postgres+psycopg2://postgres:priya@localhost/Market"
    return create_engine(DATABASE_URL)

db = connect_db()

if __name__ == '__main__':
    app.run(debug=True)
