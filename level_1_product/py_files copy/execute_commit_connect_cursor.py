import sqlite3


server = sqlite3.connect("my_sql//sql.db")

# if we don't want to make a file on the disk we can make it on memory by this code ----> server.sqlite3.connect(:memory:)

cursor = server.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               id TEXT PRIMARY KEY,
               name TEXT,
               last_name TEXT,
               gender TEXT);
               """)

cursor.execute("""CREATE TABLE orders(
               order_id TEXT PRIMARY KEY,
               date TEXT,
               user_id TEXT,
               total TEXT);
               """)
data = ("00001", "arvin", "behbahani", "-female")
cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?);", data)


server.commit()
