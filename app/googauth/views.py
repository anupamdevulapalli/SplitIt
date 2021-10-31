from . import goog_blueprint
from flask_login import current_user, login_user
from flask_dance.contrib.google import google
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from sqlalchemy.orm.exc import NoResultFound
from ..models import db, User, OAuth

from flask import redirect, url_for, flash, render_template
from flask_login import login_user, login_required, logout_user, login_manager

@goog_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for("main.index_in"))

@goog_blueprint.route("/")
def index():
    return redirect(url_for("google.login"))

# create/login local user on successful OAuth login
@oauth_authorized.connect_via(goog_blueprint)
def google_logged_in(goog_blueprint, token):
    if not token:
        flash("Failed to log in.", category="error")
        return False

    resp = goog_blueprint.session.get("/oauth2/v1/userinfo")
    if not resp.ok:
        msg = "Failed to fetch user info."
        flash(msg, category="error")
        return False

    info = resp.json()
    user_id = info["id"]

    # Find this OAuth token in the database, or create it
    query = OAuth.query.filter_by(provider=goog_blueprint.name, provider_user_id=user_id)
    try:
        if query.first() == None:
            raise NoResultFound
        oauth = query.first()
    except NoResultFound:
        oauth = OAuth(provider=goog_blueprint.name, provider_user_id=user_id, token=token)

    if oauth != None and oauth.user:
        login_user(oauth.user)
        flash("Successfully signed in.")

    else:
        # Create a new local user account for this user
        user = User(name=info['name'], email=info["email"])
        # Associate the new local user account with the OAuth token
        oauth.user = user
        # Save and commit our database models
        db.session.add_all([user, oauth])
        db.session.commit()
        # Log in the new local user account
        login_user(user)
        flash("Successfully signed in.")

    # Disable Flask-Dance's default behavior for saving the OAuth token. This can be also done if you just return a redirect object
    return redirect(url_for("main.home"))

# notify on OAuth provider error
@oauth_error.connect_via(goog_blueprint)
def google_error(goog_blueprint, message, response):
    msg = ("OAuth error from {name}! " "message={message} response={response}").format(
        name=goog_blueprint.name, message=message, response=response
    )
    flash(msg, category="error")