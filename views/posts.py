import os

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename

from config import IMAGES_DIR
from forms.posts import PostForm
from models import Post
from models.db import Session

posts_app = Blueprint("posts_app", __name__)


@posts_app.route("/create/", methods=["GET", "POST"], endpoint="create")
def create_post():
    form = PostForm()
    if request.method == "POST":
        if form.validate():
            f = request.files['image']
            filename = secure_filename(f.filename)
            f.save(os.path.join(IMAGES_DIR, filename))
            post = Post(
                title=request.form.get('title'),
                text=request.form.get('text'),
                image=filename,
                user_id=current_user.id
            )
            Session.add(post)
            Session.commit()
            return redirect(url_for("main"))
        else:
            print('form invalid')
    return render_template("posts/post_create.html", form=form)


