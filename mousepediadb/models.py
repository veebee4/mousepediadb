from mousepediadb import db

class Restaurant(db.Model):
    # Schema for the Restaurants model
    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(50), unique=True, nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey("park.id"), nullable=False)
    restaurant_location = db.Column(db.Text, nullable=False)
    dine_or_quick_service = db.Column(db.Boolean, default=False, nullable=False)
    food_type = db.Column(db.String(30), nullable=False)
    restaurant_description = db.Column(db.Text, nullable=False)
    park = db.relationship("Park", backref=db.backref("restaurants", lazy=True))

    def __repr__(self):
        # returns chosen fields from the above schema
        return (
            f"  Restaurant Name        : {self.restaurant_name}\n"
            f"  Location               : {self.restaurant_location}\n"
            f"  Type of Service        : {'Dine-in' if self.dine_or_quick_service else 'Quick Service'}\n"
            f"  Food Type              : {self.food_type}\n"
            f"  Description            : {self.restaurant_description}\n"
            f"  Park Name              : {self.park.park_name if self.park else 'Unknown'}\n"
        )


class Ride(db.Model):
    # Schema for the Rides model
    id = db.Column(db.Integer, primary_key=True)
    ride_name = db.Column(db.String(50), unique=True, nullable=False)
    park_id = db.Column(db.Integer, db.ForeignKey("park.id", ondelete="CASCADE"), nullable=False)
    ride_location = db.Column(db.String(50), nullable=False)
    ride_description = db.Column(db.Text, nullable=False)
    park = db.relationship("Park", backref=db.backref("rides", lazy=True))

    def __repr__(self):
        # returns chosen fields from the above schema
        return (
            f"  Ride ID         : {self.id}\n"
            f"  Ride Name       : {self.ride_name}\n"
            f"  Location        : {self.ride_location}\n"
            f"  Description     : {self.ride_description}\n"
            f"  Park Name       : {self.park.park_name if self.park else 'Unknown'}\n"
        )


class Park(db.Model):
    # Schema for the Parks model
    id = db.Column(db.Integer, primary_key=True)
    park_name = db.Column(db.String(50), unique=True, nullable=False)
    park_address = db.Column(db.String(50), unique=True, nullable=False)
    park_description = db.Column(db.Text, nullable=False)
    date_opened = db.Column(db.Date, nullable=False)
    time_open = db.Column(db.Time, nullable=False)
    time_closed = db.Column(db.Time, nullable=False)
    num_restaurants = db.Column(db.Integer, nullable=False)
    num_rides = db.Column(db.Integer, nullable=False)
    entertainment = db.Column(db.Text, nullable=False)
    special_features = db.Column(db.Text, nullable=False)
    transport_between_parks = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    ride = db.relationship("Ride", backref=db.backref("parks", cascade="all, delete", lazy=True))
    restaurant = db.relationship("Restaurant", backref=db.backref("parks", cascade="all, delete", lazy=True))

    def __repr__(self):
        # returns chosen fields from the above schema
        return (
            f"  Park ID                 : {self.id}\n"
            f"  Park                    : {self.park_name}\n"
            f"  Address                 : {self.park_address}\n"
            f"  Description             : {self.park_description}\n"
            f"  Date Opened             : {self.date_opened}\n"
            f"  Operating Hours         : {self.time_open} - {self.time_closed}\n"
            f"  Restaurants             : {self.num_restaurants}\n"
            f"  Rides                   : {self.num_rides}\n"
            f"  Entertainment           : {self.entertainment}\n"
            f"  Special Features        : {self.special_features}\n"
            f"  Transport Between Parks : {self.transport_between_parks}\n"
        )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
