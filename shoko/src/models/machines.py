# base class for accessing machines table 
from models import Base_Model

class Machine(Base_Model):
	"""docstring for Machine"""
	def __init__(self):
		super(Machine, self).__init__()
		

	def get_all_machines(self):
		machines = []
		conn = self.db_connect()

		cur = conn.cursor()
		cur.execute("select * from machines")

		for machine in cur.fetchall():
			machines.append(machine)

		return machines 

# test the class 
first_machine = Machine()
print(Machine().get_all_machines())
