import requests

def get_directions_api(fromAddress, fromCity, fromState, toAddress, toCity, toState):
    #parameters = {"q": city, "appid": "5a379190bfc2627d0c791dc5ab8565f7"}
    
    #fromState = "MA"
    #fromCity = "Boston"
    #fromStreetName = "Pike+Street"
    #fromNumber = "1200"
    #toState = "TX"
    #toCity = "Houston"
    #toStreetName = "Reed+Rd"
    #toNumber = "2400"
    
    fromAddressPlus = fromAddress.replace(" ","+")
    toAddressPlus = toAddress.replace(" ","+")
    
    fromAddressInput = fromAddress + "+" + fromCity + "+" + fromState
    toAddressInput = toAddress + "+" + toCity + "+" + toState
    
    mapQuestKey = "YbLPlxGYgw8hjtfRJ289cHgHROVXMCvz"
    #directions = requests.get("http://open.mapquestapi.com/directions/v2/route?key="+mapQuestKey+"&from="+fromNumber+",+"+fromStreetName+",+"+fromCity+",+"+fromState+"&to="+toNumber+"+"+toStreetName+",+"+toCity+",+"+toState) #, params=parameters)
    directions = requests.get("http://open.mapquestapi.com/directions/v2/route?key="+mapQuestKey+"&from="+fromAddressInput+"&to="+toAddressInput)
    #description = weather.json()["weather"][0]["description"]
    #temp = weather.json()["main"]["temp"] - 273.15
    #humidity = weather.json()["main"]["humidity"]
    
    sumDistance = 0
    mapping = directions.json()["route"]
    mappingDistance = directions.json()["route"]["legs"][0]["maneuvers"]
    #mappingDistance = directions.json()["route"]["legs"][0]["maneuvers"][0]["startPoint"]['lat']
    for i in range(len(mappingDistance)):
        sumDistance+=mappingDistance[i]["distance"]
        if sumDistance > 520:
            sumDistance = 0
            return  str(mappingDistance[i]["startPoint"]["lat"]) + ", " + str(mappingDistance[i]["startPoint"]["lng"])
        if 460 < sumDistance < 520: 
            sumDistance = 0
            if i + 1 < len(mappingDistance):
                return str(mappingDistance[i+1]["startPoint"]["lat"]) + ", " + str(mappingDistance[i+1]["startPoint"]["lng"])
    #return mappingDistance

print(get_directions_api("1200 Pike Street", "Boston", "MA", "2400 Reed Road", "Houston", "TX"))