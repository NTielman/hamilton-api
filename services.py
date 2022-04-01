import peewee
from peewee import fn
from playhouse.shortcuts import model_to_dict
from models import Cast, Role, Song, Musical_info
from datetime import date
from typing import Union

################# Cast queries #################
def add_cast(
    full_name: str, birth_date: date, bio: str, photo_url: str
) -> Union[peewee.Autofield, bool]:
    """adds a castmember to database"""
    try:
        new_cast = Cast.create(
            full_name=full_name, birth_date=birth_date, bio=bio, photo_url=photo_url
        )
        return new_cast.cast_id
    except peewee.PeeweeException:
        return False


def get_cast() -> list:
    """returns all castmembers"""
    query = Cast.select()
    cast_members = [model_to_dict(cast_member) for cast_member in query]
    return cast_members


def get_cast_by_id(cast_id: peewee.AutoField) -> Union[dict, bool]:
    """returns a castmember by id"""
    try:
        cast_member = Cast.get_by_id(cast_id)
        return model_to_dict(cast_member)
    except peewee.DoesNotExist:
        return False


def get_cast_by_name(cast_name: str) -> list:
    """returns castmember(s) matching name"""
    query = Cast.get(Cast.full_name % cast_name)
    cast_members = [model_to_dict(cast_member) for cast_member in query]
    return cast_members


def get_cast_by_role(role_id: peewee.AutoField) -> Union[dict, bool]:
    """returns castmember by role"""
    try:
        cast_member = Role.get_by_id(role_id).cast_member
        return model_to_dict(cast_member)
    except peewee.DoesNotExist:
        return False


def get_random_cast() -> dict:
    """returns a random castmember"""
    cast_member = Cast.select().order_by(fn.Random()).limit(1)
    return model_to_dict(cast_member)


################# Role queries #################
def add_role(
    full_name: str,
    birth_date: date,
    bio: str,
    photo_url: str,
    cast_id: peewee.AutoField,
) -> Union[peewee.Autofield, bool]:
    """adds a role to database"""
    try:
        cast_member = Cast.get_by_id(cast_id)
        new_role = Role.create(
            full_name=full_name,
            birth_date=birth_date,
            bio=bio,
            photo_url=photo_url,
            cast_member=cast_member,
        )
        return new_role.role_id
    except peewee.PeeweeException:
        return False


def get_roles() -> list:
    """returns all roles"""
    query = Role.select()
    roles = [model_to_dict(role) for role in query]
    return roles


def get_role_by_id(role_id: peewee.AutoField) -> Union[dict, bool]:
    """returns a role by id"""
    try:
        role = Role.get_by_id(role_id)
        return model_to_dict(role)
    except peewee.DoesNotExist:
        return False


def get_roles_by_name(role_name: str) -> list:
    """returns role(s) matching name"""
    query = Role.get(Role.full_name % role_name)
    roles = [model_to_dict(role) for role in query]
    return roles


def get_roles_by_cast(cast_id: peewee.AutoField) -> list:
    """returns role(s) by castmember"""
    query = Cast.get_by_id(cast_id).roles
    roles = [model_to_dict(role) for role in query]
    return roles


def get_roles_by_song(song_id: peewee.AutoField) -> list:
    """returns role(s) by song"""
    query = Song.get_by_id(song_id).singers
    roles = [model_to_dict(role) for role in query]
    return roles


def get_random_role() -> dict:
    """returns a random role"""
    role = Role.select().order_by(fn.Random()).limit(1)
    return model_to_dict(role)


################# Song queries #################
def add_song(
    title: str, lyrics: str, duration_in_seconds: int, role_ids: peewee.AutoField
) -> Union[peewee.Autofield, bool]:
    """adds a song to database"""
    try:
        singers = Role.select().where(Role.role_id << role_ids)
        new_song = Song.create(
            title=title,
            lyrics=lyrics,
            duration_in_seconds=duration_in_seconds,
            singers=singers,
        )
        return new_song.song_id
    except peewee.PeeweeException:
        return False


def get_songs() -> list:
    """returns all songs"""
    query = Song.select()
    songs = [model_to_dict(song) for song in query]
    return songs


def get_song_by_id(song_id: peewee.AutoField) -> Union[dict, bool]:
    """returns a song by id"""
    try:
        song = Song.get_by_id(song_id)
        return model_to_dict(song)
    except peewee.DoesNotExist:
        return False


def get_songs_by_title(song_title: str) -> list:
    """returns songs(s) matching title"""
    query = Song.get(Song.title % song_title)
    songs = [model_to_dict(song) for song in query]
    return songs


def get_songs_by_role(role_id: peewee.AutoField) -> list:
    """returns song(s) by role"""
    query = Role.get_by_id(role_id).songs
    songs = [model_to_dict(song) for song in query]
    return songs


def get_random_song() -> dict:
    """returns a random song"""
    song = Song.select().order_by(fn.Random()).limit(1)
    return model_to_dict(song)


################# Musical query #################
def add_musical_info(
    title: str, synopsis: str, release_year: date, poster_url: str
) -> Union[Musical_info, bool]:
    """adds musical info to database"""
    try:
        return Musical_info.create(title, synopsis, release_year, poster_url)
    except peewee.PeeweeException:
        return False


def get_musical_info() -> Union[dict, bool]:
    """returns general musical info"""
    try:
        musical_info = Musical_info[0]
        return model_to_dict(musical_info)
    except peewee.DoesNotExist:
        return False
