from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
import os
import json
import base64
import time


if not os.path.exists('data'):
    os.makedirs('data')


app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "static/uploads/"


@app.route('/')
def home():
    return 'Index Page'

  
@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def signin_post():
    name = request.form['name']
    passwd = request.form['passwd']
    
    passwd_bytes = passwd.encode('ascii')
    base64_bytes = base64.b64encode(passwd_bytes)
    base64_passwd = base64_bytes.decode('ascii')

    #os check file
    if os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'r') as f:
            i = json.load(f)
            
    elif not os.path.exists('data/{}_data.json'.format(name)):
        return 'user not found'

    if i["username"] == name and i["passwd"] == base64_passwd:
        return  "<script>window.location.href = '/userinfo/{}';</script>".format(name)
    else:
        return 'Invalid username or password <a href="/signin">Sign In</a>'
   
    



@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    name = request.form['name']
    passwd = request.form['passwd']
    
    passwd_bytes = passwd.encode('ascii')
    base64_bytes = base64.b64encode(passwd_bytes)
    base64_passwd = base64_bytes.decode('ascii')


    #os search file
    if os.path.exists('data/{}_data.json'.format(name)):
        return 'user already exists <a href="/signup">Sign Up</a>'
    elif not os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'w') as outfile:
            json.dump({'username': name, 'passwd': base64_passwd, 'img': '', 'score': 0}, outfile)
        with open('data/api/{}_data.json'.format(name), 'w') as outfile:
            json.dump({'username': name, 'img': '', 'score': 0}, outfile)
       
       
    return  "<script>window.location.href = '/signin';</script>"


@app.route('/userinfo/<name>')
def userinfo(name):
    if os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'r') as f:
            i = json.load(f)
            
    elif not os.path.exists('data/{}_data.json'.format(name)):
        return 'user not found'
    if i["score"] < 0:
        score = 'Error'
    else:
        score = i["score"]
    return render_template('userinfo.html', name=i["username"], score=score, img=i["img"])

@app.route('/api/<name>')
def api(name):
    if os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'r') as f:
            i = json.load(f)
    
    return json.dumps({'username': i["username"], 'img': i["img"], 'score': i["score"]})