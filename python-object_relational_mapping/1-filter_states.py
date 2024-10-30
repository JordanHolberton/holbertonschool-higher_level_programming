#!/usr/bin/python3

""" Lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    """ Lists all states from the database hbtn_0e_0_usa

        Usage: ./0-select_states.py <mysql username>
        <mysql password> <database name>

        Arguments:
            mysql username: username to connect the mySQL database
            mysql password: password to connect the mySQL database
            database name: name of the database to connect
        """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()
