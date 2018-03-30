import unittest
from src.models.users import User

class MyTestCase(unittest.TestCase):
    
    user = User("test","test","test")

    def test_connection(self):
        res = user.addUser(username)

        try:
        	user.addUser()
        	self.assertTrue()
        except:
        	self.assertFalse()
        

    def tearDown(self):
        user.db_close()
	

if __name__ == '__main__':
	unittest.main()
