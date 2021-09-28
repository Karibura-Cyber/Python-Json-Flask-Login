from flask import Flask, flash, request, redirect, render_template, session, url_for
from werkzeug.utils import secure_filename
import os
import os
import json
import base64
import time
import smtplib

if not os.path.exists('data'):
    os.makedirs('data')


app=Flask(__name__)

app.secret_key = b'!\xd3\xca-\xc2\xf1\xe6O\xbb#&>\xc5\x98$\xd2'
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
    
    passwd_bytes = passwd.encode('ascii')
    base64_bytes = base64.b64encode(passwd_bytes)
    base64_passwd = base64_bytes.decode('ascii')
    #os check file
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
    passwd_bytes = passwd.encode('ascii')
    base64_bytes = base64.b64encode(passwd_bytes)
    base64_passwd = base64_bytes.decode('ascii')


    #os search file
    if os.path.exists('data/{}_data.json'.format(name)):
        return 'user already exists <a href="/signup">Sign Up</a>'
    elif not os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'w') as outfile:
            json.dump({'username': name, 'passwd': base64_passwd, 'email': email, 'img': 'uploads/{}.jpg'.format(name)}, outfile)

       
       
    return  "<script>window.location.href = '/signin';</script>"

@app.route('/signout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return "<script>window.location.href = '/';</script>" #redirect to home page

@app.route('/changepasswd')
def changepasswd():
    if 'username' in session:
        return render_template('changepasswd.html')
    return "You're not logged in"

@app.route('/changepasswd', methods=['POST'])
def changepasswd_post():
    name = session['username']
    new_passwd = request.form['newpasswd']
    passwd=request.form['passwd']
    email = request.form['email']
    passwd_bytes = passwd.encode('ascii')
    base64_bytes = base64.b64encode(passwd_bytes)
    base64_passwd = base64_bytes.decode('ascii')
    
    #import json file
    with open('data/{}_data.json'.format(name), 'r') as f:
        i = json.load(f)
    
    if base64_passwd == i["passwd"]:
        new_passwd_bytes = new_passwd.encode('ascii')
        new_base64_bytes = base64.b64encode(new_passwd_bytes)
        new_base64_passwd = new_base64_bytes.decode('ascii')
        with open('data/{}_data.json'.format(name), 'w') as outfile:
            json.dump({'username': name, 'passwd': new_base64_passwd, 'email': email, 'img': 'uploads/{}.jpg'.format(name)}, outfile)
        
        return "<script>window.location.href = '/';</script>"
    

   

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
        flash('File successfully uploaded')
        #os rename file
        os.rename(os.path.join(app.config['UPLOAD_FOLDER'], filename), os.path.join(app.config['UPLOAD_FOLDER'], '{}.jpg'.format(name)))
        return redirect('/userinfo/')
    else:
        flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/delete')
def delete():
    if 'username' in session:
        name = session['username']
        if os.path.exists('data/{}_data.json'.format(name)):
            os.remove('data/{}_data.json'.format(name))
            session.pop('username', None)
            return "<script>window.location.href = '/';</script>"
            

    return "You're not logged in"

@app.route('/api/<name>')
def api(name):
    if os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'r') as f:
            i = json.load(f)
    
    return json.dumps({'username': i["username"], 'email': i["email"]})

@app.route('/forget')
def forget():
    return render_template('forget.html')

@app.route('/forget', methods=['POST'])
def forget_post():
    name = request.form['name']
    if os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'r') as f:
            i = json.load(f)
        return render_template('confirm_forget.html', name=name, email=i["email"])
    elif not os.path.exists('data/{}_data.json'.format(name)):
        return 'user not found <a href="/signup">Sign Up</a>'

@app.route('/forget/send/<name>')
def forget_send(name):
    if os.path.exists('data/{}_data.json'.format(name)):
        with open('data/{}_data.json'.format(name), 'r') as f:
            i = json.load(f)

        gmail_user = 'kariburahack@gmail.com' #replace your Gmail Here [Gmail Only for now]
        gmail_password = 'meck1201'
        reciever = i["email"]
        passwd = base64.b64decode(i["passwd"])
        sent_from = gmail_user
        to = ['{}'.format(reciever)]
        subject = 'Python Flask JSON Login system forget your password'
        body = "Hey, what's up?\n\n this email send from Python Flask JSON Login system \n\n this is your password: {} \n\n This method is beta".format(passwd)

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
        except:
            print('Something went wrong...')
        return redirect('/')

    #check file 
    
    
if __name__ == '__main__':
    app.run(debug=False)
