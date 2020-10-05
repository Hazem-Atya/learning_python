import sqlite3
import re

conn = sqlite3.connect("testsql.sqllite")
cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('CREATE TABLE Counts (email TEXT , count INTEGER)')

fh = open("mbox-short.txt")
data = fh.read()
emails = re.findall("\nFrom: (.*)", data)
print(emails)

for email in emails:
    cur.execute("SELECT count From Counts WHERE email=?", (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute("INSERT INTO Counts (email,count) VALUES (?,1)", (email,))
    else:
        cur.execute("UPDATE Counts SET count = count+1 WHERE email= ?", (email,))
    conn.commit()

sqlstm = "SELECT email ,count FROM Counts ORDER BY Count DESC LIMIT 10"
for row in cur.execute(sqlstm):
   print(row)