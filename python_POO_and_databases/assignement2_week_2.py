import sqlite3
import re

conn = sqlite3.connect("assignement_week2.sqlite")
cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fh = open("mbox.txt")
data = fh.read()
orgs = re.findall("\nFrom: .*@(.*)", data)
print(orgs)

for org in orgs:
    cur.execute("SELECT count From Counts WHERE org=?", (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (org,count) VALUES (?,1)", (org,))
    else:
        cur.execute("UPDATE Counts SET count = count+1 WHERE org= ?", (org,))

conn.commit()
sqlstm = "SELECT org ,count FROM Counts ORDER BY Count DESC LIMIT 10"
for row in cur.execute(sqlstm):
   print(row)