# import modules and functions
from flask import render_template
from mousepediadb import app, db


@app.route("/")
def home():
    return render_template("base.html")