import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, './models')))

from schedules import Schedule

class MyTestCase(unittest.TestCase):

	def setUp(self):
		self.schedule = Schedule(mid=1)


	def test_func(self):
		res = self.schedule.get_available_times()
		print(res)
		self.assertEqual(res,['8:00', '8:30', '9:00', '10:00', '10:30', '11:00', '11:30', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00'])
		
	def tearDown(self):
		self.schedule.db_close()

if __name__ == '__main__':
	unittest.main()