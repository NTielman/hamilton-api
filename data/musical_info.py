from datetime import datetime
from setup.services import add_musical_info

hamilton_musical = {
    "title": "Hamilton",
    "synopsis": """Hamilton details Alexander Hamilton's life in two acts, along with how various historical figures influenced his life, including the Marquis de Lafayette, Aaron Burr, John Laurens, Hercules Mulligan, Elizabeth Schuyler Hamilton, Angelica Schuyler Church, Peggy Schuyler, Philip Hamilton, Maria Reynolds, George Washington, James Madison, and Thomas Jefferson""",
    "category": "Musical",
    "genre": "Historical, Biographical",
    "release_year": "20 Jan 2015",
    "poster_url": "https://upload.wikimedia.org/wikipedia/en/8/83/Hamilton-poster.jpg",
}


def add_general_info(musical_info):
    add_musical_info(
        title=musical_info["title"],
        synopsis=musical_info["synopsis"],
        release_year=datetime.strptime(musical_info["release_year"], "%d %b %Y"),
        poster_url=musical_info["poster_url"],
        category=musical_info["category"],
        genre=musical_info["genre"],
    )
