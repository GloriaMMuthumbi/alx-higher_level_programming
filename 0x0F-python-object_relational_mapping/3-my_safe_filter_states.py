#!/usr/bin/python3
"""Lists all states in the database.
Where the state matches the arguments
Usage: ./3-my_safe_filter_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM `states`""")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
