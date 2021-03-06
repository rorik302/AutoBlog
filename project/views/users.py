from flask import Blueprint, render_template

from models.user import User
from models.db import Session

users_app = Blueprint("users_app", __name__)


@users_app.route("/<string:username>/profile/", endpoint="profile")
def profile(username):
    user = Session.query(User).filter_by(username=username).first()
    return render_template("users/profile.html", user=user)
