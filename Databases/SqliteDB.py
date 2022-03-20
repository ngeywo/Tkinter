import sqlite3

conn= sqlite3.connect("Music.sqlite")
cur= conn.cursor()


cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (tittle TEXT, plays INTEGER)')


cur.execute('INSERT INTO Tracks (tittle,plays) VALUES (?,?)', ("Niko sawa", 2))
cur.execute('INSERT INTO Tracks (tittle,plays) VALUES (?,?)', ("Pombe",23))

conn.commit()

print("Tracks: ")
cur.execute('SELECT * FROM Tracks')

for row in cur:
	print(row)
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()
conn.close()