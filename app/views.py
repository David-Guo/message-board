# -*- coding: utf-8 -*-

from app import app
from flask import render_template, redirect, request, jsonify
from datetime import datetime
from app.model import load_data, save_data


@app.route("/")
def index():
    greeting_list = load_data()
    return render_template("home.html")
    

@app.route("/get")
def get_message():
	data = load_data()
	return jsonify(status="success", data=data)

@app.route("/post", methods=["post"])
def add_message():
    name = request.form.get('name')
    comment  = request.form.get('comment')
    create_at = datetime.now().strftime('%b-%d-%y %H:%M:%S')
    save_data(name, comment, create_at)
    #return redirect("/")
    return jsonify(status="success")