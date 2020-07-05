from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    image = FileField("Картинка")
    text = TextAreaField("Текст", validators=[DataRequired()], render_kw={'rows': 20})