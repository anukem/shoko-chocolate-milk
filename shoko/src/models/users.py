# base class for accessing Users table
from baseModel import Base_Model
import sys

class User(Base_Model):

	def __init__(self,username,email,password):
		Base_Model.__init__(self)
		self.username = username
		self.email = email
		self.password = password
		self.conn = self.db_connect()
		self.cur = self.conn.cursor()

	def addUser(self):
		err = 1
		print("INSERT INTO users VALUES (" + ("'") + (self.username) +("'") +(", '")+ (self.email) + ("','") + (self.password)+("'o)"))

		try:
			self.cur.execute("INSERT INTO users VALUES (" + ("'") + (self.username) +("'") +(", '")+ (self.email) + ("','") + (self.password)+("')"))
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

	def findUser():
		err = 1
		try:
			cur.execute("SELECT * FROM users WHERE username=" + username)
		except:
			print("could not execute statement")

		records = cur.fetchall()

		if(len(records >= 1)):
			return 1
		else:
			return 0
		



