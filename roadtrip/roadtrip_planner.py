from flask import Flask, request
from roadtrip.database import *

app = Flask(__name__)

@app.route("/")
def homepage():
    file = codecs.open("home.html", "r", "utf-8")
    return file.read()

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if check_credential(username, password):
        return user_info(username)
    else:
        file = codecs.open("wrong credential.html", "r", "utf-8")
        return file.read()

@app.route("/register")
def register():
    file = codecs.open("register.html", "r", "utf-8")
    return file.read()

@app.route("/after_register", methods=["POST"])
def after_register():
    username = request.form["username"]
    password = request.form["password"]
    if add_user(username, password):
        return "<h1>registered successfully</h1><form action='/'><button type='submit'>login</button></form>"
    else:
        return "<h1>username already in use</h1><form action='/register'><button type='submit'>try another username</button></form>"

@app.route("/plan", methods=["POST"])
def plan():
    user = request.form["username"]
    fstreet = request.form["fstreet"]
    fcity = request.form["fcity"]
    fstate = request.form["fstate"]
    dstreet = request.form["dstreet"]
    dcity = request.form["dcity"]
    dstate = request.form["dstate"]
    return user_plan(user, fstreet, fcity, fstate, dstreet, dcity, dstate)

@app.route("/replan")
def replan():
    file = codecs.open("plan.html", "r", "utf-8")
    return file.read()

if __name__ == "__main__":
    app.run()