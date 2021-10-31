#This bluepint will deal with all user management functionality 

from re import template
from flask import Blueprint
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from ..models import db, OAuth
from flask_login import current_user
from config import Config



goog_blueprint = make_google_blueprint(
    scope=["profile", "email"],
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user),
    client_id=Config.GCLIENTID,
    client_secret=Config.GCLIENTSEC
)


from . import views