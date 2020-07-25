import mysql.connector
import datetime
 
print(datetime.datetime.now())

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="face_recognition_temp"
)
 
print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO face_recognition_temp (name, temp, time) VALUES (%s, %s, %s)"
val = ("amy", "36.6", datetime.datetime.now())
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "success")

mycursor.execute("SELECT * FROM face_recognition_temp")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)