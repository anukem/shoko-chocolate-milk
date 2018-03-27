#from google.appengine.ext import vendor
#vendor.add('lib')

from flask import Flask
from flask import render_template
from flask import request 




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
		if is_valid_login( request.form(['username']), request.form(["password"])):
			login_the_user( request.form(["username"]))

		else:
			error = "invalid username/password"
	
	return render_template("login.html",error=error)

def login_the_user(username):
	#connect to database and add user

@app.route('/machine_schedule')
def schedule():
	return render_template("machineDayschedule.html")

@app.route('/overall_schedule')
def schedule():
	return render_template("overallDaySchedule.html")

if __name__ == '__main__':
    app.run(debug=True)
