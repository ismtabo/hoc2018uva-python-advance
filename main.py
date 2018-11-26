from datetime import datetime
from collections import namedtuple

from flask import Flask, render_template, request
from flask_moment import Moment
app = Flask(__name__)
moment = Moment(app)

Comment = namedtuple('Comment', ['title', 'content', 'author', 'datetime'])
comments = [
    Comment("First comment", "This page isn't bad at all.",
            "Author 1", datetime(year=2017, month=12, day=1)),
    Comment("Second comment", "Yeah, I really like it.",
            "Author 2", datetime.utcnow()),
]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        comments.append(Comment(title, content, author, datetime.utcnow()))

    return render_template('index.html', comments=comments)
