from flask import render_template
from utility.blueprint import ProjectBlueprint
from utility.user import is_logged_in
from web.blueprints.donor.model import BloodModel

blueprint = ProjectBlueprint('dashboard', __name__)


@blueprint.route(blueprint.url, methods=['GET', 'POST'])
@is_logged_in
def dashboard():
    result = BloodModel.query.all()
    print(result)
    if result:
        return render_template('dashboard.html', details=result)
    else:
        msg = ' Blood Banks Empty '
        return render_template('dashboard.html', msg=msg)
    return None
