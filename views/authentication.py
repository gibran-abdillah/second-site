from modules.models import * 
from app import app 
from flask import render_template,request,redirect,flash,url_for
from flask_login import login_user,current_user,logout_user,login_required
from views.forms import * 
from sqlalchemy import or_
from .dashboard.controllers import * 


'''

contain about login user and resetpassword

'''

@app.route('/login',methods=["POST","GET"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_admin'))
    form = Login_Form()
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                user_name = form.username.data # get username from input
                pass_word = form.password.data # get password from password input 

                check_user = User.query.filter(or_(User.username == user_name,User.email == user_name)).first()
                if check_user and check_user.check_password(form.password.data):
                    login_user(check_user) # creating session 
                    return redirect(url_for('dashboard_admin')) # redirect to dashboard function if login success
                else:
                    flash('error username or password') # show error 
            except KeyboardInterrupt as e:
                print(e)
        else:
            if 'csrf_token' in form.errors:
                print(form.errors)
                flash('invalid token, please refresh your browser')

            
    return render_template('login.html',form=form)


@app.route('/resetpassword',methods=['POST','GET'])
def reset_password():
    form = Reset_Password()
    if form.validate_on_submit():
        check_exist = User.query.filter_by(email=form.email.data).first() # check email is exists
        if check_exist: 
            flash('OTP has been sent')
        else:
            flash('Email Not Found')
    else:
        print(form.errors)
    return render_template('resetpassword.html',form=form)

