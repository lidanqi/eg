# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 12:21:31 2018

@author: lev
"""

# test
from flask import Flask,render_template,request

app = Flask(__name__)

def convert_BBG_CUSIP(input_str):
    return input_str.upper()

@app.route('/', methods = ['GET','POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        try: 
            url = request.form['url']
            r = str(url)
        except:
            errors.append("hey waht?")
            return render_template('index.html', errors=errors)
        if r!="":
            # test func
            strs_input = r.split(",")
            strs_output = [convert_BBG_CUSIP(x.strip()) for x in strs_input if x.strip()!=""]
            results = sorted(zip(strs_input, strs_output))
    return render_template('index.html', errors=errors, results=results)

            
    return render_template('index.html')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run()