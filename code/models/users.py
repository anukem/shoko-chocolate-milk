# base class for accessing Users table
from model import Base

class User(Base):
	def __init__(self,usename,email,password):
		Base.__init__()

		self.username = username
		self.email = email
		self.password = password
		self.cur = conn.cursor()

	def addUser(username):
		err = 1
		try:
			cur.execute("INSERT INTO users VALUES " + self.name + ", "+ self.email + "," + self.password)
		except:
			print("could not insert into db")
			err = 0

		return err

	def deleteUser(username):
		err = 1
		try:
			cur.execute("DELETE FROM users WHERE username="+username)
		except:
			print("could not execute statement")
			err = 0
			
		return err



