from db_connection import *
import re

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, user_name, password):
        self._user_name = user_name
        self._password = password

    def is_valid_user(self):
        user=db.execute("select * from ecommerce.users where username = \'{}\' and password=\'{}\'".format(self._user_name,self._password))
        data = user.fetchone()
        print(data)
        if data is not None:
            return True
        else:
            return False
    
    def get_user_id(self):
        user = db.execute('select user_id from ecommerce.users where username = \'{}\''.format(self._user_name))
        data = user.fetchone()[0]
        print(data)
        if data is not None:
            return data


    def validate_name(self):
        name=self._user_name
        if re.match(r'^[a-zA-Z]+$',name ):
            return True
        else:
            return False

    def signup_user(self):
        if self.is_exist_user() == False:
            user = db.execute('insert into ecommerce.users(username,password) values(\'{}\',\'{}\')'.format(self._user_name,self._password))
            return True
        else:
            return False

    def is_exist_user(self):
        user= db.execute('select * from ecommerce.users where username = \'{}\''.format(self._user_name))
        data = user.fetchone()
        if data is not None:
            return True
        else:
            return False
