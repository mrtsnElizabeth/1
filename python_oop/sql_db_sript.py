import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cursor.execute("""CREATE TABLE Programmer
                  (First Name text, Last Name text, Email text,
                   Hired at text, Phone text, Salary Per Day text, Main Skill text)
               """)

cursor.execute("""CREATE TABLE Recruiter
                  (First Name text, Last Name text, Email text,
                   Hired at text, Phone text, Salary Per Day text)
               """)

cursor.execute("""CREATE TABLE Candidate
                  (First Name text, Last Name text, Email text,
                   Hired at text, Phone text, Main Skill text)
               """)

cursor.execute("""CREATE TABLE Vacancy
                  (Title text, Salary text, Main Skill text,
                   Technologies text, Fk '-' Recruiter text, Hired Candidate text, Status (open'/'closed) text)
               """)

cursor.execute("""CREATE TABLE Interview
                  (FK '-' vacancy text, FK '-' programmer text, FK '-' recruiter text,
                   FK '-' candidate text, 'Datetime' text, Feedback text, Result (hired'/'declined)
 text)
               """)

sql = """
INSERT INTO Programmer VALUES ('Dany', 'Karr', 'd_k@gmail.com', 'None', 'None', '50', 'None')
"""

sql = """
UPDATE Programmer SET Email='dany_k@gmail.com' WHERE First Name='Dany'
"""

sql = """SELECT * FROM Programmer"""
print(cursor.fetchall())

sql = """
DELETE FROM Programmer WHERE First Name='Dany'
"""

cursor.execute(sql)
conn.commit()
conn.close()
