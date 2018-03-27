# base class for accessing Users table
from baseModel import Base

class User(Base):
	def __init__(self,usename,email,password):
		Base.__init__()

		self.username = username
		self.email = email
		self.password = password
		self.cur = conn.cursor()

	def addUser(username):

		try:
			cur.execute("INSERT INTO users VALUES " + self.name + ", "+ self.email + "," + self.password)
		except:
			print("could not insert into db")

	def deleteUser(username):
		
		try:
			cur.execute("DELETE FROM users WHERE username="+username)
		except:
			print("could not execute statement")



