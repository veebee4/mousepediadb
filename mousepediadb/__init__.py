# import modules and functions
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# checking if env.py file exists for environment settings
if os.path.exists("env.py"):
    import env


# creating flask application and app configuration files
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


# assigning SQLAlchemy class instance to variable & migrate to update models
db = SQLAlchemy(app)

from mousepediadb import routes
