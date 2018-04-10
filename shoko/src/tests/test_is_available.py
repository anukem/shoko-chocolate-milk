import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, './models')))

from schedules import Schedule
from machines import Machine

class MyTestCase(unittest.TestCase):
    
    def setUp(self):
    	machine = Machine("treadmill_test")

    def test_pass(self):
        res = machine.schedule.is_available("12:00")

        self.assertTrue(res)
        
    def test_fail(self):
        res = machine.schedule.is_available("3:00")  #gym closed

        self.assertFalse(res)

    def tearDown(self):
    	machine.db_close()
if __name__ == '__main__':
	unittest.main()
