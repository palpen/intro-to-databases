import sqlite3

db = sqlite3.connect('library_simple.db')

# Row Factory:
# This is changing a setting in your database object
# it tells your db instance how to represent a row
# when you iterate over cursor. Previously it was just a
# tuple, now you can use column names to get info
db.row_factory = sqlite3.Row


cursor = db.execute("SELECT id, name FROM author")

print("Authors:")
for row in cursor:
    print(row, id(row))
    print("{id} - {name}".format(id=row['id'], name=row['name']))
