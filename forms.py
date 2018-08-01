from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class SelectVerseForm(FlaskForm):
    book = StringField('Book', validators = [DataRequired(), Length(min=2, max=20)])
    chapter = IntegerField('Chapter', validators = [NumberRange(min=1)])
    verse = IntegerField('Verse', validators = [NumberRange(min=1)])

    submit = SubmitField('Start')

class ReciteForm(FlaskForm):
    text = TextAreaField('', validators = [DataRequired(), Length(min=1)])
    submit = SubmitField('Submit')
