from datetime import datetime

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    comment = "First comment", "This page isn't bad at all.", datetime.utcnow()
    return render_template('index.html', comment=comment)