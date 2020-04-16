import json
from pathlib import Path

movies = [
    {
        "id": 1,
        "title": "Inception",
        "year": 2016
    },
    {
        "id": 2,
        "title": "Shutter Island",
        "year": 2015
    },
]
# write into json file
data = json.dumps(movies)
Path("movies.json").write_text(data)

# read from json file
read_data = Path("movies.json").read_text()
movies = json.loads(read_data)
print(movies[1]["title"])
