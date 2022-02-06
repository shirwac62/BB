from flask import Flask, render_template, session, flash, url_for
from werkzeug.utils import redirect

from utility.user import is_logged_in
from web.blueprints import blood_list
from web.extensions import db


def create_app(settings_override=None):
    app = Flask(__name__)
    app.secret_key = 'some secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:feelfree252@127.0.0.1:5432/bloodBank'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    for blood in blood_list:
        app.register_blueprint(blood)

    extensions(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/logout')
    @is_logged_in
    def logout():
        session.clear()
        flash('You are now logged out', 'success')
        return redirect(url_for('index'))

    return app


def extensions(app):
    db.init_app(app)

    return None

