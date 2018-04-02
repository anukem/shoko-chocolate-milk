import psycopg2 as psy 

class Base_Model:

	def __init__(self, hostname= "35.229.79.41", 
				db_username = "postgres", 
				db_password="i8KND8LOodrh2kbp",
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
		

