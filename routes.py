from app import app
from flask import Flask,render_template,request,redirect,url_for,json,flash
import sarc_detect2
import pandas as pd
from functions import retData,getDataset,GetSarc_count,create_word_cloud
from flask import Flask, render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


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
        data1 = retData(s1)
        c1 = getDataset(s1)
        sar1 = GetSarc_count(s1, 1)
        sar0 = GetSarc_count(s1, 0)
        print("Data is selected",data1)

        sarcastic_word_count=c1[c1['is_sarcastic']==1]['headline'].str.split().map(lambda x: len(x))
        non_sarcastic_word_count=c1[c1['is_sarcastic']==0]['headline'].str.split().map(lambda x: len(x))

        sarc_1 = list(sarcastic_word_count)
        sarc_0 = list(non_sarcastic_word_count)

        fig = px.histogram(c1, x= [sarc_1 + sarc_0],
                    color='is_sarcastic', barmode='group',
                    height=400,width = 800)

        #fig.show()
        fig.write_html('templates\graphchart.html')

        create_word_cloud(c1, 1)
        create_word_cloud(c1, 0)
        # Create a Styler object
        styler = data1.style

        # Apply styles to the Styler object
        styler.set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#f2f2f2'), ('color', '#333')]},
        {'selector': 'td', 'props': [('border', '1px solid #ddd'), ('padding', '8px'), ('text-align', 'left')]},
        {'selector': 'tbody tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
        {'selector': 'tbody tr:hover', 'props': [('background-color', '#ddd')]}
    ])

        # Render the styled table in HTML
        html = styler.render()

        # Pass the HTML to the template
        return render_template('dashboard.html', response1 = s1,data1=html, sarc1=sar1, sarc0=sar0, sard0 = sarc_0,sard1 = sarc_1)
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


@app.route('/graph1',methods=["GET", "POST"])
def graph1():
    print("THE METHOD SELECTED")
    if request.method == 'POST':
        selected_value = request.form['selected_value']
        s1 = selected_value
        # do something with selected_value
        data = getDataset(s1)
        print("Data is selected")
        sarcastic_word_count=df[df['is_sarcastic']==1]['headline'].str.split().map(lambda x: len(x))
        non_sarcastic_word_count=df[df['is_sarcastic']==0]['headline'].str.split().map(lambda x: len(x))

        sarc_1 = list(sarcastic_word_count)
        sarc_0 = list(non_sarcastic_word_count)

        # Render the HTML template with the image URL and counts
        return render_template('charts.html', sard0 = sarc_0,sard1 = sarc_1)
    return render_template('charts.html')