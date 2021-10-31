from . import main_blueprint
from ..googauth import goog_blueprint
from flask import render_template, request, redirect, url_for, current_app, abort

@main_blueprint.route('/')
def index_in():
    current_app.logger.info("Index page loading")
    return render_template('main/index_in.html')

@main_blueprint.route('/home')
@goog_blueprint.session.authorization_required
def home():
    current_app.logger.info("Home page loading")
    return render_template('main/index_out.html')

@main_blueprint.route('/admin')
def admin():
    abort(500)