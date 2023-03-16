from app import app
from flask import Flask,render_template,request,redirect,url_for
import sarc_detect2

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/sarc_detector')
def sarc_detector():
    return render_template('sarc_detector.html')

@app.route('/predict',methods=["GET", "POST"])
def predict():
    if request.method == "POST":    
        form_data = request.form
        status = predict(form_data["text"])
        return render_template("result.html",result=status, response=status)
    else:
        return render_template("result.html")


@app.route('/result')
def result():
    return render_template('result.html')