from flask import Blueprint, render_template

posts_app = Blueprint("posts_app", __name__)

@posts_app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_post():
    return render_template("posts/post_create.html")