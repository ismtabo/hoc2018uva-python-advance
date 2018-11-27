from collections import namedtuple
from datetime import datetime
import os

from flask import json, current_app
from flask.cli import AppGroup, with_appcontext
from tinydb import TinyDB
from tinydb_serialization import SerializationMiddleware, Serializer
from peewee import Model, CharField, TextField, DateTimeField
from playhouse.shortcuts import model_to_dict
from playhouse.db_url import connect

DATABASE = os.getenv('DATABASE') or 'sqlite:///database.db'

database = connect(DATABASE)
database_cli = AppGroup('database', help='Management operation of the database')


class BaseModel(Model):
    class Meta:
        database = database


class Comment(BaseModel):
    title = CharField()
    content = TextField()
    author = CharField()
    datetime = DateTimeField()


def get_comments():
    return Comment.select().dicts()


def create_comment(title, content, author):
    with database.atomic():
        comment = Comment(title=title, content=content, author=author, datetime=datetime.utcnow())
        comment.save()
    return model_to_dict(comment)


@database_cli.command('create', help='Create the tables of the database')
def create_tables():
    with database:
        database.create_tables([Comment])


@database_cli.command('drop', help='Drop the tables of the database')
def drop_tables():
    with database:
        database.drop_tables([Comment])
