
from flask import Flask, request, jsonify,session
from method import *
from db_connection import *
from cart import *
from category import *
from product import *
from users import *
from seller import *

@app.route('/')
def main():
    return 'Welcome to Priya\'s Shopping '

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        user=User(user_name, password).is_valid_user()
        if user is not True:
            return ("Invalid Username Password")
        else:
            session[user_id] = User(user_name,password).get_user_id()
            return ("Sucessfully Logged in")

@app.route('/register', methods=['POST'])
def signup():
    user_name = request.form['user_name']
    password = request.form['password']
    user = User(user_name, password)
    if user.signup_user() == True:
        return 'Registered successfully'
    else:
        return 'User name already exist'


@app.route('/categories', methods=['GET'])
def display_categories():
    categories = get_all_categories()
    return jsonify(categories)

@app.route('/categories/<category_id>/products', methods=['GET'])
def display_products(category_id):
    products = get_all_products(category_id)
    return jsonify(products)

@app.route('/product/<product_id>', methods=['GET'])
def display_product_details(product_id):
    product_details=Product(product_id).get_product_details()
    return jsonify(product_details)

@app.route('/cart/<user_id>', methods=['GET'])
def view_cart_product(user_id):
    cart_id=Cart(user_id).get_cart_id()
    result = get_cart_products(cart_id)
    return jsonify(result)

@app.route('/cart/<user_id>', methods=['POST'])
def add_product_to_cart(user_id):
    product_id=request.form['product_id']
    quantity = request.form['quantity']
    cart_id = Cart(user_id).get_cart_id()
    # if user_id in session:
    add_to_cart = CartProduct(cart_id, product_id).add_to_cart_products(quantity)
    if add_to_cart is True:
        return "product added to ur cart"
    else:
        return "failed to add"
    # else:
    #     return "please login to add products"


@app.route('/cart/<user_id>', methods=['PUT'])
def update_product_quantity(user_id):
    product_id=request.form['product_id']
    quantity = request.form['quantity']
    cart_id = Cart(user_id).get_cart_id()
    if Product(product_id).product_availablity(quantity) == True:
         updated= CartProduct(cart_id, product_id).update_quantity(quantity)
         if updated is True:
            return 'Product quantity is updated'
         else:
             return 'Failed to update'
    else:
        return 'product is not available now'

@app.route('/cart/<user_id>', methods=['DELETE'])
def delete_product(user_id):
    product_id=request.form['product_id']
    cart_id = Cart(user_id).get_cart_id()
    result=CartProduct(cart_id, product_id).delete_product_from_cart()
    if result is True:
        return 'Product quantity is deleted'
    else:
        return 'Failed to delete'


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return 'You are successfully Logged out'








