from app import app
from flask import Flask,render_template,request,redirect,url_for,json
import sarc_detect2

@app.route("/")
def index():
    return render_template('index.html')

#Included in dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/my-endpoint', methods=["GET","POST"])
def my_endpoint():
    if request.method == 'POST':
        selected_value = request.form['selected_value']
        s1 = selected_value
        # do something with selected_value
        print("selected value is ",selected_value)
        return render_template('dashboard.html', response1 = s1)
    return render_template('dashboard.html')

#Included in sarc detector
@app.route('/sarc_detector')
def sarc_detector():
    return render_template('sarc_detector.html')

@app.route('/result',methods=["GET", "POST"])
def prediction():
    if request.method == "POST":    
        form_data = request.form
        status = sarc_detect2.predict(form_data["text"]) 
        return render_template("result.html",result=status, response=status)
    else:
        return render_template("sarc_detector.html")


# @app.route('/result')
# def result():
#     return render_template('result.html')