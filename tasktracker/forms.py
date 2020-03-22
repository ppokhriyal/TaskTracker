from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from tasktracker.models import User

#Login Form
class LoginForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	group = SelectField('Group',choices=[('Linux R&D','Linux R&D'),('OS Development','OS Development'),('OS Testing','OS Testing'),('DS Development','DS Development'),('DS Testing','DS Testing'),('Admin','Admin')])
	submit = SubmitField('Sign In')

#Add Project Manager
class AddProjectManager(FlaskForm):
	username = StringField('Project Manager Name',validators=[DataRequired()])
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	group = SelectField('Group',choices=[('Linux R&D','Linux R&D'),('OS Development','OS Development'),('OS Testing','OS Testing'),('DS Development','DS Development'),('DS Testing','DS Testing')])
	submit = SubmitField('Submit')

	def validate_email(self,email):

		user = User.query.filter_by(email=email.data).first()
		check_email_valid = email.data

		if check_email_valid.split('@')[1] != "vxlsoftware.com":

			raise ValidationError('Please enter your valid vxlsoftware email id.')
			
		if user:
		   raise ValidationError('That email is taken. Please choose a diffrent one.')

#Add Subordinate
class AddSubordinate(FlaskForm):

	username = StringField('Project Manager Name',validators=[DataRequired()])
	email = StringField('Email',validators=[DataRequired(),Email()])
	password = PasswordField('Password',validators=[DataRequired()])
	pmanager = StringField('Project Manager')
	group = SelectField('Group',choices=[('Linux R&D','Linux R&D'),('OS Development','OS Development'),('OS Testing','OS Testing'),('DS Development','DS Development'),('DS Testing','DS Testing')])
	submit = SubmitField('Submit')

	def validate_email(self,email):

		user = User.query.filter_by(email=email.data).first()
		check_email_valid = email.data

		if check_email_valid.split('@')[1] != "vxlsoftware.com":

			raise ValidationError('Please enter your valid vxlsoftware email id.')
			
		if user:
		   raise ValidationError('That email is taken. Please choose a diffrent one.')
