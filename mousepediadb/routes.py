# import modules and functions
from flask import render_template, session, request, redirect, url_for
from mousepediadb import app, db
from mousepediadb.models import Park, Restaurant, Ride


@app.route("/")
def home():
    parks = Park.query.order_by(Park.park_name).all()
    return render_template("home.html", parks=parks)


@app.route("/parks")
def parks():
        parks = Park.query.order_by(Park.park_name).all()
        return render_template("parks.html", parks=parks)


@app.route("/add_park", methods=["GET", "POST"])
def add_park():
    if request.method == "POST":
        park_name = request.form.get("park_name")
        park_address = request.form.get("park_address")
        park_description = request.form.get("park_description")
        date_opened = request.form.get("date_opened")
        time_open = request.form.get("time_open")  
        time_closed = request.form.get("time_closed")  
        num_restaurants = request.form.get("num_restaurants")
        num_rides = request.form.get("num_rides")
        entertainment = request.form.get("entertainment")
        special_features = request.form.get("special_features")
        transport_between_parks = request.form.get("transport_between_parks")
        image_url = request.form.get("image_url")

        park = Park(
            park_name=park_name,
            park_address=park_address,
            park_description=park_description,
            date_opened=date_opened,
            time_open=time_open,
            time_closed=time_closed,
            num_restaurants=num_restaurants,
            num_rides=num_rides,
            entertainment=entertainment,
            special_features=special_features,
            transport_between_parks=transport_between_parks,
            image_url=image_url,
        )
        db.session.add(park)
        db.session.commit()
        return redirect(url_for("parks"))
    return render_template("add_park.html")