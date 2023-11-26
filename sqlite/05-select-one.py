import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor =con.cursor()
    cursor.execute("SELECT * from usuarios")
    print(cursor.fetchone())# selecciona un solo registro del bbdd
    print(cursor.fetchall())# selecciona todo los registro del BBDD
