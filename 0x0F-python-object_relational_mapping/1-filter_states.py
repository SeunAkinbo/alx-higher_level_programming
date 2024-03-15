#!/usr/bin/python3
'''Module 1-filter_states'''

import MySQLdb
import sys


def states(username, password, name):
    '''The script lists all states from the database hbtn_0e_0_usa
        Args - username, password, name
    '''
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=name)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    ''' The main name check '''
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> \
                <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    states(username, password, database)
