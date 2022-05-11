from flask import request, flash, url_for, render_template, jsonify
from werkzeug.utils import redirect
from sqlalchemy import and_

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
    # search = request.args.get('search[value]', '')
    # print("search: ", search)
    name = request.args.get('name', '')
    address = request.args.get('address', '')
    filter_data = []
    if name:
        filter_data.append(DonorModel.name.ilike('%' + name + '%'))
    if address:
        filter_data.append(DonorModel.address.ilike('%' + address + '%'))

    length = int(request.args.get('length', 5))
    if length and int(length) == -1:
        length = db.session.query(DonorModel.id).count()
    page = (int(start) + int(length)) / int(length)
    data_list = DonorModel.query.filter(and_(*filter_data)).paginate(page, length, True)
    data = []
    for b in data_list.items:
        row = [b.id, b.name, b.sex, b.age, b.weight, b.address, b.disease, b.tel, "<a href='/donor/edit/{}' >Edit</a>".format(b.id)]
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
        donor = DonorModel(dname, tel, sex, age, weight, address, disease)
        donor.save_to_db()
        flash('Success! Donor details Added.', 'success')
        return redirect(url_for('index'))
    return render_template('donor/add.html', title='donor')

    
@blueprint.route(blueprint.url + '/edit/<id_>', methods=['GET', 'POST'])
@is_logged_in
def edit(id_):
    donor = DonorModel.query.filter(DonorModel.id == id_).first()
    if request.method == 'POST':
        # Get Form Fields
        # id = request.form["id"]
        donor.name = request.form["name"]
        donor.sex = request.form["sex"]
        donor.age = request.form["age"]
        donor.weight = request.form["weight"]
        donor.address = request.form["address"]
        donor.disease = request.form["disease"]
        donor.tel = request.form["tell"]
        donor.save_to_db()
        flash('Success! Donor details Added.', 'success')
        return redirect(url_for('index'))

    return render_template('donor/edit.html', data=donor)


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
















