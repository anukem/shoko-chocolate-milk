
from flask import Flask
from flask import render_template
from flask import request 

import sys

from src.models.users import User


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
		res = user.addUser()

		user.db_close()

		#else:
		#	error = "invalid username/password"
	
	return render_template("machineDayschedule.html",error=error)



@app.route('/machine_schedule')
def machine_schedule():
	return render_template("machineDayschedule.html")

@app.route('/overall_schedule')
def overall_schedule():
	return render_template("overallDaySchedule.html")

if __name__ == '__main__':
    app.run(debug=False)
