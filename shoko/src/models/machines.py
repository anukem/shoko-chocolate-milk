# base class for accessing machines table 
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, './models')))
from baseModel import Base_Model
from schedules import Schedule

class Machine(Base_Model):
	"""docstring for Machine"""
	def __init__(self,name):
		Base_Model.__init__(self)
		self.name = name
		self.conn = self.db_connect()
		self.cur = self.conn.cursor()
		schedule = Schedule()
	#@staticmethod
	
	def get_all_machines(self):
		machines = []
		conn = self.db_connect()

		cur = conn.cursor()
		cur.execute("select * from machines")

		for machine in cur.fetchall():
			machines.append(machine)

		return machines 

	def create_machine(self):
		conn = self.db_connect()
		cur = conn.cursor()
		cur.execute("INSERT INTO machines VALUES ( DEFAULT, 'Yellow Machine', 'Elliptical', '712 Schermerhorn');")
		print(cur.statusmessage)
		conn.commit()


machine = Machine(Base_Model())

machine.create_machine()

