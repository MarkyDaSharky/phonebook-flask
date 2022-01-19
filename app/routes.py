from app import app
from flask import render_template, redirect, url_for
from app.forms import RegisterForm



@app.route('/')
def index():
    my_name = 'Mark'
    my_city = 'Houston'
    my_state = 'Texas'
    return render_template('index.html', name=my_name, city=my_city, state=my_state)




@app.route('/register', methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        address = form.address.data
        print(name, phone, address)
        return redirect(url_for('index'))
    return render_template('register.html', form = form)