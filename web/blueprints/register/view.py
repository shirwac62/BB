import random
from flask import request, flash, url_for, render_template
from passlib.handlers.sha2_crypt import sha256_crypt
from werkzeug.utils import redirect
from web.blueprints.register.forms import RegisterForm
from web.blueprints.register.model import UserModel
from utility.blueprint import ProjectBlueprint

blueprint = ProjectBlueprint('register', __name__)


@blueprint.route(blueprint.url, methods=['GET', 'POST'])
def index():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        e_id = name + str(random.randint(1111,9999))
        if UserModel.find_by_email(email):
            flashing_message = "user already exists"
            flash(flashing_message, "error")
            return redirect(url_for('register.index'))

        else:
            user = UserModel(e_id, name, email, password, )

            user.save_to_db()

            flashing_message = "Success! You can log in with Employee ID " + e_id
            flash(flashing_message, "success")

        return redirect(url_for('login.index'))

    return render_template('register.html', form=form)
