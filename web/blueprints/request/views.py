from flask import render_template

from utility.blueprint import ProjectBlueprint
from utility.user import is_logged_in
from web.blueprints.contact.model import Contact

blueprint = ProjectBlueprint('request', __name__)


@blueprint.route(blueprint.url + '/request', methods=['GET', 'POST'])
@is_logged_in
def request():
    contacts = Contact.query.all()
    return render_template('templates/index.html', title='contact', contacts=contacts)





