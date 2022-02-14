from flask import request, flash, url_for, render_template
from werkzeug.utils import redirect

from utility.blueprint import ProjectBlueprint
from web.blueprints.contact.model import Contact

blueprint = ProjectBlueprint('contact', __name__)


@blueprint.route(blueprint.url + '/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        id = request.form["id"]
        bgroup = request.form["bgroup"]
        bpackets = request.form["bpackets"]
        fname = request.form["fname"]
        adress = request.form["adress"]
        contact = Contact( id,bgroup, bpackets, fname, adress)
        contact.save_to_db()
        flash('Success! Donor details Added.', 'success')
        # return redirect(url_for('index'))
        return redirect(url_for('index'))
    return render_template('contact/add.html')
