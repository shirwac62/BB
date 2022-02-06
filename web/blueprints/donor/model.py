from web.extensions import db


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
        return list(map(lambda x: [x.id, x.name, x.tel, x.tel, x.sex, x.age, x.weight, x.address, x.address], DonorModel.query.all()))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
