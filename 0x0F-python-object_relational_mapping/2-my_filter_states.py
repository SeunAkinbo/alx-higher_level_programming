#!/usr/bin/python3
'''Module 2-my_filter_states'''

import MySQLdb
import sys


def states(username, password, name, state_name):
    '''The script lists all states from the database hbtn_0e_0_usa
        Args - username, password, name, state_name
    '''
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=name)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            state_name)
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    ''' The main name check '''
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> \
                <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    states(username, password, database, state_name)
