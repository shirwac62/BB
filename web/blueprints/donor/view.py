from flask import request, flash, url_for, render_template, jsonify
from werkzeug.utils import redirect

from utility.blueprint import ProjectBlueprint
from utility.user import is_logged_in
from web.blueprints.donor.model import DonorModel, BloodModel
from web.extensions import db

blueprint = ProjectBlueprint('donor', __name__)


@blueprint.route(blueprint.url)
def index():
    logs = DonorModel.query.all()
    return render_template('donor/index.html', logs=logs)


@blueprint.route(blueprint.url + '/api')
def pub_index():
    start = int(request.args.get('start', 0))
    search = request.args.get('search[value]', '')
    print("search: ", search)
    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(DonorModel.id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = DonorModel.query.filter(DonorModel.name.ilike('%' + search + '%')).paginate(page, length, True)
    data = []
    for b in data_list.items:
        row = [b.id, b.name, b.sex, b.age, b.weight, b.address, b.disease, b.tel]
        data += [row]
    print("data_list.total: ", data_list.total)
    return jsonify({'data': data, "recordsTotal": data_list.total,
                    "recordsFiltered": data_list.total})


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

    return render_template('donor/add.html')


@blueprint.route(blueprint.url + '/add_blood', methods=['GET', 'POST'])
@is_logged_in
def add_blood():
    if request.method == 'POST':
        donor_id = request.form["donor_id"]
        blood_group = request.form["blood_group"]
        packets_donated = request.form["packets_donated"]
        data = BloodModel(donor_id, blood_group, packets_donated)
        data.save_to_db()
        flash('Success! Donor Blood details Added.', 'success')
        return redirect(url_for('dashboard.dashboard'))
    return render_template('donor/add_blood.html')























# @blueprint.route(blueprint.url + '/add_blood', methods=['GET', 'POST'])
# @is_logged_in
# def add_blood():
#     form = bloodForm()
#     if form.validate_on_submit():
#         data = BloodForm()
#         form.populate_obj(data)
#         save_to_db(data)
#         flash('Success! Donor Blood details Added.', 'success')
#         return redirect(url_for('dashboard.dashboard'))
#     return render_template('donor/add_blood.html')
