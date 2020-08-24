from db_connection import *

class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_ke=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    def __init__(self, _user_id):
        self._user_id = _user_id
    
    def get_cart_id(self):
      cart_id =db.execute("select id from ecommerce.cart where  user_id=\'{}\'".format(self._user_id))
      return  cart_id.fetchone()[0]

    def new_cart(self):
        db.execute("insert into ecommerce.cart (user_id) values user_id=\'{}\' ".format(self._user_id))

class CartProduct(Base):
    __tablename__ = 'cart_products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)

    def __init__(self, cart_id, product_id):
        self._cart_id = cart_id
        self._product_id = product_id
        

    def add_to_cart_products(self,quantity):
      db.execute('insert into ecommerce.cart_product (cart_id,product_id,product_quantity) values (\'{}\',\'{}\',\'{}\')'.format(self._cart_id, self._product_id,quantity))
      return True
    
    def update_quantity(self,quantity):
      db.execute('update ecommerce.cart_product set product_quantity = \'{}\' where cart_id =\'{}\' and product_id = \'{}\''.format(quantity, self._cart_id, self._product_id))
      return True

    def delete_product_from_cart(self):
      db.execute('delete from ecommerce.cart_product where cart_id = \'{}\' and product_id = \'{}\''.format(self._cart_id,self._product_id))
      return True

    def get_cart_product_quantity(self):
      quantity = db.execute('select product_quantity from ecommerce.cart_product where cart_id = \'{}\' and product_id = \'{}\''.format(self._cart_id,self._product_id))
      return quantity.fetchone()[0]

