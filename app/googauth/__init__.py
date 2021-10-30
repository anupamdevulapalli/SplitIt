#This bluepint will deal with all user management functionality 

from flask import Blueprint
from flask_dance.contrib.google import make_google_blueprint, google

from config import Config

goog_blueprint = make_google_blueprint(
    client_id=Config.GCLIENTID,
    client_secret=Config.GCLIENTSEC,
    scope=["profile", "email"]
)

from . import views