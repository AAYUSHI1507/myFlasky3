from app import app
from flask import Flask,render_template,request,redirect,url_for

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/sarc_detector')
def sarc_detector():
    return render_template('sarc_detector.html')

@app.route('/result')
def result():
    return render_template('result.html')