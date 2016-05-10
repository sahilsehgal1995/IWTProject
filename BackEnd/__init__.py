from flask import Flask, session, jsonify, request
from flask.ext.cors import CORS
from database import registerTeacher, loginTeacher, FetchSyllabus, Fetchstudents, FetchTeachers
import gc
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~Xsa!jmN]LWX/,?RT'

CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
  return 'CSE Department UIET'

@app.route('/api/Teacher/login/', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    reply, user = loginTeacher(request.args.get('user'))
    if reply == 'Login Success':
      session['id'] = user['_id']
      session['Email'] = user['Email']
      session['user'] = 'Customer'
      user['responsse']='Login Successfull'
      return reply
    else:
      return reply
  return 'Invalid Request'

@app.route('/api/Teacher/signup/', methods=['GET','POST'])
def signup():
  if request.method == 'POST':
    reply = registerTeacher(request.args.get('user'))
    return reply
  return 'Invalid Request'

@app.route('/api/Fetchstudents/', methods=['GET', 'POST'])
def FetchStudents():
  if request.method=='POST':
    return Fetchstudents()
  return 'Invalid Request'

@app.route('/api/FetchSyllabus/', methods=['GET', 'POST'])
def Fetchsyllabus():
  if request.method=='POST':
    return FetchSyllabus()
  return 'Invalid Request'

@app.route('/api/FetchTeachers/', methods=['GET', 'POST'])
def Fetchteachers():
  if request.method=='POST':
    return FetchTeachers()
  return 'Invalid Request'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
