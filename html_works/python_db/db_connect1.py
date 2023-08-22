import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aruna@0704"

)
print(db)

cursor=db.cursor()

query="create database animal"
cursor.execute(query)