import mysql.connector
import codecs

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
            result += "day"+str(i+1)+": weather: " + plan[i][1] + " stay at: " + plan[i][0] + "<br>"
        result += "<form action='/replan'><button type='submit'>plan a new trip</button></form>"
        return result
    except:
        mycursor.execute("CREATE TABLE IF NOT EXISTS " + username + " (hotel VARCHAR(255), weather VARCHAR(255))")
        file = codecs.open("plan.html", "r", "utf-8")
        return file.read()

def get_hotels(stops):
    return ["sunny", "sunny", "cloudy"]

def get_weather(stops):
    return ["four seasons", "holiday inn", "hilton"]

def get_stops(start, dest):
    return []

def user_plan(user, start, dest):
    stops = get_stops(start, dest)
    hotels = get_hotels(stops)
    weathers = get_weather(stops)
    mycursor.execute("delete from " + user)
    for i in range(len(hotels)):
        mycursor.execute(
            "insert into " + user + " (hotel, weather) values ('" + hotels[i] + "', '" + weathers[i] + "')")
    mydb.commit()
    return user_info(user)
