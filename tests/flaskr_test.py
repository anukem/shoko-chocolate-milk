import os
import unittest
import testing.postgresql

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.postgresql = testing.postgresql.Postgresql()

    def tearDown(self):
        self.postgresql.stop()
	
	def test_empty_db(self):
		rv = self.app.get('/')
		assert 'No entries here so far' in rv.data


if __name__ == '__main__':
	unittest.main()
