from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from models import User
from models.db import Session


class AuthForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])


class LoginForm(AuthForm):
    def get_user(self, username):
        return Session.query(User).filter_by(username=username).first()


    def validate_username(self, field):
        if not self.get_user(field.data):
            field.errors.append("Пользователь с таким логином не зарегистрирован")


    def validate_password(self, field):
        user = self.get_user(self.username.data)
        if user and (not user.password == User.hash_password(field.data)):
            field.errors.append("Неправильный пароль")


class RegistrationForm(AuthForm):
    confirm = PasswordField("Подтверждение пароля", validators=[DataRequired()])

    def validate_username(self, field):
        if len(field.data) < 6:
            field.errors.append('Логин должен быть не менее 6 символов')
        if Session.query(User).filter_by(username=field.data).first():
            field.errors.append('Пользователь с таким логином уже зарегистрирован')

    def validate_password(self, field):
        if len(field.data) < 6:
            field.errors.append('Пароль должен быть не менее 6 символов')
        if field.data == self.username.data:
            field.errors.append('Пароль не должен быть таким же как и логин')

    def validate_confirm(self, field):
        if not field.data == self.password.data:
            field.errors.append('Пароли не совпадают')
