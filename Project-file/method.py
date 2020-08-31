from db_connection import *
from cart import *
from category import *
from product import *


def get_all_categories():
    categories = db.execute('select * from ecommerce.categories')
    result = [dict(row) for row in categories.fetchall()]
    return result

def get_all_products(category_id):
    products = db.execute('select * from ecommerce.products where fk_category_id = \'{}\''.format(category_id))
    result = [dict(row) for row in products.fetchall()]
    return result

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

def display_product_format(product, cart_id):
        product_list = {}
        product_list['product_id'] = product.id
        product_list['name'] = product.name
        product_list['price'] = product.price
        product_list['category_name'] = Category(product.fk_category_id).get_category_name()
        # product_list['seller_name'] = Seller(product.seller_id).get_seller_name()
        # product_list['quantity'] = product.quantity
        product_list['quantity'] = CartProduct(cart_id,product.id).get_cart_product_quantity()
        return product_list
