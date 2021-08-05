from flask import Flask, request, render_template
import os
import json
import base64

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('signin.html')

@app.route('/', methods=['POST'])
def my_form_post():
    name = request.form['name']
    passwd = request.form['passwd']
    
    passwd_bytes = passwd.encode('ascii')
    base64_bytes = base64.b64encode(passwd_bytes)
    base64_passwd = base64_bytes.decode('ascii')

    #os check directory
    if not os.path.exists('data'):
        os.makedirs('data')
        with open('data/{}_data.json'.format(name), 'w') as outfile:
            json.dump({'name': name, 'passwd': base64_passwd}, outfile)
    else:
        with open('data/{}_data.json'.format(name), 'w') as outfile:
            json.dump({'name': name, 'passwd': base64_passwd}, outfile)


    return render_template('signin.html')
    