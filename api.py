import services
import uvicorn
import database
from fastapi import FastAPI, Path, HTTPException, Query
from typing import Optional


# database.add_db_data()  # comment out this line after db initialised
app = FastAPI(
    title="Hamilton API",
    description=database.description,
    version="0.0.1",
    contact={
        "name": "Nneka Tielman",
        "url": "https://ntielman.github.io/Portfolio/#contact",
        "email": "khalienne@gmail.com",
    },
    openapi_tags=database.tags_metadata,
)

################ GENERAL INFO ################
@app.get("/", tags=["general"])
def general_info():
    musical_info = services.get_musical_info()
    if not musical_info:
        raise HTTPException(status_code=404, detail="Info not found")
    return {"Data": musical_info}


################ CAST INFO ################
@app.get("/cast", tags=["cast"])
def get_all_cast_members(
    n: Optional[int] = Query(
        None, title="limit by n", description="Limit number of results to n results"
    )
):
    all_cast = services.get_cast(n)
    if not all_cast:
        raise HTTPException(status_code=404, detail="Cast not found")
    return {"Data": all_cast}


@app.get("/cast/id/{cast_id}", tags=["cast"])
def get_cast_member_by_id(
    cast_id: int = Path(
        ..., title="Cast ID", description="The ID of the cast member to get"
    )
):
    cast_member = services.get_cast_by_id(cast_id)
    if not cast_member:
        raise HTTPException(
            status_code=404, detail=f"Cast with id '{cast_id}' not found"
        )
    return {"Data": cast_member}


@app.get("/cast/name/{cast_name}", tags=["cast"])
def get_cast_members_by_name(
    cast_name: str = Path(
        ...,
        title="Cast Name",
        description="The first/full/last name of the cast member to get (case insensitive)",
    ),
    n: Optional[int] = Query(
        None, title="limit by n", description="Limit number of results to n results"
    ),
):
    cast_members = services.get_cast_by_name(cast_name, n)
    if not cast_members:
        raise HTTPException(
            status_code=404, detail=f"Cast with name '{cast_name}' not found"
        )
    return {"Data": cast_members}


@app.get("/cast/role/{role_id}", tags=["cast"])
def get_cast_members_by_role(
    role_id: int = Path(
        ..., title="Role ID", description="The ID of the role/part to get"
    )
):
    cast_members = services.get_cast_by_role(role_id)
    if not cast_members:
        raise HTTPException(
            status_code=404, detail=f"Cast with role Id '{role_id}' not found"
        )
    return {"Data": cast_members}


@app.get("/cast/random", tags=["cast"])
def get_random_cast_members(
    n: Optional[int] = Query(
        1, title="limit by n", description="Limit number of results to n results"
    )
):
    cast_members = services.get_random_cast(n)
    if not cast_members:
        raise HTTPException(status_code=404, detail="Random cast member not found")
    return {"Data": cast_members}


################# ROLES INFO ################
@app.get("/roles", tags=["roles"])
def get_all_roles(
    n: Optional[int] = Query(
        None, title="limit by n", description="Limit number of results to n results"
    )
):
    all_roles = services.get_roles(n)
    if not all_roles:
        raise HTTPException(status_code=404, detail="Roles not found")
    return {"Data": all_roles}


@app.get("/roles/id/{role_id}", tags=["roles"])
def get_role_by_id(
    role_id: int = Path(
        ..., title="Role ID", description="The ID of the role/part to get"
    )
):
    role_by_id = services.get_role_by_id(role_id)
    if not role_by_id:
        raise HTTPException(
            status_code=404, detail=f"Role with ID '{role_id}' not found"
        )
    return {"Data": role_by_id}


@app.get("/roles/name/{role_name}", tags=["roles"])
def get_roles_by_name(
    role_name: str = Path(
        ...,
        title="Role Name",
        description="The first/full/last name of the role/part to get (case insensitive)",
    ),
    n: Optional[int] = Query(
        None, title="limit by n", description="Limit number of results to n results"
    ),
):
    role = services.get_roles_by_name(role_name, n)
    if not role:
        raise HTTPException(
            status_code=404, detail=f"Roles with name '{role_name}' not found"
        )
    return {"Data": role}


@app.get("/roles/cast/{cast_id}", tags=["roles"])
def get_roles_by_cast_member(
    cast_id: int = Path(
        ..., title="Cast ID", description="The ID of the cast member to get"
    )
):
    role = services.get_roles_by_cast(cast_id)
    if not role:
        raise HTTPException(
            status_code=404, detail=f"Roles with Cast id '{cast_id}' not found"
        )
    return {"Data": role}


@app.get("/roles/song/{song_id}", tags=["roles"])
def get_roles_by_song(
    song_id: int = Path(
        ..., title="Song ID", description="The ID of the song/track to get"
    ),
    n: Optional[int] = Query(
        None, title="limit by n", description="Limit number of results to n results"
    ),
):
    role = services.get_roles_by_song(song_id, n)
    if not role:
        raise HTTPException(
            status_code=404, detail=f"Roles with Song id '{song_id}' not found"
        )
    return {"Data": role}


@app.get("/roles/random", tags=["roles"])
def get_random_roles(
    n: Optional[int] = Query(
        1, title="limit by n", description="Limit number of results to n results"
    )
):
    role = services.get_random_role(n)
    if not role:
        raise HTTPException(status_code=404, detail="Random roles not found")
    return {"Data": role}


################ SONGS INFO ################
@app.get("/songs", tags=["songs"])
def get_all_songs(
    n: Optional[int] = Query(
        None, title="limit by n", description="Limit number of results to n results"
    )
):
    songs = services.get_songs(n)
    if not songs:
        raise HTTPException(status_code=404, detail="Songs not found")
    return {"Data": songs}


@app.get("/songs/id/{song_id}", tags=["songs"])
def get_song_by_id(
    song_id: int = Path(
        ..., title="Song ID", description="The ID of the song/track to get"
    )
):
    song_by_id = services.get_song_by_id(song_id)
    if not song_by_id:
        raise HTTPException(
            status_code=404, detail=f"Song with ID '{song_id}' not found"
        )
    return {"Data": song_by_id}


@app.get("/songs/title/{song_title}", tags=["songs"])
def get_songs_by_title(
    song_title: str = Path(
        ...,
        title="Song Title",
        description="The title of the song/track to get (case insensitive)",
    ),
    n: Optional[int] = Query(
        None, title="limit by n", description="Limit number of results to n results"
    ),
):
    songs = services.get_songs_by_title(song_title, n)
    if not songs:
        raise HTTPException(
            status_code=404, detail=f"Songs with title '{song_title}' not found"
        )
    return {"Data": songs}


@app.get("/songs/role/{role_id}", tags=["songs"])
def get_songs_by_role(
    role_id: int = Path(
        ..., title="Role ID", description="The ID of the role/part to get"
    ),
    n: Optional[int] = Query(
        None, title="limit by n", description="Limit number of results to n results"
    ),
):
    songs = services.get_songs_by_role(role_id, n)
    if not songs:
        raise HTTPException(
            status_code=404, detail=f"Songs with Role id '{role_id}' not found"
        )
    return {"Data": songs}


@app.get("/songs/random", tags=["songs"])
def get_random_songs(
    n: Optional[int] = Query(
        1, title="limit by n", description="Limit number of results to n results"
    )
):
    songs = services.get_random_song(n)
    if not songs:
        raise HTTPException(status_code=404, detail="Random songs not found")
    return {"Data": songs}


if __name__ == "__main__":
    uvicorn.run(app)
