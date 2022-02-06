from flask import request, flash, url_for, render_template
from werkzeug.utils import redirect

from utility.blueprint import ProjectBlueprint
from utility.user import is_logged_in
from web.blueprints.donor.model import DonorModel

blueprint = ProjectBlueprint('donor', __name__)


@blueprint.route(blueprint.url)
def index():
    result = DonorModel.list()
    print(result)
    logs = result
    if result:
        return render_template('donorlogs.html', logs=logs)
    else:
        msg = ' No logs found '
        return render_template('donorlogs.html', msg=msg)


@blueprint.route(blueprint.url + '/add', methods=['GET', 'POST'])
@is_logged_in
def add():
    if request.method == 'POST':
        # Get Form Fields
        id = request.form["id"]
        dname = request.form["dname"]
        sex = request.form["sex"]
        age = request.form["age"]
        weight = request.form["weight"]
        address = request.form["address"]
        disease = request.form["disease"]
        tel = request.form["tell"]
        donor = DonorModel(id, dname, tel, sex, age, weight, address, disease)
        donor.save_to_db()
        flash('Success! Donor details Added.', 'success')
        return redirect(url_for('index'))

    return render_template('donate.html')
