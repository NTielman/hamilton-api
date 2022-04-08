import os
from peewee import *

# Ensure database "hamilton.db" is created in current folder
full_path = os.path.realpath(__file__)
file_dir = os.path.dirname(full_path)
db_path = os.path.join(file_dir, "hamilton.db")

db = SqliteDatabase(db_path, pragmas={"foreign_keys": 1})
# Pragmas ensure foreign-key constraints are enforced.


class BaseModel(Model):
    class Meta:
        database = db


class Cast(BaseModel):
    cast_id = AutoField()
    full_name = CharField()
    birth_date = DateField()
    bio = TextField(null=True)
    photo_url = CharField(null=True)


class Role(BaseModel):
    role_id = AutoField()
    full_name = CharField()
    birth_date = DateField()
    bio = TextField(null=True)
    photo_url = CharField(null=True)
    cast_member = ForeignKeyField(Cast, backref="roles", on_delete="CASCADE")
    # historical background?


class Song(BaseModel):
    song_id = AutoField()
    title = CharField()
    lyrics = TextField()
    duration_in_seconds = IntegerField(constraints=[Check("duration_in_seconds > 0")])
    singers = ManyToManyField(Role, backref="songs", on_delete="CASCADE")

SongRoles = Song.singers.get_through_model()

class Musical_info(BaseModel):
    title = CharField()
    synopsis = TextField()
    release_year = DateField()
    poster_url = CharField(null=True)


def create_tables():
    with db:
        db.create_tables([Cast, Role, Song, SongRoles, Musical_info])
