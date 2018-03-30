import unittest
from users import User

class MyTestCase(unittest.TestCase):
    
    user = User("test","test","test")

    def test_connection(self):
        res = user.addUser(username)

        try:
        	user.addUser()
        	self.assertTrue()
        except:
        	self.assertFalse()
        
        user.db_close()
	

if __name__ == '__main__':
	unittest.main()
