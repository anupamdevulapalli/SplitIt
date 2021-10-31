from . import goog_blueprint
from flask import render_template, request, redirect, url_for
from ..tasks import send_celery_email
from flask_dance.contrib.google import google
from ..models import SecUsers
from app import db

@goog_blueprint.route('/')
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v1/userinfo")
    assert resp.ok, resp.text
    print(resp.json())

    name = resp.json()["name"]
    email = resp.json()["email"]
    id = resp.json()["id"]
    user = SecUsers.query.filter_by(email=email).first()

    if not user:
        user = SecUsers(id=id, full_name=name, email=email)
        db.session.add(user)
        db.session.commit()


    return "You are {email} on Google".format(email=resp.json()["email"])

    # message_data={
    #     'subject': 'Hello from the flask app!',
    #     'body': 'This email was sent asynchronously using Celery.',
    #     'recipients': email,

    # }
    # send_celery_email.apply_async(args=[message_data])
    # return render_template('auth/register.html', email=email)