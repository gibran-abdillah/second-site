from app import app 
import os 
from flask import render_template
from views.authentication import *  # tempat crud login
from seed_data import seed_data

# disini kita import route url dari dir views

@app.route('/')
def index_page():
    seed_data()
    blog = Blog_Post.query.all() # get data blog 
    print(blog)
    return render_template('index.html',blogs=enumerate(blog,1)) # 1 itu start nya 


@app.route('/detail-blog/<int:id>')
def show_detail(id):
    print(id)
    return Blog_Post.query.filter_by(blog_id=id).first().konten # show blog from request id 


