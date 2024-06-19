from wtforms import Form, StringField, validators

class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
