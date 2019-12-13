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
    state = sys.argv[4]
    query.execute("SELECT cities.id, cities.name, states.name FROM cities\
                 LEFT JOIN states ON states.id = cities.state_id;\
                 ORDER BY cities.id ASC;")
    output = query.fetchall()
    aux = ""
    result = ""
    for i in output:
        if (i[2] == state):
            result = result + aux + i[1]
            aux = ", "
    print(result)
