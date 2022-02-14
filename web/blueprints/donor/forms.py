from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

from utility.util_common import get_all
from web.blueprints import donor
from web.blueprints.donor.model import DonorModel


class bloodForm(FlaskForm):
    blood_group = StringField('Blood Group', validators=[DataRequired(), Length(min=2, max=20)])
    packets_donated = IntegerField('Packets donoted', validators=[DataRequired()])
    donor_id = SelectField(choices=[], coerce=str)
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(bloodForm, self).__init__(*args, **kwargs)
        self.donor_id.choices = [(0, "Select DonorModel")] + [(a.donor_id, str(a)) for a in get_all(DonorModel)]
