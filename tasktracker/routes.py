from flask import render_template, url_for, flash, redirect, request, abort, session, jsonify
from tasktracker import app,db,bcrypt
from tasktracker.forms import LoginForm,AddProjectManager,AddSubordinate
from tasktracker.models import Pmanager,User
from flask_login import login_user, current_user, logout_user, login_required



#Home Page
@app.route('/home',methods=['GET','POST'])
@login_required
def home():
	pmcount = db.session.query(Pmanager).count()
	subcount = db.session.query(User).count() - 1
	return render_template('home.html',title='TaskTracker : Home',pmcount=pmcount,subcount=subcount)
#Login Page
@app.route('/',methods=['GET','POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password,form.password.data) and user.group == form.group.data:
			login_user(user)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email,password and group','danger')

	return render_template('login.html',title='TaskTracker : Login',form=form)

#Add Project Manager
@app.route('/addpm',methods=['POST','GET'])
@login_required
def addpm():
	form = AddProjectManager()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = Pmanager(pm_name=form.username.data,pm_email=form.email.data, password=hashed_password,password_decrypted=form.password.data,group=form.group.data)
		db.session.add(user)
		db.session.commit()
		flash(f'Created Project Manager Account','success')
		return redirect(url_for('home'))

	return render_template('addpm.html',title="TaskTracker : Add Project Manager",form=form)


#Add Subordinate
@app.route('/addsubordinate',methods=['GET','POST'])
@login_required
def addsub():
	return render_template('addsub.html',title='TaskTracker : Add Subordinate')
#Logout Page
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))