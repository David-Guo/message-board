from flask import Flask
from flask import render_template

# 初始化数据库等信息

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
