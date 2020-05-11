from peewee import *
from .conn import db


class SmallComments(Model):
    hash = CharField(primary_key=True, unique=True, index=True, max_length=255)
    candidate = CharField(max_length=150, index=True)
    username = CharField(max_length=255)
    comment = TextField()
    clean_comment = TextField(default="")
    sanitized_comment = TextField(default="")

    class Meta:
        database = db


class DefaultComments(SmallComments):
    data = CharField(max_length=50)
    timestamp = TimestampField(resolution=100)

    class Meta:
        database = db


class RawFacebookComments(DefaultComments):
    class Meta:
        database = db
        table_name = "raw_facebook_comments"


class RawInstagramComments(SmallComments):
    class Meta:
        database = db
        table_name = "raw_instagram_comments"


class RawHashtagComments(Model):
    hash = CharField(primary_key=True, unique=True, index=True, max_length=255)
    hashtag = CharField(max_length=150, index=True)
    username = CharField(max_length=255)
    comment = TextField()
    data = CharField(max_length=50)
    timestamp = TimestampField(resolution=100)
    clean_comment = TextField(default="")
    sanitized_comment = TextField(default="")

    class Meta:
        database = db
        table_name = "raw_hashtag_comments"


class UserLocation(Model):
    username = ForeignKeyField(RawHashtagComments, backref="location")
    city = CharField(max_length=255)
    state = CharField(max_length=255)
    region = CharField(max_length=255)
    geo = CharField(max_length=255)

    class Meta:
        database = db
        table_name = "user_geolocation"
