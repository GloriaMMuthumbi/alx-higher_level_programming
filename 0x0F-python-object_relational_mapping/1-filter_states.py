#!/usr/bin/python3
"""Lists all states with name starting with uppercase N from database
Usage: ./1-filter_states.py <mysql username> \
                            <mysql password>
                            <databse name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3])
    mycursor = db.cursor()
    myscursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in mycursor.fetchall() if state[1][0] == "N"]
