from models import create_tables
from services import add_cast, add_musical_info, add_role, add_song
from datetime import datetime


def add_cast_members(cast_members):
    for cast_member in cast_members:
        cast_id = add_cast(
            full_name=cast_member["full_name"],
            birth_date=datetime.strptime(cast_member["birth_date"], "%d %b %Y"),
            bio=cast_member["bio"],
            photo_url=cast_member["photo_url"],
        )
        cast_member["cast_id"] = cast_id


def add_roles(roles):
    for role in roles:
        role_id = add_role(
            full_name=role["full_name"],
            birth_date=datetime.strptime(role["birth_date"], "%d %b %Y"),
            bio=role["bio"],
            photo_url=role["photo_url"],
            cast_id=role["cast_member"]["cast_id"],
        )
        role["role_id"] = role_id


def add_songs(songs):
    for song in songs:
        singers = []
        for singer in song["singers"]:
            singers.append(singer["role_id"])

        add_song(
            title=song["title"],
            lyrics=song["lyrics"],
            duration_in_seconds=song["duration_in_seconds"],
            role_ids=singers,
        )


def add_general_info(musical_info):
    success = add_musical_info(
        title=musical_info["title"],
        synopsis=musical_info["synopsis"],
        release_year=datetime.strptime(musical_info["release_year"], "%d %b %Y"),
        poster_url=musical_info["poster_url"],
    )
    print(success)


def add_db_data():
    create_tables()
    add_cast_members(cast_members)
    add_roles(roles)
    add_songs(songs)
    add_general_info(hamilton_musical)


description = """
The Hamilton Musical API for all your Hamilton fan needs. Contains information on the cast, musical tracks and roles. 🎭

## General

**read** general information about the musical

## Cast

**search and read** cast info

## Roles / Parts

**search and read** about the different roles

## Songs / Tracks

**search and read** about the different tracks the musical is comprised of

"""

tags_metadata = [
    {
        "name": "general",
        "description": "General information on the Hamilton musical",
    },
    {
        "name": "cast",
        "description": "Information on the cast members, actors and crew who worked in or on the Hamilton musical",
    },
    {
        "name": "roles",
        "description": "Description of the different characters, roles and parts that appear in the Hamilton musical",
    },
    {
        "name": "songs",
        "description": "Information on the different tracks the Hamilton musical is comprised of",
    },
]
