from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe
from datetime import datetime
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route("/")
def index_page():
    return render_template("login.html")

@app.route("/register_form", methods=["POST"])
def register_form():
    data = {
                "first_name": request.form["first_name"],
                "last_name": request.form["last_name"],
                "email": request.form["email"],
                "password1": request.form["password1"],
                "password2": request.form["password2"],
            }
    if not user.User.validate_user_register_form(data):
        return redirect("/")

    pw_hash = bcrypt.generate_password_hash(request.form['password1'])
    data["password"] = pw_hash
    
    this_user_id = user.User.save_user(data)
    session["user_id"] = this_user_id
    session["email"] = request.form["email"]
    session["first_name"] = request.form["first_name"]
    return redirect("/recipes")

@app.route("/login")
def login_page():
    return redirect("/recipes")

@app.route("/login_form", methods=["POST"])
def login_form():
    data = {
                "email": request.form["email"],
                "password3": request.form["password3"]
            }
    
    if not user.User.validate_user_login_form(data):
        return redirect("/")
    
    this_user = user.User.get_user_by_email(data)
    if this_user:
        if bcrypt.check_password_hash(this_user["password"], request.form["password3"]):
            session["user_id"] = this_user["id"]
            session["first_name"] = this_user["first_name"]
            session["email"] = this_user["email"]
            return redirect(f'/recipes')
    flash("Invalid credentials. Please try again.", "login")
    return redirect("/")
        
    # Comment out below to test out hash validation.
    # this_user = user.User.get_user_by_email(data)
    # print("print this user:", this_user)
    
    # session["first_name"] = this_user["first_name"]
    # session["email"] = this_user["email"]
    # return redirect(f'/recipes')

@app.route("/logout")
def logout_page():
    session.clear()
    return redirect("/")