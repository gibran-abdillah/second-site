from flask_sqlalchemy import SQLAlchemy
from app import app,login

from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy(app)
class User(db.Model,UserMixin):
    __tablename__ = 'dbusers'

    id = db.Column(db.Integer,nullable=False,primary_key=True)

    username = db.Column(db.String,nullable=False,
                        unique=True,index=False)
    
    email = db.Column(db.String(100),nullable=False,
                      unique=True,index=True)

    password = db.Column(db.String,nullable=False,unique=True)

    nama_lengkap = db.Column(db.String,index=True,nullable=False)
    is_admin = db.Column(db.Boolean,default=False,nullable=False)

    def set_password(self,password):
        self.password = generate_password_hash(password,method='sha512')
    
    def check_password(self,password):
        return check_password_hash(self.password,password)
    
    def __repr__(self):
        return '<username:{}'.format(self.username)

class Blog_Post(db.Model):
    __tablename__ = 'blogs'

    blog_id = db.Column(db.Integer,nullable=False,primary_key=True)

    created_on = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    konten = db.Column(db.Text,nullable=False,
                       index=True,unique=True)

    title_blog = db.Column(db.String,unique=True,nullable=False)


    def __repr__(self):
        return '<title:{}'.format(self.title_blog) 
            

# dont remove this

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# error when there is no user_loader

'''
Exception: Missing user_loader or request_loader. Refer to http://flask-login.readthedocs.io/#how-it-works for more info.
'''
