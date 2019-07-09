from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])

