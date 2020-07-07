from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
    title = StringField("Заголовок", validators=[InputRequired()])
    image_url = StringField("URL картинки")
    text = TextAreaField("Текст", validators=[InputRequired()], render_kw={'rows': 20})