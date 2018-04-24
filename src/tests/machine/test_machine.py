import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, './models')))

from baseModel import Base_Model
from machines import Machine


class MyTestCase(unittest.TestCase):
    
    def setUp(self):
        self.machine = Machine("treadmill_test")
        

    def test_get_all(self):
        try:
            self.machine = Machine("treadmill_0")

            ms = self.machine.get_all_machines()
            print(ms)

            self.assertTrue(len(ms)>0)

        except Exception as e:
            print(e)

    def test_get_machine_schedules(self):
        self.machine = Machine("tr11")

        res = self.machine.get_machine_schedule_dictionaries()
        print("dict")
        print(res)

    
    def tearDown(self):
        self.machine.db_close()
    
	

if __name__ == '__main__':
	unittest.main()
