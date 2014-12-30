# -*- coding: utf-8 -*-

import os
import random

from app import app, envs
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
