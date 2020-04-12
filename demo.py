#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:23:40 2020

@author: rajan
"""

#~movie-bag/app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {'hello': 'world'}


app.run()