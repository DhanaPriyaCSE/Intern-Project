
import db_connection
from db_connection import db

def is_valid_user(user_name,password):
  user = db.execute('select * from users where user_name = \'{}\' and password=\'{}\''.format(user_name,password))
  return True

def get_all_categories():
    categories = db.execute('select * from categories')
    result = [dict(row) for row in categories.fetchall()]
    return result


def get_all_products(category_id):
    products = db.execute('select * from products where category_id = \'{}\''.format(category_id))
    result = [dict(row) for row in products.fetchall()]
    return result

