
from db_connection import *

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

    def __init__(self, category_id):
        self._category_id = category_id

    def get_category_details(self):
        _category = db.execute('select * from ecommerce.categories where id = \'{}\''.format(self._category_id))
        category_dict = {}
        category_dict['category_id'] = _category.id
        category_dict['category_name'] = _category.name
        return category_dict

    def get_category_name(self):
      category_name= db.execute('select name from ecommerce.categories where id = \'{}\''.format(self._category_id))
      return category_name.fetchone()[0]

