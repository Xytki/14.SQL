import sqlite3

con = sqlite3.connect('netflix.db')
cur = con.cursor()

sqlite_query = ("SELECT * "
                "FROM netflix "
                "WHERE `type`='Movie' "
                "ORDER BY listed_in DESC ")


cur.execute(sqlite_query)
results = cur.fetchall()
# for i in results:
#     print(i)
con.close()


def get_genre(genre):
    data_genre = [][:11]
    for result in results:
        if result[11] == genre:
            data_genre.append({
                "title": result[2],
                "description": result[12]
            })

    return data_genre


if __name__ == '__main__':
    print(get_genre('Thrillers'))
