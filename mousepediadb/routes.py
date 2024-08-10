# import modules and functions
from flask import render_template
from mousepediadb import app, db
from mousepediadb.models import Park, Restaurant, Ride


@app.route("/")
def home():
    return render_template("home.html")