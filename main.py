from flask import Flask, json, render_template, request
from flask_socketio import SocketIO, emit, socketio

import database as db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, json=json)

users_connected = 0


@app.before_request
def before_request():
    db.database.connect(reuse_if_open=True)


@app.after_request
def after_request(response):
    if not db.database.is_closed():
        db.database.close()
    return response

app.cli.add_command(db.database_cli)


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

        comment = db.create_comment(title, content, author)
        socketio.emit('new comment', {
                      'comment': comment}, broadcast=True)

        return json.dumps({'comment': comment})

    comments = db.get_comments()

    return json.dumps({'comments': [comment for comment in comments]})


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
