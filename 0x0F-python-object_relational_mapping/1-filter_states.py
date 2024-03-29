#!/usr/bin/python3
"""Lists all states with name starting with uppercase N from database
Usage: ./1-filter_states.py <mysql username> \
                            <mysql password>
                            <databse name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM `states` ORDER BY `id`""")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
