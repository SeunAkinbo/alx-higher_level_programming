#!/usr/bin/python3
'''Module 0-select_states'''

import MySQLdb
import sys


def states(username, password, name):
    '''The script lists all states from the database hbtn_0e_0_usa
        Args - sql username, sql password, database name
    '''
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    ''' The main name check '''
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    states(username, password, database)
