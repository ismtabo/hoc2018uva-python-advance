from collections import namedtuple
from datetime import datetime

from flask import json, current_app
from tinydb import TinyDB
from tinydb_serialization import SerializationMiddleware, Serializer


class FlaskSerializer(Serializer):
    OBJ_CLASS = object

    def encode(self, obj):
        return json.dumps(obj)

    def decode(self, s):
        return json.loads(s)


serialization = SerializationMiddleware()
serialization.register_serializer(FlaskSerializer(), 'TinyFlask')

Comment = namedtuple('Comment', ['title', 'content', 'author', 'datetime'])
comments = [
    Comment("First comment", "This page isn't bad at all.",
            "Author 1", datetime(year=2017, month=12, day=1)),
    Comment("Second comment", "Yeah, I really like it.",
            "Author 2", datetime.utcnow()),
]

db = TinyDB('database.json', storage=serialization)
comments = db.table('comments')


def get_comments():
    return comments.all()


def create_comment(title, content, author):
    comment = Comment(title, content, author, datetime.utcnow())
    comments.insert(comment._asdict())
    return comment
