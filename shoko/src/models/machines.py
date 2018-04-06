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

		cur.execute("select * from machines")

		for machine in cur.fetchall():
			machines.append(machine)

		return machines 
	def get_a_machine(self,name):

		cur.execute("select * from machines where name is " + name)

		return cur.fetchall()[0]
