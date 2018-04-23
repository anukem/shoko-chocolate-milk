from flask import Flask
from flask import render_template
from flask import request

import fix_path

from models.users import User
from models.machines import Machine
from models import baseModel as bm

app = Flask(__name__)
loggedIn = False

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
		print("added user")

		if res is 1:
			user.db_close()
			mg = Machine(bm.Base_Model())
			machines = mg.get_all_machines()
			loggedIn = True
			return render_template("LoggedInUsers.html",error=error,machines=machines)
		else:
			user.db_close()
			error = "invalid username/password"
			return render_template("index.html",error=error)

@app.route("/login", methods=["POST"])
def login():
	error = None
	if request.method == "POST":
		try:
			print(request.form['uni'])
			user = User(request.form["uni"],None,request.form["psw"])
			res = user.findUser() 

			user.db_close()
			if res is True:
				loggedIn = True
				return render_template("LoggedInUsers.html",error=error)
			else:
				error = "invalid username/password"
				return render_template("incorrectLogin.html",error=error)
		except Exception as e:
			print(e)
			return render_template("index.html")


	#return render_template("login.html",error=error)

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
    if loggedIn is True:
    	return render_template("LoggedInUsers.html", times=times)
    else:
    	return render_template("index.html")

@app.route('/incorrectLogin')
def incorrectLogin():
	if request.method == "POST":
		user = User(request.form["uni"],request.form["email"],request.form["psw"])
		res = user.findUser() 

		user.db_close()

		if res is 1:
			loggedIn = True
			return render_template("LoggedInUsers.html",error=error)
		else:
			error = "invalid username/password"
			return render_template("incorrectLogin.html",error=error)
    

@app.route('/machineDayschedule')
def machineDayschedule():
	if loggedIn is True:
		return render_template("machineDayschedule.html")
	else:
		return render_template("index.html")

@app.route('/scheduleWorkoutSuccess')
def scheduleWorkoutSuccess():
    # REPLACE THE LINE UNDER WITH ACTUAL DETAILS
	machine = {'type' : 'Treadmill', 'ID' : 't11', 'Time:' : '02:00 pm - 02:30 pm'}
	if loggedIn is True:
		return render_template("scheduleWorkoutSuccess.html", machine=machine)
	else:
		return render_template("index.html")



if __name__ == '__main__':
	app.run(debug=True)
