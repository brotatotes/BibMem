import sys
from bible import Bible
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange


class SelectVerseForm(FlaskForm):
    b = Bible()
    book_choices = [(book, ' '.join(word.capitalize() for word in book.split())) for book in b.BOOKS]
    book = SelectField('Book', choices = book_choices)
    chapter = IntegerField('Chapter')
    verse = IntegerField('Verse', validators = [NumberRange(min=1,max=999),])
    version = SelectField('Version', choices = [("amp", "Amplified Bible (AMP)"), ("esv", "English Standard Version (ESV)"), ("niv", "New International Version (NIV)"), ("nkjv", "New King James Version (NKJV)")], default="esv")
    submit = SubmitField('Start')

    def validate(self):
        max_chapter = self.b.CHAPTERS[self.b.BOOKS.index(self.book.data)]
        self.chapter.validators = [NumberRange(min=1,max=max_chapter)]
        if not super().validate():
            return False
        else:
            return True

class ReciteForm(FlaskForm):
    text = TextAreaField('', validators = [DataRequired(), Length(min=1)])
    submit = SubmitField('Submit')
