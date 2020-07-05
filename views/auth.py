from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from forms.auth import LoginForm, RegistrationForm
from models import User
from models.db import Session

auth_app = Blueprint("auth_app", __name__)


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        user = Session.query(User).filter_by(username=form.username.data).first()
        login_user(user)
        return redirect(url_for("main"))
    return render_template("auth/login.html", form=form)


@auth_app.route("/registration", methods=["GET", "POST"], endpoint="registration")
def registration():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        user = User(
            username=form.username.data,
            password=form.password.data
        )
        Session.add(user)
        Session.commit()

        flash(
            message=f'Пользователь {user.username} успешно зарегистрирован',
            category='success'
        )
        return redirect(url_for("auth_app.login"))
    return render_template("auth/registration.html", form=form)


@auth_app.route("/logout/", endpoint="logout")
def logout():
    logout_user()
    return redirect(url_for("main"))