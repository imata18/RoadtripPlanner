import requests

mapQuestKey = "YbLPlxGYgw8hjtfRJ289cHgHROVXMCvz"

def get_directions_api(fromAddress, fromCity, fromState, toAddress, toCity, toState):
    #parameters = {"q": city, "appid": "5a379190bfc2627d0c791dc5ab8565f7"}
    fromAddressPlus = fromAddress.replace(" ","+")
    toAddressPlus = toAddress.replace(" ","+")
    
    fromAddressInput = fromAddress + "+" + fromCity + "+" + fromState
    toAddressInput = toAddress + "+" + toCity + "+" + toState

    #directions = requests.get("http://open.mapquestapi.com/directions/v2/route?key="+mapQuestKey+"&from="+fromNumber+",+"+fromStreetName+",+"+fromCity+",+"+fromState+"&to="+toNumber+"+"+toStreetName+",+"+toCity+",+"+toState) #, params=parameters)
    directions = requests.get("http://open.mapquestapi.com/directions/v2/route?key="+mapQuestKey+"&from="+fromAddressInput+"&to="+toAddressInput)
    
    sumDistance = 0
    locationStops = []
    mapping = directions.json()["route"]
    mappingDistance = directions.json()["route"]["legs"][0]["maneuvers"]
    #mappingDistance = directions.json()["route"]["legs"][0]["maneuvers"][0]["startPoint"]['lat']
    for i in range(len(mappingDistance)):
        sumDistance+=mappingDistance[i]["distance"]
        if sumDistance > 520:
            sumDistance = 0
            locationStops.append([str(mappingDistance[i]["startPoint"]["lat"]) + ", " + str(mappingDistance[i]["startPoint"]["lng"])])
        if 460 < sumDistance < 520: 
            sumDistance = 0
            if i + 1 < len(mappingDistance):
                locationStops.append([str(mappingDistance[i+1]["startPoint"]["lat"]) + ", " + str(mappingDistance[i+1]["startPoint"]["lng"])])
    return locationStops

def getlocation(r):
    locationtotal = []
    for i in r:
        stringInput = i[0].replace(" ","")
        #print(i[0])
        #i[0].replace(" ","")
        #print(stringInput)
        locations = requests.get("http://open.mapquestapi.com/geocoding/v1/reverse?key="+mapQuestKey+"&location="+stringInput+"&includeRoadMetadata=true&includeNearestIntersection=true")
        parsedCity = locations.json()["results"][0]["locations"][0]["adminArea5"]
        parsedState = locations.json()["results"][0]["locations"][0]["adminArea3"]
        cityAndState = str(parsedCity) + ", " + str(parsedState)
        locationtotal.append(cityAndState)
    return locationtotal


