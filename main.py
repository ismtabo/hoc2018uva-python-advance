from datetime import datetime
from collections import namedtuple

from flask import Flask, render_template
app = Flask(__name__)

Comment = namedtuple('Comment', ['title', 'content', 'datetime'])

@app.route('/')
def hello_world():
    comment = Comment("First comment", "This page isn't bad at all.", datetime.utcnow())
    return render_template('index.html', comment=comment)