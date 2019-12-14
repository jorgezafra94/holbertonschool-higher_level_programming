#!/usr/bin/python3
"""
here we are going to connect to a database and realize a
query
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         port=3306, passwd=sys.argv[2], db=sys.argv[3],
                         charset="utf8")
    query = db.cursor()
    query.execute("SELECT * FROM states ORDER BY id ASC")
    output = query.fetchall()
    for i in output:
        if (i[1][0] == 'N'):
            print(i)
    query.close()
    db.close()
