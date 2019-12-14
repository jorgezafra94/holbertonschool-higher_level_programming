#!/usr/bin/python3
"""
here we are going to connect to a database and realize a
query

"""
import sys
import MySQLdb


if __name__ == "__main__":
    if (len(sys.argv) == 4):
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             charset="utf8")
        query = db.cursor()
        query.execute("SELECT * FROM states ORDER BY id ASC")
        out = query.fetchall()
        for i in out:
            print(i)
        query.close()
        db.close()
