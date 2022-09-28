import sqlite3

con = sqlite3.connect('netflix.db')
cur = con.cursor()
sqlite_query = ("SELECT release_year, title "
                "FROM netflix "
                "WHERE `type`='Movie' "
                "ORDER BY release_year DESC "
                "LIMIT 100 ")

cur.execute(sqlite_query)
results = cur.fetchall()
con.close()


def get_release_year(ot, do):
    a = []
    for result in results:
        if ot <= result[0] <= do:
            a.append({"title": result[1], "release_year": result[0]})
    return a



