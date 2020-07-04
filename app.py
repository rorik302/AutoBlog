from flask import Flask, render_template

from models.db import Session
from views.auth import auth_app

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY="7zWV@9&BKn6!SFXKhEioZ!6kHvLgKj8Q"
)

app.register_blueprint(auth_app, url_prefix="/auth")


@app.route("/")
def main():
    return render_template("index.html")


@app.teardown_request
def remove_session(*args):
    Session.remove()


if __name__ == '__main__':
    app.run()
