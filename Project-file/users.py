from db_connection import *

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, user_name, password):
        self._user_name = user_name
        self._password = password

    def is_valid_user(self):
       db.execute('select * from ecommerce.users where username = \'{}\' and password=\'{}\''.format(self._user_name,self._password))
       return True
    
    def get_user_id(self):
      user = db.execute('select user_id from ecommerce.users where username = \'{}\''.format(self._user_name))
      return user.fetchone()[0]

    def signup_user(self):
        db.execute('insert into ecommerce.users(username,password) values(\'{}\',\'{}\')'.format( self._user_name, self._password))
        return True
    