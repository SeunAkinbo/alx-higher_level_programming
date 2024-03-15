#!/usr/bin/python3
'''Module 0-select_states'''

import MySQLdb
import sys


def states(username, password, name, searched):
    '''The script lists all states from the database hbtn_0e_0_usa
        Args - username, password, name, searched
    '''
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=name)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (searched,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    ''' The main name check '''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]
    states(username, password, database, searched)
