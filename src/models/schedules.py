# base class for accessing schedules table 

from users import User
#from baseModel import Base_Model#local
from Base_Model import Base_Model#live


class Schedule(Base_Model):
	def __init__(self):
		Base_Model.__init__(self)

		self.conn = self.db_connect()
		self.cur = self.conn.cursor()
		self.are_reserved = ["08:00 - 08:30","08:30 - 09:00","09:00 - 09:30","10:00 - 10:00","10:30 - 11:00","11:00 - 11:30","11:30 - 12:00","12:00 - 12:30","12:30 - 13:00","13:00 - 13:30","13:30 - 14:00","14:00 - 14:30","14:30 - 15:00","15:00 - 15:30","15:30 - 16:00","16:00 - 16:30","16:30 - 17:00"]
		#function to find out if a time slot for a certain machine is free or full
	def is_available(self):
		try:
			available = self.cur.execute("SELECT * FROM schedules")
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

	def make_reservation(self,userid):
		try:
			availbility = self.is_available()
			if availability == True:
				self.cur.execute("INSERT INTO schedules VALUES (" + ("'") + (userid) +("'") +(", '")+ (self.mid) + ("',"))
				return print("Your machine is reserved")
		except:
			print("could no insert into db")
			err = 0 
	
	def cancel_reservation(self,userid,mid):
		err = 1
		try:
			self.cur.execute('DELETE FROM schedules WHERE userid=\'%s\' AND machineid=\'%s\''%userid%mid)
		except Exception as e:
			print(e)
			err = 0
			
		return err
	#returns dictionary of all possible times for a machine and whether they are available or not
	def get_available_times(self,mid):
		try:
			#get all reserved times
			self.cur.execute("SELECT * FROM schedules WHERE mid =\'%s\'"%mid)
			records = self.cur.fetchall()

			temp = self.are_reserved
			print(temp)
			for record in records:
				#record[2] corresponds to the time
				time = record[2]
				string = str(time.hour)
				if(time.minute is 0):
					string = string+":"+str(time.minute)+'0'
				else:
					string = string+":"+str(time.minute)
				for s in temp:
					t = s.split(" ")[0]
					
					if t == string:
						temp.remove(s)
				#if string in temp:
				#	temp.remove(string)

			return temp
		except Exception as e:
			print(e)
			return print(e)
		return 1


	def get_all_appointments(self):
		total = []

		try:
			self.cur.execute('select email, time_reserved, type, M.name from users as U, machines as M, schedules as S where S.uid=U.uid and M.mid=S.mid')
			records = self.cur.fetchall()
			#print(records)
			for record in records:
				print(record)
				temp = []
				for item in record: #for formatting
					temp.append(str(item))
				total.append(temp)

			return total


		except Exception as e:
			print(e)

	def get_user_schedule(self,uid):

		try:
			ret = []
			self.cur.execute('select * from schedules where uid = {0}'.format(str(uid)))

			records = self.cur.fetchall()

			for record in records:
				temp = []
				for item in record:
					temp.append(str(item))
				
				ret.append(temp)
			return ret


		except Exception as e:
			print(e)
