from setup.models import create_tables
from data.acts import add_acts, acts
from data.cast import add_cast_members, cast_members
from data.roles import add_roles, roles
from data.songs import add_songs, songs
from data.musical_info import add_general_info, hamilton_musical


def add_db_data():
    create_tables()
    print("adding cast")
    add_cast_members(cast_members)
    print("adding acts")
    add_acts(acts)
    print("adding roles")
    add_roles(roles)
    print("adding songs")
    add_songs(songs)
    print("adding general")
    add_general_info(hamilton_musical)
    print("database created succesfully")


if __name__ == "__main__":
    add_db_data()
