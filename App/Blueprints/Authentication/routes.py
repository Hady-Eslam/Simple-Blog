from flask import render_template, request, url_for, flash, redirect
from flask_login import current_user, login_user, logout_user
from App.Blueprints.Authentication import authentication
from App import bcrypt, db
from .models import User
from .utilits import send_reset_link
from .forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm



@authentication.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created Successfully For {form.username.data}', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


@authentication.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page if next_page else url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@authentication.route('/logout')
def logout():
    logout_user()
    return redirect('login')



@authentication.route('/reset_password', methods=['GET', 'POST'])
def request_reset():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_link(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('authentication.login'))

    return render_template('request_reset.html', title='Reset Password', form=form)


@authentication.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    user = User.varify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('authentication.request_reset'))
    
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('authentication.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
