

from db import *
from methods import *
from db_connection import *

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        user=is_valid_user(user_name, password)
        if user=='True':
          return("Sucessfully Logged in")
        else:
          return("Invalid Username Pasword")

@app.route('/categories', methods=['GET'])
def display_categories():
    categories = get_all_categories()
    return jsonify(categories)

@app.route('/categories/<category_id>/products', methods=['GET'])
def display_products(category_id):
    products = get_all_products(category_id)
    return jsonify(products)

@app.route('/categories/<category_id>/products', methods=['GET'])
def display_products(category_id):
    products = get_all_products(category_id)
    return jsonify(products)

