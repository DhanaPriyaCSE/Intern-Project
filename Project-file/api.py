
from flask import Flask, request, jsonify,session
from flask_cors import cross_origin
from method import *
from db_connection import *
from cart import *
from category import *
from product import *
from users import *
from seller import *

CORS(app, resources=r'/api/*')
CORS(app, resources={r"/*": {"origins": "*"}})

@cross_origin
@app.route('/')
def main():
    return 'Welcome to Priya\'s Shopping'
    # return render_template("index.html",greet)

@cross_origin
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        req_data = request.get_json()
        user_name = req_data['user_name']
        password = req_data['password']
        # user_name = request.form['user_name']
        # password = request.form['password']
        # h_pwd = bcrypt.generate_password_hash(password).decode('utf-8')
        user=User(user_name, password)
        # user_id = User(user_name, password).get_user_id()
        print(user,user_name,password)
        if user.is_valid_user()==True:
            # session[user_id] = user_id
            # flash("Sucessfully Logged in")
            return jsonify({'status': '200', 'user_id': user.get_user_id()})
            # return render_template("category.html")

        else:
            # flash("Invalid Username Password")
            return jsonify({'status': '401'})
            # return render_template("login.html",message="Invalid Username Password")
        

@cross_origin
@app.route('/register', methods=['POST'])
def signup():
    if request.method == 'POST':
        req_data = request.get_json()
        user_name = req_data['user_name']
        password = req_data['password']
        valid_user_name = User(user_name,password).validate_name()
        h_pwd=bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(user_name, password)
        if user.signup_user()==True:
                return jsonify({'status': '200', 'user_id': user.get_user_id(),'message':'Sucessfully Registerd!'})
        elif valid_user_name == False:
            return jsonify({'status': '401', 'message':'Enter valid Name'})
        else:
            return jsonify({'status': '401', 'message':'User Already Exists'})



@cross_origin
@app.route('/categories', methods=['GET'])
def display_categories():
    categories = get_all_categories()
    return jsonify(categories)

@cross_origin
@app.route('/categories/<category_id>/products', methods=['GET'])
def display_products(category_id):
    products = get_all_products(category_id)
    return jsonify(products)

@cross_origin
@app.route('/product/<product_id>', methods=['GET'])
def display_product_details(product_id):
    product_details=Product(product_id).get_product_details()
    return jsonify(product_details)

@cross_origin
@app.route('/cart/<user_id>', methods=['GET'])
def view_cart_product(user_id):
    cart_id=Cart(user_id).get_cart_id()
    result = get_cart_products(cart_id)
    return jsonify(result)

@cross_origin
@app.route('/cart/<user_id>', methods=['POST'])
def add_product_to_cart(user_id):

    if request.method == 'POST':
        req_data = request.get_json()
        product_id=req_data['product_id']
        quantity = req_data['quantity']
        cart_id = Cart(user_id).get_cart_id()
        # if user_id in session:
        add_to_cart = CartProduct(cart_id, product_id).add_to_cart_products(quantity)
        if add_to_cart is True:
            return jsonify({'status': '200', 'message':'product added to your cart'})
        else:
            return jsonify({'status': '401', 'message':'Error while add'})
        # else:
        #     return "please login to add products"



@cross_origin
@app.route('/cart/<user_id>', methods=['PUT'])
def update_product_quantity(user_id):
    req_data = request.get_json()
    product_id=req_data['product_id']
    quantity = req_data['quantity']
    cart_id = Cart(user_id).get_cart_id()

    if Product(product_id).product_availablity(quantity) == True:
         updated= CartProduct(cart_id, product_id).update_quantity(quantity)
         if updated is True:
            return jsonify({'status': '200', 'message':'Product quantity is updated' })
         else:
             return  jsonify({'status': '401', 'message':'Failed to update' })
    else:
        return  jsonify({'status': '200', 'message':'product is not available now' })


@cross_origin
@app.route('/cart/<user_id>', methods=['DELETE'])
def delete_product(user_id):
    req_data = request.get_json()
    product_id=req_data['product_id']
    cart_id = Cart(user_id).get_cart_id()
    result=CartProduct(cart_id, product_id).delete_product_from_cart()

    if result is True:
        return jsonify({'status': '200', 'message':'Product from ur cart is deleted'  })
    else:
        return jsonify({'status': '200', 'message':'Failed to delete' })


@cross_origin
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return 'You are successfully Logged out'








