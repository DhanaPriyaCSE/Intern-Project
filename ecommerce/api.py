
from flask import Flask, request, jsonify,session

from db import *
from methods import *

@app.route('/')
def main():
    return 'Welcome to Priya\'s Shopping '

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['username']
        password = request.form['password']
        user=is_valid_user(user_name, password)
        if user is None:
            return ("Invalid Username Password")
        else:
            session[status] = True
            session[user_id] = user.get_user_id(user_name)
        return ("Sucessfully Logged in")

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
    product_details=get_product_details(product_id)
    return jsonify(product_details)

@app.route('/cart/<user_id>', methods=['GET'])
def view_cart_product(user_id):
    cart_id=get_cart_id(user_id)
    result = get_cart_products(cart_id)
    return jsonify(result)

@app.route('/cart/<user_id>', methods=['POST'])
def add_product_to_cart(user_id):
    product_id=request.form['product_id']
    quantity = request.form['quant
    cart_id = get_cart_id(user_id)
    # if user_id in session:
    add_to_cart = add_to_cart_products(cart_id, product_id, quantity)
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
    cart_id = get_cart_id(user_id)
    if product_availablity(product_id,quantity) == True:
         updated= update_quantity(cart_id,product_id,quantity)
         if updated is True:
            return 'Product quantity is updated'
         else:
             return 'Failed to update'
    else:
        return 'product is not available now'

@app.route('/cart/<user_id>', methods=['DELETE'])
def delete_product(user_id):
    product_id=request.form['product_id']
    cart_id = get_cart_id(user_id)
    result=delete_product_from_cart(cart_id, product_id)
    if result is True:
        return 'Product quantity is deleted'
    else:
        return 'Failed to delete'









