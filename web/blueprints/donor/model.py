from web.extensions import db


class BloodModel(db.Model):
    donor_id = db.Column(db.Integer, primary_key=True)
    blood_group = db.Column(db.String(20), unique=False, nullable=False)
    packets_donated = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, donor_id, blood_group, packets_donated):
        self.donor_id = donor_id
        self.blood_group = blood_group
        self.packets_donated = packets_donated

    @classmethod
    def find_by_user_id(cls, donor_id):
        return cls.query.filter_by(donor_id=donor_id).first()

    @classmethod
    def list(cls):
        return list(map(lambda x: [x.donor_id, x.blood_group, x.tel, x.packets_donated],
                        BloodModel.query.all()))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class DonorModel(db.Model):
    __tablename__ = 'donor'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80))
    tel = db.Column(db.Integer())
    sex = db.Column(db.String(80))
    age = db.Column(db.Integer())
    weight = db.Column(db.Integer())
    address = db.Column(db.String(80))
    disease = db.Column(db.String(80))

    def __init__(self, id, name, tel, sex, age, weight, address, disease):
        self.id = id
        self.name = name
        self.tel = tel
        self.sex = sex
        self.age = age
        self.weight = weight
        self.address = address
        self.disease = disease

    @classmethod
    def find_by_user_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def list(cls):
        return list(map(lambda x: [x.id, x.name, x.tel, x.tel, x.sex, x.age, x.weight, x.address, x.address],
                        DonorModel.query.all()))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

