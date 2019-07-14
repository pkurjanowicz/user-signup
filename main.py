from flask import Flask, render_template, redirect, request
from validate_email import validate_email

app = Flask(__name__)
app.config["DEBUG"] = True

def check_character_len(string):
    if len(string) > 20 or len(string) < 3:
        return False
    return True

@app.route("/", methods=["GET"])
def base_page():
    return render_template("their.html")

@app.route("/",methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]
    
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    
    if username == "" or check_character_len(username) == False:
        username_error = "That's not a valid username"

    if password == "" or check_character_len(password) == False:
        password_error = "That's not a valid password"

    if verify == "" or verify != password or check_character_len(verify) == False:
        verify_error = "Passwords don't match"

    if email != "" and validate_email(email) == False:
        email_error = "That's not a valid email"

    return render_template("their.html", username=username, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

app.run()

