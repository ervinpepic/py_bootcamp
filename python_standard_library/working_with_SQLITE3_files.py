import sqlite3
import json
from pathlib import Path

# Writing into database sqlite
# movies = json.loads(Path("movies.json").read_text())

# with sqlite3.connect("db.sqlite3") as connection:
#     sql = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         connection.execute(sql, tuple(movie.values()))
#     connection.commit()

# reading from database sqlite

with sqlite3.connect("db.sqlite3") as read_connection:
    read_sql = "SELECT * FROM MOVIES"
    cursor = read_connection.execute(read_sql)
    for row in cursor:
        print(row)
    movies = cursor.fetchall()
    print(movies) # of coruse we need to comment for loop 
