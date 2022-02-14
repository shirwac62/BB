from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class bloodForm(FlaskForm):
    blood_group = StringField('Blood Group', validators=[DataRequired(), Length(min=2, max=20)])
    packets_donated = IntegerField('Packets donoted', validators=[DataRequired()])
    submit = SubmitField('Submit')
