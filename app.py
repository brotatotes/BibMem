import sys
from bible import Bible
from diff import Diff
from flask import Flask, render_template, url_for, flash, redirect, request
from forms import SelectVerseForm, ReciteForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '4782067e42ba1f8c4e7b84a99b914070'

@app.route('/mem', methods=['GET', 'POST'])
def mem():
    form = ReciteForm()
    if form.validate_on_submit():
        b = Bible()
        actual = b.get_verse(request.args.get("book").lower(), request.args.get("chapter"), request.args.get("verse"), "esv")
        typed = form.text.data

        d = Diff(actual, typed)
        html = d.generate_html()
        return html
    return render_template('mem.html', form=form, book=request.args.get("book"), chapter=request.args.get("chapter"), verse=request.args.get("verse"))

@app.route('/')
def home():
    return redirect(url_for('select_verses'))

@app.route('/select-verses', methods=['GET', 'POST'])
def select_verses():
    form = SelectVerseForm()
    if form.validate_on_submit():
        book = ' '.join(word.capitalize() for word in form.book.data.strip().split())
        chapter = form.chapter.data
        verse = form.verse.data
        return redirect(url_for('mem', book=book, chapter=chapter, verse=verse))
    else:
        return render_template('select-verses.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
