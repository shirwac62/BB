from wtforms import Form, StringField, validators


class ContactForm(Form):
    blood_groub = StringField('Blood Group', [validators.DataRequired()])
    full_name = StringField('Full name', [validators.DataRequired()])
    address = StringField('address', [validators.DataRequired()])
    number_packets = StringField('Number Backets', [validators.DataRequired()])
