import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="Mrkang15",
  database="roadtrip"
)

mycursor = mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
  print(i)

