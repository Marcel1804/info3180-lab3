from flask_wtf import FlaskForm
from wtforms import Form, Stringfield, TextAreaField
from wtforms.validators import DataRequired

WTF_CSRF_SECRET_KEY='TET342525WL=2]42P[21K,10``L2@#@@$1~2`3]'
class MyForm(FlassForm):
    name= Stringfield('name',validators=[DataRequired]());
    email_address=Stringfield('email',validators=[DataRequired()]);
    subject=Stringfield('subject',validators=[DataRequired()]);
    msg=TextAreaField('msg',validators[DataRequired()]);


                                                                    