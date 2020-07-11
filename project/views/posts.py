from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user

from forms.posts import PostForm
from models.post import Post
from models.db import Session

posts_app = Blueprint("posts_app", __name__)


@posts_app.route("/post_<int:post_id>/", endpoint="post")
def read_post(post_id):
    post = Session.query(Post).filter_by(id=post_id).first()
    return render_template("posts/read.html", post=post)

@posts_app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_post():
    form = PostForm()
    if request.method == "POST" and form.validate():
        post = Post(
            title=request.form.get('title'),
            text=request.form.get('text'),
            image_url=request.form.get('image_url'),
            user_id=current_user.id
        )
        Session.add(post)
        Session.commit()
        return redirect(url_for("main"))
    return render_template("posts/create.html", form=form)


@posts_app.route("/<int:post_id>/update/", methods=["GET", "POST"], endpoint="update")
def update_post(post_id):
    post = Session.query(Post).filter_by(id=post_id).first()
    form = PostForm(obj=post)
    if request.method == "POST" and form.validate():
        post.title = request.form.get('title')
        post.text = request.form.get('text')
        post.image_url = request.form.get('image_url')

        Session.commit()
        return redirect(url_for("main"))
    return render_template("posts/update.html", form=form, post_id=post.id)
