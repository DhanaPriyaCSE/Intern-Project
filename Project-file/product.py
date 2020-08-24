  
from db_connection import *
from category import *
from seller import *

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    seller_id = Column(Integer, ForeignKey('sellers.id'))
    quantity = Column(Integer, nullable=False) 

    def __init__(self, product_id):
        self._product_id = product_id
    
    # def display_product_format(self):
    #   product=db.execute("select * from products where id='{}'".format(self._product_id))
    #   product_list = {}
    #   product_list['product_id'] = product.id
    #   product_list['name'] = product.name
    #   product_list['price'] = product.price
    #   product_list['category_name'] = Category(product.fk_category_id).get_category_name()
    #   product_list['seller_name'] = Seller(product.seller_id).get_seller_name()
    #   product_list['quantity'] =product.quantity
    #   return product_list
    #
    def product_availablity(self,quantity):
        availability = db.execute('select quantity from ecommerce.products where id = \'{}\''.format(self._product_id))
        if availability.fetchone()[0] >= (int(quantity)):
            return True
        else:
            return False

    def get_all_products(self,category_id):
        products = db.execute('select * from ecommerce.products where fk_category_id = \'{}\''.format(category_id))
        result = [dict(row) for row in products.fetchall()]
        return result

    def get_product_details(self):
        product = db.execute("select * from ecommerce.products where  id=\'{}\'".format(self._product_id))
        result = [dict(row) for row in product.fetchall()]
        return result