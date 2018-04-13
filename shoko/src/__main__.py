
from flask import Flask
from flask import render_template
from flask import request 

import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, '/src/models/')))
from models.users import User
from models.machines import Machine
from models import Base_Model as bm 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

    #return render_template("index.html")

#placeholder function
@app.route('/login', methods=['POST'])
def login():
	error = None
	if request.method == "POST":
		user = User(request.form["uni"],request.form["psw"],"test")

		res = user.findUser()
		user.db_close()
		if res == True:
			return render_template("machineDayschedule.html",error=error, machines=machines)

		

	
	return render_template("machineDayschedule.html",error=error, machines=machines)

def signin():
	error = None
	if request.method == "POST":
		user = User(request.form["uni"],request.form["psw"],"test")
		res = user.findUser()

		user.db_close()

		if res == 1:
			return render_template("machineDayschedule.html",error=error)
		else:
			error = "invalid username/password"
	
	
@app.route('/machine_schedule')
def machine_schedule():
	#machine = Machine()
	#machine.get_all_machines()
	return render_template("machineDayschedule.html")

@app.route('/overall_schedule')
def overall_schedule():
	return render_template("overallDaySchedule.html")

if __name__ == '__main__':
    app.run(debug=False)
