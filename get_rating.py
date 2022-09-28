import sqlite3

con = sqlite3.connect('netflix.db')
cur = con.cursor()

sqlite_query = ("SELECT * "
                "FROM netflix "
                "WHERE `type`='Movie' "
                "AND rating != '' ")

cur.execute(sqlite_query)
results = cur.fetchall()
con.close()


def get_rating(res):
    data_rating = []
    for result in results:
        if result[8] in res:
            data_rating.append({
                "title": result[2],
                "rating": result[8],
                "description": result[12]
            })
    return data_rating


# if __name__ == '__main__':
#     print(get_rating(['PG', ]))
