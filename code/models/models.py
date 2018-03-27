import psycopg2 as psy 

class Base:
	def __init__(hostname= "35.229.79.41", 
				db_username = "postgres", 
				db_password="i8KND8LOodrh2kbp",
				dbname = "postgres"):

		self.hostname = hostname
		self.db_username = db_username
		self.db_password = db_password
		self.dbname = dbname
		self.conn = None


	def db_connect():
		self.conn = psy.connect(host=hostname, user=db_username, password=db_password, dbname=db_name)

	def db_close():
		self.conn.close()
		

