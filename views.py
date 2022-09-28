import json
import sqlite3
from flask import Flask

app = Flask(__name__)


def get_data(sql):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row

        result = connection.execute(sql).fetchall()
    return result


@app.get("/movie/<title>")
def step_1(title):
    result = {}
    for item in get_data(sql=f'''
            select title, country, release_year, genre, description
            from netflix
            where title = '{title}'
            order by release_year desc
            limit 1
            '''):
        result = dict(item)

        return app.response_class(
            json.dumps(result, ensure_ascii=True, indent=4),
            mimetype="application/json",
            status=200
        )


@app.get("/movie/<int:year1>/to/<int:year2>/")
def step_2(year1, year2):
    # result = {}
    sql = f'''select * from netflix
    where release_year between {year1} and {year2}
    limit 100'''
    result = []

    for item in get_data(sql):
        result.append(
            dict(item)
        )

    return app.response_class(
        json.dumps(result, ensure_ascii=True, indent=4),
        mimetype="application/json",
        status=200
    )


@app.get("/rating/<rating>/")
def step_3(rating):
    my_rating = {
        "children": ('G', 'G'),
        "family": ('G', 'PG', 'PG-13'),
        "adult": ('R', 'NC-17')
    }
    sql = f'''select * from netflix
    where rating in {my_rating.get(rating, ('PG', 'NC-17'))}'''
    result = []

    for item in get_data(sql):
        result.append(
            dict(item)
        )

    return app.response_class(
        json.dumps(result, ensure_ascii=True, indent=4),
        mimetype="application/json",
        status=200
    )


@app.get("/genre/<genre>/")
def step_4(genre):
    sql = f'''select show_id, type from netflix
    where listed_in like '%{str(genre).title()}%'
    '''
    result = []

    for item in get_data(sql):
        result.append(
            dict(item)
        )

    return app.response_class(
        json.dumps(result, ensure_ascii=True, indent=4),
        mimetype="application/json",
        status=200
    )


def step_5(name1, name2):
    sql = f'''select "cast" from netflix
        where "cast" like '%{str(name1).title()}%' and '%{str(name2).title()}%'
        '''
    names_dict = {}

    for item in get_data(sql):
        result = dict(item)

        names = set(result.get('cast').split(', ')) - {name1, name2}

        for name in names:
            names_dict[name.strip()] = names_dict.get(name.strip(), 0) + 1

    for key, value in names_dict.items():
        if value > 2:
            print(key)


def step_6(types, year, genre):
    sql = f'''
         select * from netflix
         where type = '{types}' and release_year = '{year}' and listed_in like '%{str(genre).title()}%'  
    '''

    result = []

    for item in get_data(sql):
        result.append(
            dict(item)
        )

    return json.dumps(result, indent=4)


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)

