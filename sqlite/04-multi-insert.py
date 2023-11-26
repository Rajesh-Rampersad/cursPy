import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor =con.cursor()
    usuarios = [
        (2, "Cochinito alegre"),
        (3, "Cochinito triste"),
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )