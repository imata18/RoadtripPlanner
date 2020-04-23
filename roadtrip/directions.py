import requests

def get_directions_api(fromLocation, toLocation):
    #parameters = {"q": city, "appid": "5a379190bfc2627d0c791dc5ab8565f7"}
    fromState = "MA"
    fromCity = "Boston"
    fromStreetName = "Pike+Street"
    fromNumber = "1200"
    toState = "TX"
    toCity = "Houston"
    toStreetName = "Reed+Rd"
    toNumber = "2400"
    mapQuestKey = "YbLPlxGYgw8hjtfRJ289cHgHROVXMCvz"
    directions = requests.get("http://open.mapquestapi.com/directions/v2/route?key="+mapQuestKey+"&from="+fromNumber+",+"+fromStreetName+",+"+fromCity+",+"+fromState+"&to="+toNumber+"+"+toStreetName+",+"+toCity+",+"+toState) #, params=parameters)
    #description = weather.json()["weather"][0]["description"]
    #temp = weather.json()["main"]["temp"] - 273.15
    #humidity = weather.json()["main"]["humidity"]
    mapping = directions.json()["route"]
    return mapping

print(get_directions_api("hi","hey"))