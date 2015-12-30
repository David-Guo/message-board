from flask import Flask
from flask import render_template, redirect, request
import shelve
from datetime import datetime

# 初始化数据库等信息

app = Flask(__name__)

DATA_FILE = 'guestbook.dat'

@app.route("/")
def index():
    greeting_list = load_data()
    return render_template("index.html", greeting_list = greeting_list)


def save_data(name, comment, create_at):
    """
    save data from form submitted
    """
    database = shelve.open(DATA_FILE)

    if 'greeting_list' not in database:
        greeting_list = []
    else:
        greeting_list = database['greeting_list']

    greeting_list.insert(
        0, {'name': name, 'comment': comment, 'create_at': create_at})
        
    database['greeting_list'] = greeting_list
    database.close()


def load_data():
    """
    load saved data
    """
    database = shelve.open(DATA_FILE)
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list

    
@app.route("/post", methods=['post'])
def add_message():
    name = request.form.get('n')
    msg  = request.form.get('m')
    create_at = datetime.now().strftime('%b-%d-%y %H:%M:%S')
    save_data(name, msg, create_at)
    return redirect("/")
