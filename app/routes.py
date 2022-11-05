from flask import render_template, redirect, url_for, request
from app import app

#@app.route('/')
@app.route('/index', methods =['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.form)

    
    return render_template('index.html', title='Home')
