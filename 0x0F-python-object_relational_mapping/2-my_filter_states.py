#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                            <database name> \
                            <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' \
        ORDER BY id ASC".format(sys.argv[4]))
    for state in cursor.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
