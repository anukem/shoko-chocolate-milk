import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, './models')))

from schedules import Schedule

class MyTestCase(unittest.TestCase):

	def setUp(self):
		self.schedule = Schedule(mid=1)


	def test_func(self):
		res = self.schedule.get_all_appointments()
		assert(len(res) != 0)
		
	def tearDown(self):
		self.schedule.db_close()

if __name__ == '__main__':
	unittest.main()