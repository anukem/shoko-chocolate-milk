from baseModel import Base

class User(Base):
	def __init__(self,usename,password):
		Base.__init__()

		self.username = username
		self.password = password

	def addUser(username)