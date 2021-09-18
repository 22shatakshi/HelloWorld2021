from flask import Flask, render_template, request

import templates

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('homepage.html')

@app.route("/print_input", methods = ['POST'])
def print_input():
    str_input = request.form['textInput']
    return "<h1>" + str_input + "</h1>"


