import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, './models')))

from baseModel import Base_Model
from machines import Machine
from users import User


class MyTestCase(unittest.TestCase):
    
    def setUp(self):
        self.user = User("test_account", "test@test.com", "password1234")
        self.user.addUser()

    def test_login(self):
        assert(self.user.findUser() == True)
        
        
    def tearDown(self):
        self.user.deleteUser("test_account")
        self.user.db_close()

	

if __name__ == '__main__':
	unittest.main()
