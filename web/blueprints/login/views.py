from flask import request, session, render_template, flash, url_for
from passlib.handlers.sha2_crypt import sha256_crypt
from werkzeug.utils import redirect
from web.blueprints.register.model import UserModel
from utility.blueprint import ProjectBlueprint

blueprint = ProjectBlueprint('login', __name__)


@blueprint.route(blueprint.url, methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        e_id = request.form["e_id"]
        password_candidate = request.form["password"]

        result = UserModel.find_by_user_id(e_id)
        print(result)
        if result != None:

            password = result.password

            if sha256_crypt.verify(password_candidate, password):
                session['logged_in'] = True
                session['e_id'] = e_id

                flash('You are now logged in', 'success')
                return redirect(url_for('index'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
        else:
            error = 'Employee ID not found'
            return render_template('login.html', error=error)

    return render_template('login.html')



