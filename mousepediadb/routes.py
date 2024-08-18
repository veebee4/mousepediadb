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


@app.route("/edit_park/<int:park_id>", methods=["GET", "POST"])
def edit_park(park_id):
    park = Park.query.get_or_404(park_id)
    if request.method == "POST":
        park.park_name = request.form.get("park_name")
        park.park_address = request.form.get("park_address")
        park.park_description = request.form.get("park_description")
        park.date_opened = request.form.get("date_opened")
        park.time_open = request.form.get("time_open")  
        park.time_closed = request.form.get("time_closed")  
        park.num_restaurants = request.form.get("num_restaurants")
        park.num_rides = request.form.get("num_rides")
        park.entertainment = request.form.get("entertainment")
        park.special_features = request.form.get("special_features")
        park.transport_between_parks = request.form.get("transport_between_parks")
        park.image_url = request.form.get("image_url")
        db.session.commit()
        return redirect(url_for("parks"))
    return render_template("edit_park.html", park=park)


@app.route("/delete_park/<int:park_id>")
def delete_park(park_id):
    park = Park.query.get_or_404(park_id)
    db.session.delete(park)
    db.session.commit()
    return redirect(url_for("parks"))


@app.route("/rides")
def rides():
    rides = Ride.query.order_by(Ride.ride_name).all()
    return render_template("rides.html", rides=rides)


@app.route("/add_ride", methods=["GET", "POST"])
def add_ride():
    if request.method == "POST":
        try:
            ride_name = request.form.get("ride_name")
            park_id = request.form.get("park_id")
            ride_location = request.form.get("ride_location")
            ride_description = request.form.get("ride_description")

            # Check if the park_id exists
            park = Park.query.get(park_id)
            if not park:
                flash("Invalid park ID. Please select a valid park.", "error")
                return redirect(url_for("add_ride"))

            ride = Ride(
                park_id=park_id,
                ride_name=ride_name,
                ride_location=ride_location,
                ride_description=ride_description,
            )
            db.session.add(ride)
            db.session.commit()
            return redirect(url_for("rides"))

        except Exception as e:
            db.session.rollback()
            return redirect(url_for("add_ride"))
    parks = Park.query.all()
    return render_template("add_ride.html")