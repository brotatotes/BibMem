import sys
from bible import Bible
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange


class SelectVerseForm(FlaskForm):
    bible = Bible()
    
    book_choices = []
    for book in bible.books():
        book_choices.append((book, bible.capitalize(book)))
    book = SelectField('Book', choices = book_choices)
    chapter = IntegerField('Chapter')
    verse = IntegerField('Verse')

    version_choices = []
    for version in bible.versions():
        version_choices.append((version, bible.version_name(version)))
    version = SelectField('Version', choices = version_choices, default="esv")

    submit = SubmitField('Start')

    def validate(self):
        max_chapter = self.bible.num_chapters(self.book.data)
        self.chapter.validators = [NumberRange(min=1,max=max_chapter)]
        if self.chapter.data <= max_chapter:
            max_verse = self.bible.num_verses(self.book.data, self.chapter.data)
            self.verse.validators = [NumberRange(min=1,max=max_verse)]
        return super().validate()

class ReciteForm(FlaskForm):
    text = TextAreaField('', validators = [DataRequired(), Length(min=1)])
    submit = SubmitField('Submit')
