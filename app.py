from flask import Flask, render_template, redirect, url_for, session
import random

app = Flask(__name__)

# Main route
@app.route("/")
def index():
    return render_template("index.html")

# Temperature route
@app.route('/temp')
def temp():
    # Generate junk data
    test = random.randint(0,100)
    return render_template('temp.html', test=test)