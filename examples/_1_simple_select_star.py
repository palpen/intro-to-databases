import sqlite3

# makes a connection to a database
db = sqlite3.connect('library_simple.db')
print(db)
print(dir(db))

# returns an object that you can iterate over
cursor = db.execute("SELECT * FROM author")
print(cursor, type(cursor))
print(dir(cursor))

# print("Authors:")
for row in cursor:
    print(row)
