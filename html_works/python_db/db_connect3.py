import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aruna@0704",
    database="animal"
)

cursor=db.cursor()


query="""
insert into pets(age,gender,breed,location,price) values(20,'male','breed3','pampady','18000')
"""

cursor.execute(query)
db.commit()# save changes



