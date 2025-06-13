from flask import flask, render_template

app = flask(__name__)

app.route('/')
def index():
    return render_template("index.html")

app.route('/login')
def index():
    return render_template("login.html")

app.route('/register')
def index():
    return render_template("register.html")