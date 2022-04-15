import peewee
from peewee import fn
from playhouse.shortcuts import model_to_dict
from models import Cast, Role, Song, Musical_info
from datetime import date
from typing import Union

################# Cast queries #################
def add_cast(
    full_name: str, birth_date: date, bio: str, photo_url: str
) -> Union[int, bool]:
    """adds a castmember to database"""
    try:
        new_cast = Cast.create(
            full_name=full_name, birth_date=birth_date, bio=bio, photo_url=photo_url
        )
        return new_cast.cast_id
    except peewee.PeeweeException:
        return False


def get_cast(limit: int) -> list:
    """returns all castmembers"""
    if limit:
        query = Cast.select().limit(limit)
    else:
        query = Cast.select()

    cast_members = [model_to_dict(cast_member) for cast_member in query]
    return cast_members


def get_cast_by_id(cast_id: int) -> Union[dict, bool]:
    """returns a castmember by id"""
    try:
        cast_member = Cast.get_by_id(cast_id)
        return model_to_dict(cast_member)
    except peewee.DoesNotExist:
        return False


def get_cast_by_name(cast_name: str, limit: int) -> list:
    """returns castmember(s) matching name"""
    if limit:
        query = Cast.select().where(Cast.full_name ** f"%{cast_name}%").limit(limit)
    else:
        query = Cast.select().where(Cast.full_name ** f"%{cast_name}%")

    cast_members = [model_to_dict(cast_member) for cast_member in query]
    return cast_members


def get_cast_by_role(role_id: int) -> Union[dict, bool]:
    """returns castmember by role"""
    try:
        cast_member = Role.get_by_id(role_id).cast_member
        return model_to_dict(cast_member)
    except peewee.DoesNotExist:
        return False


def get_random_cast(limit: int) -> list:
    """returns a random castmember"""
    cast_member = Cast.select().order_by(fn.Random()).limit(limit)
    rand_member = [model_to_dict(member) for member in cast_member]
    return rand_member


################# Role queries #################
def add_role(
    full_name: str, birth_date: date, bio: str, photo_url: str, cast_id: int
) -> Union[int, bool]:
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


def get_roles(limit: int) -> list:
    """returns all roles"""
    if limit:
        query = Role.select().limit(limit)
    else:
        query = Role.select()

    roles = [model_to_dict(role) for role in query]
    return roles


def get_role_by_id(role_id: int) -> Union[dict, bool]:
    """returns a role by id"""
    try:
        role = Role.get_by_id(role_id)
        return model_to_dict(role)
    except peewee.DoesNotExist:
        return False


def get_roles_by_name(role_name: str, limit: int) -> list:
    """returns role(s) matching name"""
    if limit:
        query = Role.select().where(Role.full_name ** f"%{role_name}%").limit(limit)
    else:
        query = Role.select().where(Role.full_name ** f"%{role_name}%")

    roles = [model_to_dict(role) for role in query]
    return roles


def get_roles_by_cast(cast_id: int) -> list:
    """returns role(s) by castmember"""
    query = Cast.get_by_id(cast_id).roles
    roles = [model_to_dict(role) for role in query]
    return roles


def get_roles_by_song(song_id: int, limit: int) -> list:
    """returns role(s) by song"""
    if limit:
        query = query = Song.get_by_id(song_id).singers.limit(limit)
    else:
        query = Song.get_by_id(song_id).singers

    roles = [model_to_dict(role) for role in query]
    return roles


def get_random_role(limit: int) -> list:
    """returns a random role"""
    role = Role.select().order_by(fn.Random()).limit(limit)
    rand_roles = [model_to_dict(x) for x in role]
    return rand_roles


################# Song queries #################
def add_song(
    title: str, lyrics: str, duration_in_seconds: int, role_ids: list
) -> Union[int, bool]:
    """adds a song to database"""
    try:
        new_song = Song.create(
            title=title,
            lyrics=lyrics,
            duration_in_seconds=duration_in_seconds,
        )
        new_song.save()

        new_song.singers.add(Role.select().where(Role.role_id << role_ids))
        new_song.save()
        return new_song.song_id
    except peewee.PeeweeException:
        return False


def get_songs(limit: int) -> list:
    """returns all songs"""
    if limit:
        query = Song.select().limit(limit)
    else:
        query = Song.select()

    songs = [model_to_dict(song) for song in query]
    return songs


def get_song_by_id(song_id: int) -> Union[dict, bool]:
    """returns a song by id"""
    try:
        song = Song.get_by_id(song_id)
        return model_to_dict(song)
    except peewee.DoesNotExist:
        return False


def get_songs_by_title(song_title: str, limit: int) -> list:
    """returns songs(s) matching title"""
    if limit:
        query = Song.select().where(Song.title ** f"%{song_title}%").limit(limit)
    else:
        query = Song.select().where(Song.title ** f"%{song_title}%")
    songs = [model_to_dict(song) for song in query]
    return songs


def get_songs_by_role(role_id: int, limit: int) -> list:
    """returns song(s) by role"""
    if limit:
        query = Role.get_by_id(role_id).songs.limit(limit)
    else:
        query = Role.get_by_id(role_id).songs

    songs = [model_to_dict(song) for song in query]
    return songs


def get_random_song(limit: int) -> list:
    """returns a random song"""
    song = Song.select().order_by(fn.Random()).limit(limit)
    rand_songs = [model_to_dict(x) for x in song]
    return rand_songs


################# Musical query #################
def add_musical_info(
    title: str, synopsis: str, release_year: date, poster_url: str
) -> Union[Musical_info, bool]:
    """adds musical info to database"""
    try:
        return Musical_info.create(
            title=title,
            synopsis=synopsis,
            release_year=release_year,
            poster_url=poster_url,
        )
    except peewee.PeeweeException:
        return False


def get_musical_info() -> Union[dict, bool]:
    """returns general musical info"""
    try:
        musical_info = Musical_info.get_by_id(1)
        return model_to_dict(musical_info)
    except peewee.DoesNotExist:
        return False
