from . import main_blueprint
from ..googauth import goog_blueprint
from flask import render_template, request, redirect, url_for, current_app, abort
from flask_login import login_required

@main_blueprint.route('/')
def index_in():
    current_app.logger.info("Index page loading")
    return render_template('main/index_in.html')

@main_blueprint.route('/home')
def home():
    try:
        if goog_blueprint.session.authorized:
            current_app.logger.info("Home page loading")
            return render_template('main/index_out.html')
        else:
            return render_template('main/index_in.html')
    except:
        return render_template('main/index_in.html')

@main_blueprint.route('/admin')
def admin():
    abort(500)