#!/usr/bin/python3
"""Takes in an argument and displays all values in states table
of database where name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]).strip("'"))
    [print(state) for state in c.fetchall()]
