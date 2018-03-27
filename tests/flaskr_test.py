import os
import unittest
import sqlalchemy


class TestDB(unittest.TestCase):
	"""
	will try to fetch the database URL to use from an environment variable, and
	then wiill rely on SQLAlchemy to create a database conncection 
	"""  
	def setUp(self):
		url = os.getenv("DB_TEST_URL")
		if not url:
			self.skipTest("No database URl set")
		self.engine = sqlalchemy.create_engine(url)

	def test_empty_db(self):
		rv = self.app.get('/')
		assert 'No entries here so far' in rv.data


if __name__ == '__main__':
	unittest.main()
