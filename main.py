#########################################
#  If you want to use free STMP server  #
#  you can rename free_stmp_config.json #
#  to config.json                       #
#                                       #
# but this server you can send 300 mail #
# per day                               #
#########################################

from flask import Flask, flash, request, redirect, render_template, session, url_for
from werkzeug.utils import secure_filename
from smtplib import SMTP
import os, json, base64, time, smtplib, requests, string, random

if not os.path.exists('data'):
    os.makedirs('data')




app = Flask(__name__)

app.secret_key = os.urandom(24)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'static/uploads')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', value=session['username'], url='/userinfo', color='success', text='Hi, {}'.format(session['username']))
    return render_template('index.html', value='Sign In', url='/signin', color='danger', text="You're not sign in.")


@app.route('/signin')
def signin():
    flash('')
    return render_template('signin.html')


@app.route('/signin', methods=['POST'])
def signin_post():
    name = request.form['name']
    passwd = request.form['passwd']

    passwd_bytes = passwd.encode('utf-8')
    base64_bytes = base64.b64encode(passwd_bytes)
    base64_passwd = base64_bytes.decode('utf-8')
    # os check file
    if os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'r') as f:
            i = json.load(f)

    elif not os.path.exists('data/{}_data.json'.format(name)):
        flash('User Not Found')
        return render_template('signin.html')

    if i["username"] == name and i["passwd"] == base64_passwd:
        session['username'] = i["username"]
        return "<script>window.location.href = '/';</script>"
    else:
        flash('Invalid username or password')
        return render_template('signin.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_post():
    name = request.form['name']
    passwd = request.form['passwd']
    email = request.form['email']
    passwd_bytes = passwd.encode('utf-8')
    base64_bytes = base64.b64encode(passwd_bytes)
    base64_passwd = base64_bytes.decode('utf-8')

    # os search file
    if os.path.exists('data/{}_data.json'.format(name)):
        return 'user already exists <a href="/signup">Sign Up</a>'
    elif not os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'w') as outfile:
            json.dump({'username': name, 'passwd': base64_passwd,
                      'email': email, 'img': 'uploads/{}.jpg'.format(name)}, outfile)

    return "<script>window.location.href = '/signin';</script>"


