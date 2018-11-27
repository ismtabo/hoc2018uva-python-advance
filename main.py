from datetime import datetime
from collections import namedtuple

from flask import Flask, render_template, request, json
from flask_moment import Moment
from flask_socketio import SocketIO, emit, socketio
app = Flask(__name__)
moment = Moment(app)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, json=json)

Comment = namedtuple('Comment', ['title', 'content', 'author', 'datetime'])
comments = [
    Comment("First comment", "This page isn't bad at all.",
            "Author 1", datetime(year=2017, month=12, day=1)),
    Comment("Second comment", "Yeah, I really like it.",
            "Author 2", datetime.utcnow()),
]
users_connected = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/comments', methods=['GET', 'POST'])
def on_comments():
    if request.method == 'POST':
        if not request.is_json:
            author = request.form.get('author')
            title = request.form.get('title')
            content = request.form.get('content')
        else:
            author = request.get_json().get('author')
            title = request.get_json().get('title')
            content = request.get_json().get('content')

        comment = Comment(title, content, author, datetime.utcnow())
        comments.append(comment)
        socketio.emit('new comment', {
                      'comment': comment._asdict()}, broadcast=True)

        return json.dumps({'comment': comment._asdict()})

    return json.dumps({'comments': [comment._asdict() for comment in comments]})


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
