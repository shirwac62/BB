# Check if user logged in
from functools import wraps

from flask import session, flash, url_for
from werkzeug.utils import redirect

from utility.blueprint import ProjectBlueprint


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login!', 'danger')
            return redirect(url_for('login'))

    return wrap
