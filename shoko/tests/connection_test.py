import os
import unittest
from .models.users import User

class MyTestCase(unittest.TestCase):
    def setUp(self):
        user = User("test","test","test")

    def test_connection(self):
    	res = user.addUser(username)
        user.addUser()

    	assertsTrue()

    def tearDown(self):
        self.postgresql.stop()
	
	

if __name__ == '__main__':
	unittest.main()
