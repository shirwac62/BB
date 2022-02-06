from wtforms import StringField, Form, validators, PasswordField


class RegisterForm(Form):
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=1, max=25)])
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=10, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')
