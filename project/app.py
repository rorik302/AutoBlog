from flask import Flask, render_template
from flask_login import LoginManager

from models.post import Post
from models.user import User
from models.db import Session
from views.auth import auth_app
from views.posts import posts_app
from views.users import users_app

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
