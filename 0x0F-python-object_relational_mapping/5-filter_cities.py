#!/usr/bin/python3

'''Module - 4-cities_by_states'''
import MySQLdb
import sys


def cities(username, password, db_name, state_name):
    '''A function that creates and queries a database
    Args: username, password, name
    '''

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name)

    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
               FROM states
               INNER JOIN cities ON states.id = cities.state_id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    '''The main name checker'''
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]

        cities(username, password, db_name, state_name)
    else:
        print("Usage: python <script.py> <username> \
                <password> <db_name> <state_name>")
        sys.exit(1)
