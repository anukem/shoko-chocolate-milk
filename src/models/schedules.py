# base class for accessing schedules table 

from users import User

class Schedule():
	def __init__(self,machineid):
		Base_Model.__init__(self)

		self.conn = self.db_connect()
		self.cur = self.conn.cursor()
		self.machineid = machineid

		#function to find out if a time slot for a certain machine is free or full
		def is_available(self):
			try:
				available = self.cur.execute("SELECT * FROM machines WHERE machineid IS NULL")
				records = cur.fetchall()
				if(len(records) is 0):
					return True
				else:
					return False
				#TODO find correct sql query
				#self.cur.execute("SELECT * FROM schedules WHERE time ="+str(time))
			except Exception as e:
				print(e)
			
		
		#def reserve_time_slot(self,time):
		#	err = 1
		#	self.cur.execute("INSERT INTO schedules VALUES (%s,%s,%s) ", (self.user_id,self.machineid,time))

		def make_reservation(userid,machineid,time):
			try:
				availbility = self.is_available()
				if availability == True:
					self.cur.execute("INSERT INTO schedules VALUES (" + ("'") + (userid) +("'") +(", '")+ (machineid) + ("',"))
					return print("Your machine is reserved")
			except:
				print("could no insert into db")
				err = 0 
		
		def cancel_reservation(userid,machineid):
			err = 1
			try:
				self.cur.execute("DELETE FROM schedules WHERE userid="+userid + "AND machineid="+machineid)
			except:
				print("could not execute statement")
				err = 0
				
			return err

