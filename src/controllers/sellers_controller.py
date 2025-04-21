from flask import render_template, request,redirect, url_for, flash, session
from . import auth_bp
from src.data.models.seller import create_user, find_user_by_email, check_password_hash



@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if find_user_by_email(email):
            flash('Email already registered')
            return redirect(url_for('user_controller.register'))

        create_user(username, password, email)
        flash("Registration done successfully. Please login to continue.")
        return redirect(url_for('user_controller.login'))
    return render_template("register.html")


@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = find_user_by_email(email)

        if user and check_password_hash(user.password, password):
            session["user_id"] = str(user.id)
            session["username"] = user["username"]
            flash("Login successfully")
        else:
            flash("Invalid email or password")
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Logout successfully")
    return redirect(url_for('user_controller.login'))