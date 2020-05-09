''' I have also added the Mysql database 
also but we can also complete the task without it also.'''
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
local_server=True
with open('config.json','r') as c:
    params = json.load(c)["params1"]
app =Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT ='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params["user_name"],
    MAIL_PASSWORD=params["password"]
)
mail=Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = params["local_url"]
db = SQLAlchemy(app)
class contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone_no = db.Column(db.String(20),nullable=False )
    password = db.Column(db.String(180),nullable=False)
@app.route("/signup",methods=['GET','POST'])
def contact1():
    if(request.method=="POST"):
        name=request.form.get("name")
        email=request.form.get("emailid") 
        phone_no=request.form.get("phone_no")
        password=request.form.get("password")
        mail.send_message("New user "+name+" joined",
                             sender=email,
                             recipients=[params['user_name']],
                             body ="Sender's Name: "+name+'\n'+"Sender's Email: "+ email+'\n'+"Contact Number:"  +phone_no)
        return render_template("confirmation.html",params=params)
    return render_template("signup.html",params=params)
app.run(debug=True)
