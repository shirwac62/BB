from web.extensions import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_user_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()