from flask import Flask, render_template
from flask_login import LoginManager

from project.models import Post
from project.models import User
from project.models import Session
from project.views.auth import auth_app
from project.views.posts import posts_app
from project.views.users import users_app

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY="7zWV@9&BKn6!SFXKhEioZ!6kHvLgKj8Q"
)

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(posts_app, url_prefix="/posts")
app.register_blueprint(users_app, url_prefix="/users")


@login_manager.user_loader
def load_user(user_id):
    return Session.query(User).filter_by(id=user_id).one_or_none()


@app.route("/", endpoint="main")
def main():
    posts = Session.query(Post).order_by(Post.created)
    return render_template("index.html", posts=posts)


@app.teardown_request
def remove_session(*args):
    Session.remove()


if __name__ == '__main__':
    app.run()
