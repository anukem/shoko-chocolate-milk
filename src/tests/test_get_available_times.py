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
		self.assertEqual(res, ["08:00 - 08:30","08:30 - 09:00","09:00 - 09:30","10:00 - 10:00","10:30 - 11:00","11:00 - 11:30","11:30 - 12:00","12:30 - 13:00","13:00 - 13:30","13:30 - 14:00","14:00 - 14:30","14:30 - 15:00","15:00 - 15:30","15:30 - 16:00","16:00 - 16:30","16:30 - 17:00"])

		
	def tearDown(self):
		self.schedule.db_close()

if __name__ == '__main__':
	unittest.main()