from flask import Flask
from flask_mail import mailbox


app = Flask(__name__)
app.config['SECRET_KEY']='24y3hdw54tas002-o24rjq42-0'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT']='465'
app.config['MAIL_USERNAME']='ab1c250737434c'
app.config['MAIL_PASSWORD']='464c0cc6c462e'

mail= Mail(app)
from app import views