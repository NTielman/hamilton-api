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
    birth_date = DateField(null=True)
    bio = TextField(null=True)
    photo_url = CharField(null=True)


class Act(BaseModel):
    act_number = IntegerField(primary_key=True)
    plot = TextField()


class Role(BaseModel):
    role_id = AutoField()
    full_name = CharField()
    gender = TextField(choices=["M", "F"])
    birth_date = DateField(null=True)
    part_size = TextField(choices=["Lead", "Supporting"])
    bio = TextField(null=True)
    photo_url = CharField(null=True)
    acts = ManyToManyField(Act, backref="roles")
    cast_member = ForeignKeyField(Cast, backref="roles", on_delete="CASCADE")


ActRoles = Role.acts.get_through_model()


class Song(BaseModel):
    song_id = AutoField()
    title = CharField()
    lyrics = TextField()
    duration = TimeField()
    singers = ManyToManyField(Role, backref="songs", on_delete="CASCADE")
    act = ForeignKeyField(Act, backref="songs")


SongRoles = Song.singers.get_through_model()


class Musical_info(BaseModel):
    title = CharField()
    synopsis = TextField()
    category = TextField()
    release_year = DateField()
    genre = TextField()
    poster_url = CharField(null=True)


def create_tables():
    with db:
        db.create_tables([Cast, Act, Role, Song, ActRoles, SongRoles, Musical_info])
