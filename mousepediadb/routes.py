# import modules and functions
from flask import render_template, session, request, redirect, url_for, flash
from mousepediadb import app, db
from mousepediadb.models import Park, Restaurant, Ride


@app.route("/")
def home():
    # fetch all park records to display
    parks = Park.query.order_by(Park.park_name).all()
    return render_template("home.html", parks=parks)


@app.route("/parks")
def parks():
    # fetch all park records to display
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

        # Check if park name already exists
        existing_park = Park.query.filter_by(park_name=park_name).first()
        if existing_park:
            flash(
                "A park with this name already exists."
                "Please choose a different name.", "danger"
                )
            return redirect(url_for("add_park"))

        # Create the Park object and add to the database
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
        flash("Park added successfully!", "success")
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
        park.transport_between_parks = (
            request.form.get("transport_between_parks")
            )
        park.image_url = request.form.get("image_url")

        db.session.commit()
        flash("Park edited successfully!", "success")
        return redirect(url_for("parks"))
    return render_template("edit_park.html", park=park)


@app.route("/delete_park/<int:park_id>")
def delete_park(park_id):
    park = Park.query.get_or_404(park_id)
    db.session.delete(park)
    db.session.commit()
    flash
    ("Park and associated ride/restaurant records deleted successfully!",
        "success")
    return redirect(url_for("parks"))


@app.route("/rides")
def rides():
    # fetch all ride records to display
    rides = Ride.query.order_by(Ride.ride_name).all()
    return render_template("rides.html", rides=rides)


@app.route("/add_ride", methods=["GET", "POST"])
def add_ride():
    if request.method == "POST":
        ride_name = request.form.get("ride_name")
        park_id = request.form.get("park_id")
        ride_location = request.form.get("ride_location")
        ride_description = request.form.get("ride_description")

        # Check if ride name already exists
        existing_ride = Ride.query.filter_by(ride_name=ride_name).first()
        if existing_ride:
            flash(
                "A ride with this name already exists."
                "Please choose a different name.", "danger"
                )
            return redirect(url_for("add_ride"))

        # Create the Ride object and add to the database
        ride = Ride(
            park_id=park_id,
            ride_name=ride_name,
            ride_location=ride_location,
            ride_description=ride_description,
        )

        db.session.add(ride)
        db.session.commit()
        flash("Ride added successfully!", "success")
        return redirect(url_for("rides"))

    # Fetch the parks to display in a dropdown on the add ride form
    parks = Park.query.all()
    return render_template("add_ride.html", parks=parks)


@app.route("/edit_ride/<int:ride_id>", methods=["GET", "POST"])
def edit_ride(ride_id):
    ride = Ride.query.get_or_404(ride_id)

    if request.method == "POST":
        ride.park_id = request.form.get("park_id")
        ride.ride_name = request.form.get("ride_name")
        ride.ride_description = request.form.get("ride_description")
        ride.ride_location = request.form.get("ride_location")

        db.session.commit()
        flash("Ride edited successfully!", "success")
        return redirect(url_for("rides"))

    # Fetch the parks to display in a dropdown on the edit ride form
    parks = Park.query.all()
    return render_template("edit_ride.html", ride=ride, parks=parks)


@app.route("/delete_ride/<int:ride_id>")
def delete_ride(ride_id):
    ride = Ride.query.get_or_404(ride_id)
    db.session.delete(ride)
    db.session.commit()
    flash("Ride deleted successfully!", "success")
    return redirect(url_for("rides"))


@app.route("/restaurants")
def restaurants():
    # fetch all restaurant records to display
    restaurants = Restaurant.query.order_by(Restaurant.restaurant_name).all()
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/add_restaurant", methods=["GET", "POST"])
def add_restaurant():
    if request.method == "POST":
        restaurant_name = request.form.get("restaurant_name")
        park_id = request.form.get("park_id")
        restaurant_location = request.form.get("restaurant_location")
        restaurant_description = request.form.get("restaurant_description")
        food_type = request.form.get("food_type")

        # collects the selected service types (dine in/quick service)
        service_types = request.form.getlist("service_type")

        # Check if restaurant name already exists
        existing_restaurant = (
            Restaurant.query
            .filter_by(restaurant_name=restaurant_name)
            .first()
            )
        if existing_restaurant:
            flash(
                "A restaurant with this name already exists."
                "Please choose a different name.", "danger"
            )
            return redirect(url_for("add_restaurant"))

        # Create the Restaurant object and add to the database
        restaurant = Restaurant(
            park_id=park_id,
            restaurant_name=restaurant_name,
            restaurant_location=restaurant_location,
            restaurant_description=restaurant_description,
            food_type=food_type,
            dine_in='dine_in' in service_types,
            quick_service='quick_service' in service_types
        )

        db.session.add(restaurant)
        db.session.commit()
        flash("Restaurant added successfully!", "success")
        return redirect(url_for("restaurants"))

    # Fetch the parks to display in a dropdown on the add restaurant form
    parks = Park.query.all()
    return render_template("add_restaurant.html", parks=parks)


@app.route("/edit_restaurant/<int:restaurant_id>", methods=["GET", "POST"])
def edit_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)

    if request.method == "POST":
        restaurant.park_id = request.form.get("park_id")
        restaurant.restaurant_name = request.form.get("restaurant_name")
        restaurant.restaurant_description = (
            request.form.get("restaurant_description")
            )
        restaurant.restaurant_location = (
            request.form.get("restaurant_location")
            )
        restaurant.food_type = request.form.get("food_type")

        # collect the selected service types
        service_types = request.form.getlist("service_type")

        # Update the service types
        restaurant.dine_in = 'dine_in' in service_types
        restaurant.quick_service = 'quick_service' in service_types

        db.session.commit()
        flash("Restaurant edited successfully!", "success")
        return redirect(url_for("restaurants"))

    # Fetch the parks to display in a dropdown on the edit restaurant form
    parks = Park.query.all()
    return render_template(
        "edit_restaurant.html", restaurant=restaurant, parks=parks
        )


@app.route("/delete_restaurant/<int:restaurant_id>")
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)
    db.session.delete(restaurant)
    db.session.commit()
    flash("Restaurant deleted successfully!", "success")
    return redirect(url_for("restaurants"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
