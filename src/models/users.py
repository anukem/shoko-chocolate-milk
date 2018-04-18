# base class for accessing Users table
import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, '/shoko/src/models')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, './models')))
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
		err = True
		print("INSERT INTO users VALUES (" + ("'") + (self.username) +("'") +(", '")+ (self.email) + ("','") + (self.password)+("')"))

		try:
			self.cur.execute("INSERT INTO users VALUES (" + ("'") + (self.username) +("'") +(", '")+ ("FAKE@EMAIL.COM") + ("','") + (self.password)+("')"))
			self.conn.commit()
		except:
			print("could not insert into db")
			err = False

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
			err = 0

		records = cur.fetchall()

		if(len(records >= 1)):
			return True
		else:
			return False
		



