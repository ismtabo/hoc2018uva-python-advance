from flask import Flask, json, jsonify, render_template, request
from flask_jwt_extended import get_jti, get_raw_jwt, jwt_required
from flask_socketio import SocketIO, emit, socketio
from playhouse.shortcuts import model_to_dict
from flask_cors import CORS

import authentication as auth
import database as db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['JWT_BLACKLIST_ENABLED'] = True

cors = CORS(app, resources={
            r"/comments": {"origins": "*"},
            r"/auth/*": {"origins": "*"}
            })
socketio = SocketIO(app, json=json)
app.cli.add_command(db.database_cli)
auth.jwt.init_app(app)

users_connected = 0


@app.before_request
def before_request():
    db.database.connect(reuse_if_open=True)


@app.after_request
def after_request(response):
    if not db.database.is_closed():
        db.database.close()
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


@app.route('/comments', methods=['GET', 'POST'])
@jwt_required
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
                      'comment': model_to_dict(comment)}, broadcast=True)

        return jsonify({'comment': model_to_dict(comment)})

    comments = db.get_comments().dicts()

    return jsonify({'comments': [comment for comment in comments]})


@app.route('/auth/login', methods=['POST'])
def login():
    if not request.is_json:
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.get_json().get('username')
        password = request.get_json().get('password')
    token = auth.login_user(username, password)
    return jsonify({'token': token, 'user': {'username': username}})


@app.route('/auth/register', methods=['POST'])
def register():
    if not request.is_json:
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = request.get_json().get('username')
        password = request.get_json().get('password')
    token = auth.register_user(username, password)
    return jsonify({'token': token, 'user': {'username': username}})


@app.route('/auth/logout', methods=['POST'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    auth.logout_user(jti)
    return jsonify({})


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
