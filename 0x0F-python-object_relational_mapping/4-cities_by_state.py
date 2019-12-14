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
    query.execute("SELECT cities.id, cities.name, states.name FROM cities\
                 LEFT JOIN states ON states.id = cities.state_id\
                 ORDER BY cities.id ASC")
    output = query.fetchall()
    for i in output:
        print(i)
    query.close()
    db.close()
