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
		self.user_id = None

	def addUser(self):
		err = 1
		print("INSERT INTO users VALUES (" + ("'") + (self.username) +("'") +(", '")+ (self.email) + ("','") + (self.password)+("')"))
		try:
			self.cur.execute("INSERT INTO users VALUES (" + ("'") + (self.username) +("'") +(", '")+ (self.email) + ("','") + (self.password)+("');"))
			self.conn.commit()
		except Exception as e:
			print(e)
			print("not working!!!!!!!")
			err = 0

		return err

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
			#print('SELECT * FROM users WHERE name=\'%s\''%str(self.username))
			self.cur.execute('SELECT FROM users WHERE name=\'{0}\' and password=\'{1}\''.format(str(self.username),str(self.password)))
			records = self.cur.fetchall()
			#print(records)
			#print(len(records))
			if(len(records) >= 1):
				return True
			else:
				return False
		except Exception as e :
			print(e)
			return False

	def setUserID(self):
		err = 1
		try:
			self.cur.execute('SELECT * FROM users WHERE name=\'%s\''%str(self.username))	
			record = self.cur.fetchone()
			#record[3] is the id column in the db
			record[3] = self.user_id
		except Exception as e:
			print(e)



		
