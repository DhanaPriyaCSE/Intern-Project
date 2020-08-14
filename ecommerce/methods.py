from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from db_connection import *

def get_user_id(user_name):
    user = db.execute('select user_id from ecommerce.users where username = \'{}\''.format(user_name))
    data = user.fetchone()[0]
    return data

def is_valid_user(username,password):
  user = db.execute('select * from ecommerce.users where username = \'{}\' and password=\'{}\''.format(username,password))
  data =user.fetchone()
  return data

def get_all_categories():
    categories = db.execute('select * from ecommerce.categories')
    result = [dict(row) for row in categories.fetchall()]
    return result

def get_all_products(category_id):
    products = db.execute('select * from ecommerce.products where fk_category_id = \'{}\''.format(category_id))
    result = [dict(row) for row in products.fetchall()]
    return result


def get_product_details(product_id):
        product = db.execute("select * from ecommerce.products where  id=\'{}\'".format(product_id))
        result = [dict(row) for row in product.fetchall()]
        return result

def get_cart_id(user_id):
    cart_id =db.execute("select id from ecommerce.cart where  user_id=\'{}\'".format(user_id))
    return  cart_id.fetchone()[0]

def get_cart_products(cart_id):
    # cart_id=db.execute("select id from ecommerce.cart where  user_id=\'{}\'".format(user_id))
    #cart=db.execute("select * from ecommerce.cart_product where cart_id=\'{}\'".format("select id from ecommerce.cart where  user_id=\'{}\'".format(user_id)))
    cart_product = db.execute("select product_id from ecommerce.cart_product where cart_id=\'{}\'".format(cart_id))
    products = [dict(row) for row in cart_product.fetchall()]
    products_in_cart=[]
    for product in range(len(products)):
        products_in_cart.append(get_cart_product_details(products[product]['product_id'],cart_id))
    return products_in_cart

def get_cart_product_details(product_id, cart_id):
    products = db.execute('select * from ecommerce.products where id = \'{}\''.format(product_id))
    for product in products.fetchall():
        result= display_product_format(product, cart_id)
    return result


def get_category_name(category_id):
    category_name= db.execute('select name from ecommerce.categories where id = \'{}\''.format(category_id))
    return category_name.fetchone()[0]
def get_cart_product_quantity(cart_id, product_id):
    quantity = db.execute('select product_quantity from ecommerce.cart_product where cart_id = \'{}\' and product_id = \'{}\''.format(cart_id,product_id))
    return quantity.fetchone()[0]

def display_product_format(product, cart_id):
    product_list = {}
    product_list['product_id'] = product.id
    product_list['name'] = product.name
    product_list['price'] = product.price
    product_list['category_name'] = get_category_name(product.fk_category_id)
    product_list['quantity'] =get_cart_product_quantity(cart_id, product.id)
    return product_list

def add_to_cart_products(cart_id,product_id,quantity):
    add_product = db.execute('insert into ecommerce.cart_product (cart_id,product_id,product_quantity) values (\'{}\',\'{}\',\'{}\')'.format(cart_id, product_id,quantity))
    return True

def update_quantity(cart_id,product_id,quantity):
    db.execute('update ecommerce.cart_product set product_quantity = \'{}\' where cart_id =\'{}\' and product_id = \'{}\''.format(quantity, cart_id, product_id))
    return True

def product_availablity(product_id,quantity):
        availability = db.execute('select quantity from ecommerce.products where id = \'{}\''.format(product_id))
        if availability.fetchone()[0] >= (int(quantity)):
            return True
        else:
            return False
def delete_product_from_cart(cart_id,product_id):
    db.execute('delete from ecommerce.cart_product where cart_id = \'{}\' and product_id = \'{}\''.format(cart_id,product_id))
    return True