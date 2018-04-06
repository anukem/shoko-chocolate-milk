import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, './models')))

from users import User

class MyTestCase(unittest.TestCase):
    #user = 0
    def setUp(self):
        self.user = User("test","test","test")

    def test_connection(self):
        res = self.user.addUser()
        self.assertTrue(res)
      
    def tearDown(self):
        self.user.db_close()
	

if __name__ == '__main__':
	unittest.main()
