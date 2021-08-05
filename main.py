from flask import Flask, request, render_template
import os
import json
import base64

app = Flask(__name__)
if not os.path.exists('data'):
    os.makedirs('data')
@app.route('/')
def index():
    return render_template('index.html')

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
        return 'Welcome {}'.format(name)
    else:
        return 'Invalid username or password'
   
    



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


 
    with open('data/{}_data.json'.format(name), 'w') as outfile:
       json.dump({'username': name, 'passwd': base64_passwd}, outfile)
       
    return ''

    
    