from app import app
from flask import Flask,render_template,request

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
