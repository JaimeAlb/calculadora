import MySQLdb

db = MySQLdb.connect(host="academiachicureo.cl",
                     user="academia_jaime",         # your username
                     passwd="f+oY5**v3}Q}",  # your password
                     db="academia_jaime")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM usuarios")

# print all the first cell of all the rows
for row in cur.fetchall():
    print (row)

db.close()
