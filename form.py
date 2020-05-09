from flask import Flask,render_template,request
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
@app.route("/contact",methods=['GET','POST'])
def contact1():
    if(request.method=="POST"):
        name=request.form.get("name")
        email=request.form.get("emailid") 
        phone_no=request.form.get("phone_no")
        message=request.form.get("message")
        mail.send_message("New message from "+name,
                             sender=email,
                             recipients=[params['user_name']],
                             body ="Sender's Name: "+name+'\n'+"Sender's Email: "+ email+'\n'+"Contact Number:"  +phone_no+'\n'+message)
        return render_template("confirmation.html",params=params)
    return render_template("contact.html",params=params)
app.run(debug=True)
