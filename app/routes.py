#Imports all the necessary modules from the Flask framework, including mail modules
from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail

#Write the mail element to the mail variable
mail = Mail()

#Write the flask name to the app variable
app = Flask(__name__)

#Secret key for app access (not currently needed in development mode)
app.secret_key = 'Go0Gl3524'

#Configure the Google mail client (ideally for The BBC, this should be outlook, yet this should be accepted by Fireewall rules and outlook rules)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'authorisationrequest@gmail.com'
app.config["MAIL_PASSWORD"] = 'digital.247operations'

mail.init_app(app)

#Configure the default homepage to home.html
@app.route('/')
def home():
  return render_template('home.html')

#Configure a root to the about page
@app.route('/about')
def about():
  return render_template('about.html')

#Configure a root to the contact page. Pass in GET and POST functionality to this page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

#If the user clicks the submit button on the form
  if request.method == 'POST': 
  	#If the form has not had all their fields entered correctly e.g. missing a username
    if form.validate() == False:
      #Flash an error message reinforcing the fact that all fields are required
      flash('All fields are required.')
      #Pull these error messages from the contact.html page, which will then pull this from the forms.py
      return render_template('contact.html', form=form)
      #Otherwise
    else:
      #Execute order 66, I'm joking, submit the request and send the e-mail with the following crednetials
      msg = Message(subject='CPS Access Request', sender='authorisationrequest@gmail.com', recipients=['bfyffe1993@gmail.com', form.email.data])
      #Declare the message body here. This uses three sets of quotations to give multiple lines of e-mail content. The %s calls each value from the contact.html page using flask and prints them in the order specified below in brackets.
      msg.html = """\
	<html>
 	 <head></head>
  		<body>
    	<h2>You Have A New CPS Request</h2>
    	Hi 24/7, please action the following request for CPS access.<br>
      ------------------------------------------------------------<br>
      The Users name: %s<br>
      The Username: %s<br>
      Request From: %s <br>
      Email: %s<br>
       		How are you?<br>
       		Have an issue with this request? Send us an e-mail on: <a href="http://www.python.org">link</a> you wanted. %s
   		 </p>
  		</body>
		</html>
		
      """ % (form.usersname.data, form.username.data, form.name.data, form.email.data, form.message.data)
      #Pass in the msg value and send it off
      mail.send(msg)


      #Return the values from contact.html and verify this process has been completed.
      return render_template('contact.html', success=True, usersname=form.usersname.data, username=form.username.data, name=form.name.data, email=form.email.data, message=form.message.data)
  #ElseIf this has worked
  elif request.method == 'GET':
  	#Return the contact.html page for the user to see their confirmation page
    return render_template('contact.html', form=form)
#Run a debugger to see error messages
if __name__ == '__main__':
  app.run(debug=True)