import psycopg2 as psy 
import os 

class Base_Model:

	def __init__(self, hostname= os.environ['DB_HOSTNAME'], 
				db_username = "postgres", 
				db_password=os.environ['DB_PASSWORD'],
				dbname="postgres"):

		self.hostname = hostname
		self.db_username = db_username
		self.db_password = db_password
		self.dbname = dbname
		self.conn = None


	def db_connect(self):
		self.conn = psy.connect(host=self.hostname, 
			user=self.db_username, 
			password=self.db_password, 
			dbname=self.dbname)
		return self.conn 

	def db_close(self):
		self.conn.close()
		

