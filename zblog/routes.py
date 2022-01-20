from flask import render_template
from zblog import app

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/page1') 
def pages():
    return render_template('page1.html')
