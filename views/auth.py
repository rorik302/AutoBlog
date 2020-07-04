from flask import render_template, Blueprint, request, redirect, url_for

from forms import LoginForm, RegistrationForm
from models import User
from models.db import Session

auth_app = Blueprint("auth_app", __name__)


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    form = LoginForm()
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
        return redirect(url_for("main"))
    return render_template("auth/registration.html", form=form)