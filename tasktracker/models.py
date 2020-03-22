from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from tasktracker import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))


class Pmanager(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	pm_name = db.Column(db.String(20),unique=True,nullable=False)
	pm_email = db.Column(db.String(120),unique=True,nullable=False)
	password = db.Column(db.String(60),nullable=False)
	password_decrypted = db.Column(db.String(60),nullable=False)
	group = db.Column(db.String(60),nullable=False)
	user = db.relationship('User',backref='project_manager',lazy=True)

class User(db.Model,UserMixin):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(20),unique=True,nullable=False)
	email = db.Column(db.String(120),unique=True,nullable=False)
	password = db.Column(db.String(60),nullable=False)
	password_decrypted = db.Column(db.String(60),nullable=False)
	group = db.Column(db.String(60),nullable=False)
	pmanager_id = db.Column(db.Integer,db.ForeignKey('pmanager.id'))

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.group}')"