# Flask-JSON-Login | Last Update <code>2 Oct 2021</code>


<h2>English</h2>
<h3>This project is an implementation of Flask, one of Python's web libraries and JSON.</h3>
<hr><br>
<h2>ภาษาไทย</h2>
<h3>โปรเจคนี้คือการนำ Flask ที่เป็นหนึ่งใน Web Library ของ Python มาประยุกต์ใช้กับ JSON โดยได้ใช้ JSON ในการเป็นตัวที่ใช้เก็บข้อมูล</h3><hr><br><br>
<h2>How to use<h2><br>


  <h2>CMD</h2>
  
```
set FLASK_APP=main.py
```
```
flask run
```

  <h2> Powershell</h2>
  
```
$env:FLASK_APP = "main"
```
```
flask run
```

  <h2> Linux </h2>
  
```
sudo apt-get install python3-flask -y
```
```
sudo ufw allow 5000
```
```
export FLASK_APP=main.py
```
```
flask run
```
  
  
<h2>Requirement</h2><br>

```
pip install Flask
```

 <br>
<h2>Updating Log</h2>
  
* 5 Aug 2021
  * Signup page
  * Signin page
  * JSON
* 6 Aug 2021
  * Profile Info Page
  * REST API
    * username
* 8 Aug 2021
  * Profile Picture Upload Page 
* 11 Aug 2021
  * Forget password send password to gmail
* 27 Sep 2021
  * Session system
  * Change Password
  * Sign Out
  * Fix Profile Logo not load
* 2 Oct 2021
  * STMP Config
  
  <br>
<h2>Picture</h2><hr>
  <code>Home Page (Not Logged in)</code><br>
  <img src="https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/243182655_272614758070075_5118033769358615999_n.png?_nc_cat=106&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeHTKTs-Z-bvw9LVDhWkQhB83TZ850emH7HdNnznR6YfscAZRWHk2a9UJW0Wrd2sQgzCe8orkNWcdMUpoRHjXpHe&_nc_ohc=yAMsjBOE26AAX-GZF_R&_nc_ht=scontent.fbkk6-2.fna&oh=8b776961f334043cb763b4b7630b438e&oe=6176FFC6"><br>
  
  <code>Home Page (Logged in)</code><br>
  <img src="https://scontent.fbkk6-1.fna.fbcdn.net/v/t1.15752-9/243209859_1229615750888544_307089034347143859_n.png?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeFRq_jilDUC6NwBXD8ebzQJH5kEXYJpJTIfmQRdgmklMpRbib8ojK8Ha9cIUfZF1M971MzqmSPv-_Hs7Bibks1m&_nc_ohc=SFiCy1QPA9EAX97-7kg&_nc_ht=scontent.fbkk6-1.fna&oh=6f106b235c41fdac120612aac22812c3&oe=61787B05"><br>
  
  <code>Sign In</code><br>
  <img src="https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/243276975_560258678580765_2084574841917350539_n.png?_nc_cat=104&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeFvFxBb3guB9nGgoCsFGCW38NDal9DUuM7w0NqX0NS4zpugza_nXjojqTEwYyBfdPU13-7MTtl42Qtu5C6WxCN0&_nc_ohc=WdpdD_kALtwAX_gOQ98&_nc_ht=scontent.fbkk6-2.fna&oh=9c0c53ba92b6b58a4d6162b6c95cad4f&oe=6178BDA7"><br>
  
  <code>Sign Up</code><br>
  <img src="https://scontent.fbkk6-1.fna.fbcdn.net/v/t1.15752-9/243260584_289303049696321_1617608709200188255_n.png?_nc_cat=110&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeEQJugadvLSfkOYb5QmiED7qi7G2DCHjmCqLsbYMIeOYDo6UMi1ywCNzFv8yMpfZlO7yK_hRUWiR5cg6EqcKkJD&_nc_ohc=Fu3vy-JTE6QAX_0hFiW&_nc_ht=scontent.fbkk6-1.fna&oh=ec5c3fb2e2ad0cfd6ced641f2e1f22de&oe=6178AFF0"><br>
  
  <code>Forget Password</code><br>
  <img src="https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/243377874_556582338755639_4352061999172724811_n.png?_nc_cat=103&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeF2I7wvSNgwBoENFQDxu-lGBYMOvdgMMLgFgw692AwwuK34MY9F3T6n-YavRCL-0qMpP3VWxijGnZOic32J_PPi&_nc_ohc=3NAtonr1NzQAX_d6Rzf&tn=6hU7arYck_OOlEOT&_nc_ht=scontent.fbkk6-2.fna&oh=8bd652e644aa2bcc738cd498dc5f4e9b&oe=61778BA6"><br>
  <br>
  
  <code>Profile Page</code><br>
  <img src="https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/243445313_253189863358585_7339625176840068129_n.png?_nc_cat=109&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeHoRRg1WOHROvozFa6yrxDQ_-PO743QWmT_487vjdBaZJfzsd9AC-mPsJpdYwQhU7RoUCa21wNDnVNlsjNwqX5V&_nc_ohc=FA2YJxEPuQ4AX_ySAGM&tn=6hU7arYck_OOlEOT&_nc_ht=scontent.fbkk6-2.fna&oh=2caa3b7d23d31cf6d328f7eb47885da3&oe=6177E854"><br>
  
  <code>Change Password Page</code><br>
  <img src="https://scontent.fbkk6-2.fna.fbcdn.net/v/t1.15752-9/243269179_1061866811251365_6025750414967860363_n.png?_nc_cat=109&ccb=1-5&_nc_sid=ae9488&_nc_eui2=AeH-HKbbx5ETS77PY8KjwmXcfyo-vx5T6xl_Kj6_HlPrGWjprpcH40fJkn8DxQvRWmbJGCLDmc3xR0YmEVRhl-hP&_nc_ohc=Nhzu2DfqE8wAX8NRzx1&tn=6hU7arYck_OOlEOT&_nc_ht=scontent.fbkk6-2.fna&oh=5ff110bd3d9b031a9591581260212593&oe=61757831"><br>

  <code>STMP Config</code>
  <img src="https://scontent.fbkk6-1.fna.fbcdn.net/v/t39.30808-6/243867061_2743459319289883_2324431750249832497_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeHzc253JFgeot5wsYhHRK78WF8OCFvBlIRYXw4IW8GUhFEz9sSINK_RFy7-ckL4JIEEQdPClfucxAwSqSvMR7-D&_nc_ohc=KnGeBF48UQ8AX9DmEK5&_nc_ht=scontent.fbkk6-1.fna&oh=f1177f94fc00fdf2fea3566e0e2df721&oe=615DCDC2"><br>
  
  <hr><br>
<h3 align="center">Development By <a href="https://github.com/Karibura-Cyber">Karibura (Meck)</a></h3>
  <h3 align="center">Powered By <a href="https://getbootstrap.com">Bootstrap</a>, <a href="https://flask.palletsprojects.com/en/2.0.x/">Flask</a></h3>
