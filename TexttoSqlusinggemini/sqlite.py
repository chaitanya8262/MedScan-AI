import sqlite3

## connect to the sqlite database

connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table

cursor = connection.cursor()

## create the table
table_info ="""
Create table STUDENT(Name varchar(25), Class varchar(25), Section varchar(25));
"""

cursor.execute(table_info)

## Insert some more Records

cursor.execute("""Insert Into STUDENT values('Krish', 'Data Science', 'A') """)
cursor.execute("""Insert Into STUDENT values('Sudhashu', 'ML', 'B') """)
cursor.execute("""Insert Into STUDENT values('Ripesh', 'AI Enginner', 'C') """)
cursor.execute("""Insert Into STUDENT values('Sunny', 'Data Science', 'D') """)
cursor.execute("""Insert Into STUDENT values('Dish', 'Data Science', 'A') """)


## Display  All records

print("The Inserted records are")
data = cursor.execute(''' Select * from STUDENT''')
for row in data:
    print(row)