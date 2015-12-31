# -*- coding: utf-8 -*-

from app import app
from flask import render_template, redirect, request
from datetime import datetime
from app.model import load_data, save_data


@app.route("/")
def index():
    greeting_list = load_data()
    return render_template("index.html", greeting_list = greeting_list)
    

@app.route("/post", methods=['post', 'get'])
def add_message():
    name = request.form.get('n')
    msg  = request.form.get('m')
    create_at = datetime.now().strftime('%b-%d-%y %H:%M:%S')
    save_data(name, msg, create_at)
    return redirect("/")