import sqlite3

con = sqlite3.connect('netflix.db')
cur = con.cursor()
sqlite_query = ("SELECT * "
                "FROM netflix "
                "WHERE type = 'Movie'"
                "ORDER BY title DESC ")

cur.execute(sqlite_query)
results = cur.fetchall()
con.close()


def get_info_films(title):
    for result in results:
        for i in result:
            if i == title:
                film_info = {
                    "title": result[2],
                    "country": result[5],
                    "release_year": result[7],
                    "genre": result[11],
                    "description": result[12]
                }
                return film_info


if __name__ == '__main__':
    print(get_info_films('1922'))

# Charming
