

import db_connection
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

base = declarative_base()

class User(base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(30), nullable=False)
    password = Column(String(100), nullable=False)

class Category(base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


class Product(base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    seller_id = Column(Integer, ForeignKey('sellers.id'))
    product_quantity = Column(Integer, nullable=False)


class Cart(base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))


class CartProduct(base):
    __tablename__ = 'cart_products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(Integer, ForeignKey('carts.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, nullable=False)

