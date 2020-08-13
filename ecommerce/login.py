
from flask import Flask, request, jsonify
from sqlalchemy import create_engine

app = Flask(__name__)

def connect_db():
    DATABASE_URL = "postgres+psycopg2://postgres:priya@localhost/Ecommerce"
    return create_engine(DATABASE_URL)
db = connect_db()

@app.route("/")
def home():
  return "Welcome to !! <h1>Priya Store</h1>"

@app.route('/categories',methods=['GET'])
def get_categories():
    categories = db.execute('select * from ecommerce.categories')
    result = [dict(row) for row in categories]
    return jsonify(result)
