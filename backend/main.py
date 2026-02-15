from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
Tasks = []
app = Flask(__name__)

# Database file config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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


