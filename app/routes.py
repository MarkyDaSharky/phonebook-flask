from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.forms import RegisterForm, ContactForm, LoginForm
from app.models import User, Contact

#flask migrate video at 1:36:08

@app.route('/')
def index():
    my_name = 'Mark'
    my_city = 'Houston'
    my_state = 'Texas'
    contacts= Contact.query.all()
    return render_template('index.html', name=my_name, city=my_city, state=my_state, contacts=contacts)



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
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        #Get the data from the Contact form
        name = form.name.data
        phone = form.phone.data
        address = form.address.data
        print(name, phone, address)


        #create new instance of contact into db using form data
        Contact(name=name, phone=phone, address=address)

        return redirect(url_for('index'))
    return render_template('contact.html', form = form)



@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        # Grab the data from the form
        username = form.username.data
        password = form.password.data
       
        # Query user table for user with username
        user = User.query.filter_by(username=username).first()
        
        # if the user does not exist or the user has an incorrect password
        if not user or not user.check_password(password):
            # redirect to login page
            print('That username and password is incorrect')
            return redirect(url_for('login'))
        
        # if user does exist and correct password, log user in
        login_user(user)
        print('User has been logged in')
        return redirect(url_for('index'))

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))