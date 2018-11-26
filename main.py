from datetime import datetime
from collections import namedtuple

from flask import Flask, render_template, request
from flask_moment import Moment
from flask_socketio import SocketIO, emit
app = Flask(__name__)
moment = Moment(app)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

Comment = namedtuple('Comment', ['title', 'content', 'author', 'datetime'])
comments = [
    Comment("First comment", "This page isn't bad at all.",
            "Author 1", datetime(year=2017, month=12, day=1)),
    Comment("Second comment", "Yeah, I really like it.",
            "Author 2", datetime.utcnow()),
]
users_connected = 0


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        comments.append(Comment(title, content, author, datetime.utcnow()))

    return render_template('index.html', comments=comments)

@socketio.on('connect')
def socket_connect():
    global users_connected
    users_connected += 1
    emit('new connection', {'users': users_connected}, broadcast=True)

@socketio.on('disconnect')
def socket_disconnect():
    global users_connected
    users_connected -= 1
    emit('new disconnection', {'users': users_connected}, broadcast=True)
