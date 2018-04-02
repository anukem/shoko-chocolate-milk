import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'code')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'code/models')))
import unittest
from models import machines as mac 

class MachineTest(unittest.TestCase):
	
	def setUp(self):
		self.machine_in_test = mac.Machine()
		self.conn = self.machine_in_test.db_connect()				

	def test_create_machine(self):
		# data to insert
		cursor = self.conn.cursor()
		name = "machine_test"
		typ = "Bicycle"
		location = "5th Floor, Test Room"
				
		# check to see the insert passed
		cursor.execute("insert into machines (name, type, location) values (%s,%s,%s)", (name, typ, location))
		assert(cursor.statusmessage == "INSERT 0 1")

	def tearDown(self):
		self.conn.close()

if __name__ == '__main__':
    unittest.main()