@app.route('/signout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return "<script>window.location.href = '/';</script>"  # redirect to home page


@app.route('/changepasswd')
def changepasswd():
    if 'username' in session:
        return render_template('changepasswd.html', error='')
    return "You're not logged in"


@app.route('/changepasswd', methods=['POST'])
def changepasswd_post():
    name = session['username']
    new_passwd = request.form['newpasswd']
    passwd = request.form['passwd']
    passwd_bytes = passwd.encode('utf-8')
    base64_bytes = base64.b64encode(passwd_bytes)
    base64_passwd = base64_bytes.decode('utf-8')

    # import json file
    with open('data/{}_data.json'.format(name), 'r') as f:
        i = json.load(f)

    if base64_passwd == i["passwd"]:
        new_passwd_bytes = new_passwd.encode('utf-8')
        new_base64_bytes = base64.b64encode(new_passwd_bytes)
        new_base64_passwd = new_base64_bytes.decode('utf-8')
        with open('data/{}_data.json'.format(name), 'w') as outfile:
            json.dump({'username': name, 'passwd': new_base64_passwd,
                      'email': i['email'], 'img': 'uploads/{}.jpg'.format(name)}, outfile)

        return "<script>window.location.href = '/userinfo';</script>"
    else:
        return render_template('changepasswd.html', error='Wrong Password')


@app.route('/userinfo/')
def userinfo():
    name = session['username']
    if 'username' in session:
        if os.path.exists('data/{}_data.json'.format(name)):
            with open('data/{}_data.json'.format(name), 'r') as f:
                i = json.load(f)

        elif not os.path.exists('data/{}_data.json'.format(name)):
            return 'user not found'
        return render_template('userinfo.html', name=name, img=i["img"], email=i["email"])
    return "You're not logged in"


@app.route('/userinfo/upload/')
def upload_form():
    name = session['username']
    if 'username' in session:
        return render_template('upload.html', name=name)
    return "You're not logged in"


@app.route('/userinfo/upload/', methods=['POST'])
def upload_file():
    name = session['username']
    # check if the post request has the file part
    file = request.files['file']
    if file.filename == '':
        flash('No file selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # os rename file
        os.rename(os.path.join(app.config['UPLOAD_FOLDER'], filename), os.path.join(
            app.config['UPLOAD_FOLDER'], '{}.jpg'.format(name)))
        return redirect('/userinfo/')
    else:
        return redirect(request.url)


@app.route('/delete')
def delete():
    if 'username' in session:
        name = session['username']
        if os.path.exists('data/{}_data.json'.format(name)):
            if os.path.exists('static/uploads/{}.jpg'.format(name)):
                os.remove('static/uploads/{}.jpg'.format(name))
            os.remove('data/{}_data.json'.format(name))
            session.pop('username', None)
            return "<script>window.location.href = '/';</script>"

    return "You're not logged in"

#user RESTAPI
@app.route('/api/users/<name>')
def api(name):
    if os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'r') as f:
            i = json.load(f)

    return json.dumps({'username': i["username"], 'email': i["email"]})

@app.route('/forget')
def forget():
    return render_template('forget.html', error='')


@app.route('/forget', methods=['POST'])
def forget_post():
    name = request.form['name']
    if os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'r') as f:
            i = json.load(f)
        return render_template('confirm_forget.html', name=name, email=i["email"])
    elif not os.path.exists('data/{}_data.json'.format(name)):
        return render_template('forget.html', error="user not found")


@app.route('/forget/send/<name>')
def forget_send(name):
    if os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'r') as f:
            i = json.load(f)
        
        #open config.json file
        with open('config.json', 'r') as f:
            config = json.load(f)
        passwd = base64.b64decode(i["passwd"])
        passwd = passwd.decode('utf-8')
        receiver = i["email"]

        smtp = SMTP()
        smtp.set_debuglevel(0)
        smtp.connect(config['stmp_host'], int(config['stmp_port']))
        smtp.login(config['stmp_auth'], config['stmp_pass'])

        message_text = "FJSL Password Forgot \n\nHi! {}\nthis is a mail from Flask JSON Login\nYour password is {}\n".format(name,passwd)

        msg = "From: FJSL <{}>\nTo: meck22772@gmail.com\nSubject: {}\n".format(config['stmp_sender'],message_text)


        smtp.sendmail(config['stmp_sender'], receiver, msg)
        smtp.quit()
        return redirect('/')

@app.route('/config')
def config():
    return render_template('config.html')    

@app.route('/config', methods=['POST'])
def config_post():
    host = request.form['host']
    port = request.form['port']
    sender = request.form['sender']
    auth = request.form['auth']
    passwd = request.form['passwd']
    sender = request.form['sender']
    with open('config.json', 'w') as f:
        json.dump({"stmp_host": host, "stmp_port": port, "stmp_auth": auth, "stmp_pass": passwd, "stmp_sender": sender}, f)
    return "<script>window.location.href = '/';</script>"  # redirect to home page

"""
#sign up RESTAPI
@app.route('/api/signup/<username>&<email>&<password>')
def api_signin(username, email, password):
    if os.path.exists('data/{}_data.json'.format(username)):
        return 'user already exists'
    else:
        password_bytes = password.encode('utf-8')
        base64_bytes = base64.b64encode(password_bytes)
        base64_passwd = base64_bytes.decode('utf-8')
        with open('data/{}_data.json'.format(username), 'w') as outfile:
            json.dump({'username': username, 'passwd': base64_passwd,
                      'email': email, 'img': 'uploads/{}.jpg'.format(username)}, outfile)
        return 'user created'
"""
