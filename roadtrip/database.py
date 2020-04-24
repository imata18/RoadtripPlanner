import mysql.connector
import codecs
from roadtrip.directionyelp import *
from roadtrip.yelp import get_hotel_name
from roadtrip.weather import get_weather_api

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Mrkang15",
  database="roadtrip"
)

mycursor = mydb.cursor()

def check_credential(username, password):
    try:
        mycursor.execute("select password from security where username='" + username+"'")
        pw = mycursor.fetchone()[0]
        if pw == password:
            return True
        else:
            return False
    except:
        return False

def add_user(username, password):
    try:
        mycursor.execute("select password from security where username='" + username+"'")
        pw = mycursor.fetchone()[0]
        return False
    except:
        mycursor.execute("insert into security (username, password) values ('"+username+"','"+password+"')")
        mydb.commit()
        return True


def user_info(username):
    try:
        mycursor.execute("select * from " + username)
        result = "<h1>Your Roadtrip Plan</h1><br>"
        plan = mycursor.fetchall()
        for i in range(len(plan)):
            result += "On day"+str(i+1)+", you will stop in "+plan[i][2]+ ". The weather is " + plan[i][1] + ". You will stay at " + plan[i][0] + ".<br>"
        result += "<form action='/replan'><button type='submit'>plan a new trip</button></form>"
        return result
    except:
        mycursor.execute("CREATE TABLE IF NOT EXISTS " + username + " (hotel VARCHAR(255), weather VARCHAR(255), location VARCHAR(255))")
        file = codecs.open("plan.html", "r", "utf-8")
        return file.read()

def get_hotels(stops):
    result = []
    for location in stops:
        result.append(get_hotel_name(location))
    return result

def get_weather(stops):
    result = []
    for location in stops:
        city = location.split(",")[0]
        result.append(get_weather_api(city))
    return result

def get_stops(fstreet, fcity, fstate, dstreet, dcity, dstate):
    r = get_directions_api(fstreet, fcity, fstate, dstreet, dcity, dstate)
    return getlocation(r)

def user_plan(user, fstreet, fcity, fstate, dstreet, dcity, dstate):
    stops = get_stops(fstreet, fcity, fstate, dstreet, dcity, dstate)
    hotels = get_hotels(stops)
    weathers = get_weather(stops)
    mycursor.execute("delete from " + user)
    for i in range(len(hotels)):
        mycursor.execute(
            "insert into " + user + " (hotel, weather, location) values ('" +
            hotels[i] + "', '" + weathers[i] + "', '" + stops[i] + "')"
        )
    mydb.commit()
    return user_info(user)


