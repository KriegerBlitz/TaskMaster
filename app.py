# This is where I will put the code, once I have some.
from flask import Flask  #, render_template, request, redirect

Tasks = []
app = Flask(__name__)


@app.route('/')
def home():
    return '<p>Hello World!</p>'


@app.route('login')
def login():
    return
