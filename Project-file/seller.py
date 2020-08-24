from db_connection import *

class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __init__(self, seller_id):
        self._seller_id = seller_id

    def get_seller_name(self):
        _seller_name =db.execute('select name from ecommerce.sellers where id = \'{}\''.format(self._seller_id))
        return _seller_name.fetchone()[0]