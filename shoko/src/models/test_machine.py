import unittest
from .machines import Machine


class MyTestCase(unittest.TestCase):
    
    def setUp(self):
        machine = Machine("treadmill_test")
        

    def test_get_all(self):
        try:
            machine = Machine("treadmill_0")

            ms = machine.get_all_machines()

            self.assertTrue(len(ms)>0)

        except:
            print("error")

    
    def tearDown(self):
        machine.db_close()
    
	

if __name__ == '__main__':
	unittest.main()
