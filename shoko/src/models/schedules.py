# base class for accessing schedules table 

from .baseModel import Base_Model

class Schedule(Base_Model):
	def __init__(self):
		Base_Model.__init__(self)

		self.conn = self.db_connect()
		self.cur = self.conn.cursor()

		#function to find out if a time slot for a certain machine is free or full
		def is_available(self,time):
			err = 1
			try:
				#TODO find correct sql query
				self.cur.execute("SELECT * FROM schedules WHERE time ="+str(time))
			except:
				print("could not insert into db")
				err = 0
		def reserve_time_slot(self,time):
			err = 1
			self.cur.execute("INSERT INTO schedules VALUES")
