from utility.blueprint import ProjectBlueprint
from utility.user import is_logged_in

blueprint = ProjectBlueprint('dashboard', __name__)


@blueprint.route(blueprint.url, methods=['GET', 'POST'])
@is_logged_in
def dashboard():
    # cur = mysql.connection.cursor()
    # result = cur.callproc('BLOOD_DATA')
    # details = cur.fetchall()
    #
    # if result > 0:
    #     return render_template('dashboard.html', details=details)
    # else:
    #     msg = ' Blood Bank is Empty '
    #     return render_template('dashboard.html', msg=msg)
    # # close connection
    # cur.close()
    return None