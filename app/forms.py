from flask_wtf import Form
from wtforms import TextField, SubmitField, validators, ValidationError, TextAreaField, BooleanField
from wtforms.validators import DataRequired, InputRequired
 
class ContactForm(Form):
  name = TextField("Your Full Name",  [validators.Required("Please enter your name.")])
  email = TextField("Your E-Mail",  [validators.Required("Please enter your email address."), validators.Email("Please enter a valid email address.")])
  training = BooleanField("Completed CPS Training?", [validators.Required("Please confirm they have completed CPS training")])
  usersname = TextField("Users Full Name", [validators.Required("Please enter the user's full name.")])
  username = TextField("Users Username", [validators.Required("Please enter the user's username.")])
  message = TextAreaField("Addittional Information?")
  submit = SubmitField("Send Request")