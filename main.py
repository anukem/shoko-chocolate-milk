from flask import Flask,redirect,url_for,flash,session
from flask import render_template
from flask import request
from flask_session import Session

import fix_path

from models.users import User
from models.machines import Machine
from models.schedules import Schedule
from models import baseModel as bm

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
app.secret_key = 'key'
Session(app)
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
		if res is True:
			uid = user.getIDFromName(request.form["uni"])
			session['uid'] = uid
			user.db_close()
			mg = Machine(bm.Base_Model())
			machines = mg.get_all_machines()
			return render_template("LoggedInUsers.html",error=error,machines=machines)
		else:
			user.db_close()
			error = "invalid username/password"
			return render_template("index.html",error=error)

@app.route("/login", methods=['POST'])
def login():
	if request.method == 'POST':
		try:
			#print(request.form['uni'])
			user = User(request.form["uni"],None,request.form["psw"])
			res = user.findUser()

			user.db_close()
			if res[0] is True:
				print("res")
				print(res[1])
				session['uid'] = res[1] 
				return redirect(url_for("LoggedInUsers"))
			else:
				error = "invalid username/password"
				return redirect(url_for("index",incorrectLogin=True))
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
	#print(dicts)
	tr11times = ["08:00 - 08:30", "14:30 - 15:00"]
	tr12times = ["08:00 - 08:30", "14:30 - 15:00"]
	tr13times = ["08:00 - 08:30", "14:30 - 15:00"]


	s = Schedule()
	ret = s.get_user_schedule(session["uid"])
	s.db_close()
	mg.db_close()

	return render_template("LoggedInUsers.html", machines=dicts, nextWorkout=ret,uid=session['uid'])


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

@app.route('/scheduleWorkout',methods=['POST'])
def scheduleWorkout():
	s = Schedule()
	u = User()
	try:
		workoutTime = request.form[("time")]
		uni = request.form["uni"]
		mid = request.form['optradio']
		#name = u.getNameFromID(uni)
		uid = u.getIDFromName(uni)
		print(uid)
		print("w is:")
		w = [uid,workoutTime,mid]
		print(w)
		success = s.make_reservation(workoutTime,uid,mid)
		if success == True:
			return redirect(url_for("scheduleSuccess",workout=w))
		else:
			print("error")
			redirect(url_for("index.html"))
	except Exception as e:
		print(e)
		redirect(url_for("index.html"))
	#s.makeReservation()

@app.route('/gymSchedule',methods=['GET','POST'])
def gymSchedule():
	s = Schedule()
	ret = s.get_all_appointments()
	print(ret)
	return render_template("gymSchedule.html",workouts = ret)


@app.route('/cancelSuccess')
def cancelSuccess():
    return render_template("cancelSuccess.html")

@app.route('/scheduleSuccess',methods=['POST','GET'])
def scheduleSuccess():
	if request.method == 'GET':

		w = request.args['workout']
		return render_template("scheduleSuccess.html",workout=w)

	if request.method == 'POST':
		w = request.args['workout']

		return render_template("scheduleSuccess.html",workout=w)



@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/cancelWorkout',methods=['POST'])
def cancelWorkout():
	s = Schedule()
	u = User()
	uni = request.form['uni']
	uid = u.getIDFromName(uni)
	workoutExists = True
	nextWorkout = s.get_user_schedule(uid)#["Treadill", "tr11", "14:00 - 14:30", "sk4120"]
	nextWorkout = nextWorkout[0]
	print(uni)
	print(nextWorkout)
	nextWorkout.append(uni)
	print(nextWorkout)
	if nextWorkout is not None:
		s.cancel_reservation(nextWorkout[0],nextWorkout[1])

		return render_template("cancelWorkout.html", nextWorkout=nextWorkout,workoutExists = workoutExists)
	else:
		return redirect(url_for("index.html"))

@app.route('/logout')
def logout():
	session["uni"] = None
	return redirect(url_for("index"))


if __name__ == '__main__':
	try:
	  import googleclouddebugger
	  googleclouddebugger.enable()
	except ImportError:
	  pass

	app.run(debug=True)
