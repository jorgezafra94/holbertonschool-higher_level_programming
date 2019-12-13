#!/usr/bin/python3
"""
here we are going to connect to a database and realize a
query
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         port=3306, passwd=sys.argv[2], db=sys.argv[3])
    query = db.cursor()
    x = sys.argv[4]
    query.execute("SELECT * FROM states WHERE name='{}';\
                  ORDER BY id ASC;".format(x))
    output = query.fetchall()
    for i in output:
        print(i)
