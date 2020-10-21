from app import app
from flask import render_template,redirect,url_for
from flask_login import login_required
from views.forms import * 
from views.authentication import *


@app.route('/dashboard')
@login_required

def dashboard_admin():
    return render_template('dashboard/index.html')

@app.route('/dashboard/add-blog',methods=['POST','GET'])
@login_required
def add_blog():
    form = Add_Blog()
    if form.validate_on_submit():
        title = form.judul.data
        body = form.isi.data 
        Blog = Blog_Post()
        Blog.title_blog = title 
        Blog.konten = body 
        db.session.add(Blog)
        db.session.commit()
    return render_template('dashboard/add-blog.html',form=form)

@app.route('/dashboard/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))

