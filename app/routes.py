from app import app
from flask import render_template, redirect, url_for
from app.forms import RegisterForm
from models import User, Contact



@app.route('/')
def index():
    my_name = 'Mark'
    my_city = 'Houston'
    my_state = 'Texas'
    return render_template('index.html', name=my_name, city=my_city, state=my_state)



@app.route('/register', methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #Get the data from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        #check if either the username or the email is already in db
        user_exists = User.query.filter((User.username == username)|(User.email == email)).all()

        #if it is inside the database redirect to register
        if user_exists:
            return redirect(url_for('register'))

        #Create a new user instance using form data
        User(username=username, email=email, password=password)

        return redirect(url_for('index'))
    return render_template('register.html', form=form)




@app.route('/contact', methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        address = form.address.data
        print(name, phone, address)
        return redirect(url_for('index'))
    return render_template('contact.html', form = form)