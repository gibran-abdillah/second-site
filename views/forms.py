from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,validators,SubmitField,TextAreaField



class Login_Form(FlaskForm):
    username = StringField('Username',[validators.Length(min=5,max=100,message='Username must be between 5 to 100 character'),
                                       validators.DataRequired('Enter username')])
    
    password = PasswordField('Password',[validators.DataRequired('Enter Your password')])
    submit = SubmitField('Login')

class Reset_Password(FlaskForm):
    email = StringField('Email',[validators.DataRequired('Enter your email')])

    submit = SubmitField('reset')

class Add_Blog(FlaskForm):
    
    judul = StringField('Title',[validators.DataRequired('Enter title blog')])
    isi = TextAreaField('Content')
    submit = SubmitField('Submit')




