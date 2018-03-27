#from google.appengine.ext import vendor
#vendor.add('lib')

from flask import Flask
from flask import render_template
from flask import request 

import sys

from models.users import User

app = Flask(__name__)


# dynamodb = boto3.resource(
#     'dynamodb',
#     endpoint_url='http://localhost:8000',
#     region_name='dummy_region',
#     aws_access_key_id='dummy_access_key',
#     aws_secret_access_key='dummy_secret_key',
#     verify=False)


@app.route('/')
def index():
    return render_template("index.html")

    #return render_template("index.html")

#placeholder function
@app.route('/login', methods=['POST'])
def login():
	error = None
	if request.method == "POST":
		signup_the_user( request.form["uni"],request.form["psw"])

		#else:
		#	error = "invalid username/password"
	
	return render_template("machineDayschedule.html",error=error)

def signup_the_user(username,password):
	
	user = User(username,password,"test")
	user.db_connect()

	res = user.addUser(username)

	user.db_close()

	return res


@app.route('/machine_schedule')
def machine_schedule():
	return render_template("machineDayschedule.html")

@app.route('/overall_schedule')
def overall_schedule():
	return render_template("overallDaySchedule.html")

if __name__ == '__main__':
    app.run(debug=True)
