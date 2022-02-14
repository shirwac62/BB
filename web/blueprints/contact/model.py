from web.extensions import db


class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.String, primary_key=True)
    full_name = db.Column(db.String(80))
    blood_group = db.Column(db.String(80))
    blood_packets = db.Column(db.String(80))
    address = db.Column(db.String(80))

    def __init__(self, id, full_name, blood_group, blood_packets, address):
        self.id = id
        self.full_name = full_name
        self.blood_group = blood_group
        self.blood_packets = blood_packets
        self.address = address

    @classmethod
    def find_by_email(cls, address):
        return cls.query.filter_by(address=address).first()

    @classmethod
    def find_by_user_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
