from collections import namedtuple
from datetime import datetime
import os

from flask import json, current_app
from flask.cli import AppGroup, with_appcontext
from flask_login import UserMixin
from flask_jwt_extended import JWTManager
from peewee import Model, CharField, TextField, DateTimeField
from playhouse.shortcuts import model_to_dict
from playhouse.db_url import connect
from playhouse.flask_utils import get_object_or_404

DATABASE = os.getenv('DATABASE') or 'sqlite:///database.db'

database = connect(DATABASE)
database_cli = AppGroup(
    'database', help='Management operation of the database')


class BaseModel(Model):
    class Meta:
        database = database


class Comment(BaseModel):
    title = CharField()
    content = TextField()
    author = CharField()
    datetime = DateTimeField()


def get_comments():
    return Comment.select()


def create_comment(title, content, author):
    with database.atomic():
        comment = Comment(title=title, content=content,
                          author=author, datetime=datetime.utcnow())
        comment.save()
    return comment


class User(BaseModel, UserMixin):
    username = CharField(unique=True)
    password = CharField()

    def get_id(self):
        return self.username


def create_user(username, password):
    with database.atomic():
        user = User(username=username, password=password)
        user.save()
    return user


def get_user(username):
    return get_object_or_404(User, (User.username == username))


class BlacklistToken(BaseModel):
    token = CharField()
    datetime = DateTimeField()


def create_blacklist_token(token):
    with database.atomic():
        token = BlacklistToken(token=token, datetime=datetime.utcnow())
        token.save()
    return token

def is_toke_blacklisted(token):
    with database:
        return BlacklistToken.select().where(BlacklistToken.token == token).exists()


@database_cli.command('create', help='Create the tables of the database')
def create_tables():
    with database:
        database.create_tables([Comment, User, BlacklistToken])


@database_cli.command('drop', help='Drop the tables of the database')
def drop_tables():
    with database:
        database.drop_tables([Comment, User, BlacklistToken])
