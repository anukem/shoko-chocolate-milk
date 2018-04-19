from flask import Flask
from flask import render_template
from flask import request

import fix_path

from models.users import User
from models.machines import Machine
from models import Base_Model as bm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

#placeholder function
@app.route('/sign_up', methods=['POST'])
def sign_up():
	error = None
	if request.method == "POST":
		user = User(request.form["uni"],request.form["email"], request.form["psw"]	)
		res = user.addUser()

		if res == 1:
			return render_template("LoggedInUsers.html",error=error)
		else:
			error = "invalid username/password"

		user.db_close()

	mg = Machine(bm.Base_Model())
	machines = mg.get_all_machines()

	return render_template("LoggedInUsers.html",error=error, machines=machines)

@app.route("/login", methods=["POST"])
def login():
	error = None
	if request.method == "POST":
		user = User(request.form["uni"],request.form["email"],request.form["psw"])
		res = user.findUser()

		user.db_close()

		if res == 1:
			return render_template("LoggedInUsers.html",error=error)
		else:
			error = "invalid username/password"
	return render_template("machineDayschedule.html",error=error)

@app.route('/machine_schedule')
def machine_schedule():
	#machine = Machine()
	#machine.get_all_machines()
	return render_template("machineDayschedule.html")

@app.route('/overall_schedule')
def overall_schedule():
	return render_template("overallDaySchedule.html")

@app.route('/LoggedInUsers')
def LoggedInUsers():
    times = [
        "10:00 am - 10:30 am",
        "10:30 am - 11:00 am",
        "11:30 am - 12:00 pm",
        "12:00 pm - 12:30 pm",
        "12:30 pm - 01:00 pm",
        "01:00 pm - 01:30 pm",
        "01:30 pm - 02:00 pm",
        "02:00 pm - 02:30 pm",
        "02:30 pm - 03:00 pm",
        "03:00 pm - 03:30 pm"
    ]
    return render_template("LoggedInUsers.html", times=times)

@app.route('/incorrectLogin')
def incorrectLogin():
    return render_template("incorrectLogin.html")

@app.route('/machineDayschedule')
def machineDayschedule():
    return render_template("machineDayschedule.html")

@app.route('/scheduleWorkoutSuccess')
def scheduleWorkoutSuccess():
    # REPLACE THE LINE UNDER WITH ACTUAL DETAILS
    machine = {'type' : 'Treadmill', 'ID' : 't11', 'Time:' : '02:00 pm - 02:30 pm'}
    return render_template("scheduleWorkoutSuccess.html", machine=machine)



if __name__ == '__main__':
	app.run(debug=True)
