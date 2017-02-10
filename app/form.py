from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TextField
from wtforms.validators import DataRequired, Email

class ContactForm():
	name = TextField('name', validators= [DataRequired("Please enter your full name")])
	email = TextField('email', validators= [DataRequired("Please enter your e-mail address"), Email("Please enter your e-mail address")])
	subject = TextField('subject', validators= [DataRequired("Please enter the subject for your message")])
	msg = TextAreaField('message', validators= [DataRequired("Please enter the message you would like to send")])
	send = SubmitField("Send_e-mail")
            
            