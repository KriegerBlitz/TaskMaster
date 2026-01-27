# This is where I will put the code, once I have some.
from flask import Flask  #, render_template, request, redirect

Tasks = []
app = Flask(__name__)


@app.route('/')
def home():
    return '<p>Hello World!</p>'

@app.route('/login')
def login():
    return '<p>Login Page</p>'

@app.route('/newTask')
def newTask():
    return '<p>New Task Page</p>'

@app.route('/register')
def register():
    return '<p>Register Page</p>'

@app.route('/logout')
def logout():
    return '<p>Logout Page</p>'


