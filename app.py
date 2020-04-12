#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 02:22:04 2020

@author: rajan
"""
import os
from flask import Flask, request, render_template, url_for, redirect
from datetime import date

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('index.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':  
           # os.makedirs(d1)
            photo.save(os.path.join('/home/rajan/Documents/style-transfer/style-images', photo.filename))
    return render_template('Select_background.html')

@app.route("/handlestyle", methonds=["POST"])
def handlestyle():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':  
           # os.makedirs(d1)
            photo.save(os.path.join('/home/rajan/Documents/style-transfer/style-images', photo.filename))
    return render_template('Select_background.html')

if __name__ == "__main__":
    app.run()