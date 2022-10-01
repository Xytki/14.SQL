import sqlite3


def get_data(sql):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row

        result = connection.execute(sql).fetchall()
    return result


def get_release_year(year1, year2):
    result = []
    for item in get_data(sql=f'''SELECT * 
                    FROM netflix 
                    WHERE `type`='Movie' 
                    and release_year between {year1} and {year2} 
                    LIMIT 100 '''):
        result.append(dict(item))
    return result


