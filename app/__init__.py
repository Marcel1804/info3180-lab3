from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY']='24y3hdw54tas002-o24rjq42-0'
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT']='465'
app.config['MAIL_USERNAME']='username'
app.config['MAIL_PASSWORD']='password'

mail= Mail(app)
from app import views