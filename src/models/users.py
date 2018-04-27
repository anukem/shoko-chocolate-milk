# base class for accessing Users table
import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, '/shoko/src/models')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, './models')))
from baseModel import Base_Model


import sys

class User(Base_Model):

	def __init__(self,username=None,email=None,password=None):
		Base_Model.__init__(self)
		self.username = username
		self.email = email
		self.password = password
		self.conn = self.db_connect()
		self.cur = self.conn.cursor()
		self.user_id = None

	def addUser(self):
		err = True
		res = self.findUser()
		print(res)
		print("INSERT INTO users VALUES (" + ("'") + (self.username) +("'") +(", '")+ (self.email) + ("','") + (self.password)+("')"))
		if(res[0] == True):
			err ="username/password already exists"
			return err
		try:
			self.cur.execute("INSERT INTO users VALUES (" + ("'") + (self.username) +("'") +(", '")+ (self.email) + ("','") + (self.password)+("');"))
			self.conn.commit()
		except Exception as e:
			print(e)
			err = "exception"

		return err

	def getPwd(self):

		self.cur.execute('SELECT * FROM users WHERE name=\'{0}\' and password=\'{1}\''.format(str(self.username),str(self.password)))
		record = self.cur.fetchone()
		if record != None:
			return record[2]
		else:
			return False



	def deleteUser(self, username):
		err = 1
		try:
			self.cur.execute('DELETE FROM users WHERE name=\'{0}\' and password=\'{1}\''.format(str(self.username),str(self.password)))
			self.conn.commit()
		except Exception as e:
			print(e)
			print("deleteUser() failed! => could not execute statement")
			err = 0
			
		return err

	def findUser(self):
		try:

			print('SELECT * FROM users WHERE name=\'{0}\' and password=\'{1}\''.format(str(self.username),str(self.password)))
			self.cur.execute('SELECT * FROM users WHERE name=\'{0}\' and password=\'{1}\''.format(str(self.username),str(self.password)))
			records = self.cur.fetchall()
			print(records)
			print(len(records))
			#print(records)
			#print(len(records))
			if(len(records) >= 1):
				return True,records[0][3]
			else:
				return False,None
		except Exception as e :
			print(e)
			return False,None

	def setUserID(self):
		err = 1
		try:
			self.cur.execute('SELECT * FROM users WHERE name=\'%s\''%str(self.username))	
			record = self.cur.fetchone()
			#record[3] is the id column in the db
			record[3] = self.user_id
		except Exception as e:
			print(e)
	def getNameFromID(self,id):
		self.cur.execute('SELECT * FROM users WHERE uid=\'{0}\''.format(id))
		record = self.cur.fetchone()

		return record[0]

	def getIDFromName(self,name):
		self.cur.execute('SELECT * FROM users WHERE name = \'{0}\''.format(name))
		record = self.cur.fetchone()

		return record[3]



		
