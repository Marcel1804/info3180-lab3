from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired

WTF_CSRF_SECRET_KEY='TET342525WL=2]42P[21K,10``L2@#@@$1~2`3]'
class myForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()]);
    email=StringField('Email',validators=[DataRequired()]);
    subject=StringField('Subject',validators=[DataRequired()]);
    msg=TextAreaField('Message',validators=[DataRequired()]);


                                                                    
                                                                    