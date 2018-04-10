import unittest
from shoko.src.models.users import User


class MyTestCase(unittest.TestCase):
    
    def setUp(self):
        user = User("test","test","test")

    def test_connection(self):

        try:
            #if user is found return true
        	res = user.findUser()
        	self.assertTrue(res)
        except:
        	print("error")
        

    def tearDown(self):
        user.db_close()
	

if __name__ == '__main__':
	unittest.main()
