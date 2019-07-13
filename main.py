from flask import Flask, render_template, redirect, request
from validate_email import validate_email

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def base_page():
    return render_template("their.html")

@app.route("/",methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]
    if username == "":
        username_error = "That's not a valid username"
    else:
        username_error = ""
    if password == "":
        password_error = "That's not a valid password"
    else:
        password_error = ""
    if verify == "" or verify != password:
        verify_error = "Passwords don't match"
    else:
        verify_error = ""
    if email != "" and validate_email(email) == False:
        email_error = "That's not a valid email"
    else:
        email_error = ""
    return render_template("their.html",username=username, username_error=username_error,password_error=password_error,verify_error=verify_error,email_error=email_error)

app.run()

