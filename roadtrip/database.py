import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="Mrkang15",
  database="roadtrip"
)

mycursor = mydb.cursor()

def add_current_weather(city, temp):
    mycursor.execute("insert into weather (city, temperature) values ('"+city+"',"+str(temp)+")")
    mydb.commit()

def get_current_weather_database(city):
    mycursor.execute("select temperature from weather where city='"+city+"'")
    result = mycursor.fetchone()
    if result == None:
        return None
    else:
        return result[0]

