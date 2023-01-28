from flask import Blueprint, render_template, redirect, url_for, request, flash
from .import db
from models import User
auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    return render_template('login.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password')
        password2 = request.form.get('password2')

       email_exists = User.query.filter_by(email=email)
       username_exists = User.query.filter_by(username=username)
.first()
    if email_exists:
        flash("Email is already in use")

    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('views.home'))

@auth.route