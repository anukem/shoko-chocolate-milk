from flask import Flask,redirect,url_for
from flask import render_template
from flask import request

import fix_path

from models.users import User
from models.machines import Machine
#from models import baseModel as bm #local
from models import Base_Model as bm #live

app = Flask(__name__)

@app.route('/')
def index():
	incorrectLogin = False
	print(len(request.args))
	if len(request.args) > 0:
		incorrectLogin = request.args['incorrectLogin']
	return render_template("index.html",incorrectLogin=incorrectLogin)

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
			#print(request.form['uni'])
			user = User(request.form["uni"],None,request.form["psw"])
			res = user.findUser()

			#user.db_close()
			# if res is True:
			# 	return redirect(url_for("LoggedInUsers"))
			# else:
			# 	error = "invalid username/password"
			# 	return redirect(url_for("index",incorrectLogin=True))
		except Exception as e:
			print(e)
			return redirect(url_for("index"))


	#return render_template("login.html",error=error)

@app.route('/machine_schedule')
def machine_schedule():
	#machine = Machine()
	#machine.get_all_machines()
	return render_template("machineDayschedule.html")

@app.route('/overall_schedule')
def overall_schedule():
	return render_template("overallDaySchedule.html")

@app.route('/LoggedInUsers',methods=['GET','POST'])
def LoggedInUsers():
	mg = Machine(bm.Base_Model())

	dicts = mg.get_machine_schedule_dictionaries()

	"""tr11times = ["08:00 - 08:30", "14:30 - 15:00"]
    tr12times = ["08:00 - 08:30", "14:30 - 15:00"]
    tr13times = ["08:00 - 08:30", "14:30 - 15:00"]

	nextWorkout = ["Treadill", "tr11", "14:00 - 14:30", "sk4120"]
	
	tr11times = ["08:00 - 08:30", "14:30 - 15:00"]
	tr12times = ["08:00 - 08:30", "14:30 - 15:00"]
	tr13times = ["08:00 - 08:30", "14:30 - 15:00"]

	st11times = ["08:00 - 08:30", "14:30 - 15:00"]
	st12times = ["08:00 - 08:30", "14:30 - 15:00"]
	st13times = ["08:00 - 08:30", "14:30 - 15:00"]

	sk11times = ["08:00 - 08:30", "14:30 - 15:00"]
	sk12times = ["08:00 - 08:30", "14:30 - 15:00"]
	sk13times = ["08:00 - 08:30", "14:30 - 15:00"]

	treadmills = { 'tr11': tr11times, 'tr12': tr12times, 'tr13': tr13times }
	striders = { 'st11': st11times, 'st12': st12times, 'st13': st13times }
	skis = { 'sk11': sk11times, 'sk12': sk12times, 'sk13': sk13times }

	machines = {
        'Treadmills': treadmills,
        'Striders': striders,
        'Skis': skis
		}"""

	return render_template("LoggedInUsers.html", machines=dicts, nextWorkout=nextWorkout)


@app.route('/incorrectLogin')
def incorrectLogin():
	if request.method == "POST":
		user = User(request.form["uni"],request.form["email"],request.form["psw"])
		res = user.findUser()

		user.db_close()

		if res is 1:
			return render_template("LoggedInUsers.html",error=error)
		else:
			error = "invalid username/password"
			return render_template("incorrectLogin.html",error=error)


@app.route('/gymSchedule')
def gymSchedule():
	s = Schedule()
	ret = s.get_all_appointments()
	return render_template("gymSchedule.html",workouts = ret)


@app.route('/cancelSuccess')
def cancelSuccess():
    return render_template("cancelSuccess.html")

@app.route('/scheduleSuccess')
def scheduleSuccess():
    # REPLACE THESE PLACEHOLDERS WITH ACTUAL DATA
    workout = {'type': 'Treadmill', 'ID': 't11', 'Time': '02:00 pm - 02:30 pm'}
    return render_template("scheduleSuccess.html", workout=workout)


@app.route('/about')
def about():
	return render_template("about.html")

if __name__ == '__main__':
	try:
	  import googleclouddebugger
	  googleclouddebugger.enable()
	except ImportError:
	  pass
	app.run(debug=True)
