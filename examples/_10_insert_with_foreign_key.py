import sqlite3

db = sqlite3.connect('library_constraints.db')
db.execute("PRAGMA foreign_keys = 1")  # Important


query = """INSERT INTO book (
    author_id, title, isbn
) VALUES (
    :author_id, :title, :isbn
);"""


cursor = db.execute(query, {
    'title': 'The Raven',
    'author_id': 1, # Author doesn't exist---this is why we get an integrity error
    'isbn': 'TR1'
})

print(cursor)
# author_id is a foreign key in the book table. author_id 100 does not exist in the author table

db.commit()
