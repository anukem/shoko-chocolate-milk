import os
import unittest
import testing.postgresql

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.postgresql = testing.postgresql.Postgresql()

    def test_connection(self):
    	conn = PG::Connection.open(dbname: 'test')
    	assertsTrue()

    def tearDown(self):
        self.postgresql.stop()
	
	

if __name__ == '__main__':
	unittest.main()
