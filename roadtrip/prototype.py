import codecs
from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route("/")
def homepage():
    file = codecs.open("homepage.html", "r", "utf-8")
    return file.read()


@app.route("/cityweather", methods=["POST"])
def cityweather():
    city = request.form["city"]
    parameters = {"q": city, "appid": "5a379190bfc2627d0c791dc5ab8565f7"}
    weather = requests.get("http://api.openweathermap.org/data/2.5/weather", params=parameters)
    description = weather.json()["weather"][0]["description"]
    temp = weather.json()["main"]["temp"] - 273.15
    humidity = weather.json()["main"]["humidity"]
    result = "<h1>"+city+"'s weather</h1>" + "<h3>Description:</h3>" + description + "<h3>Temperature(Celsius):</h3>" + str(temp) + "<h3>Humidity:</h3>" + str(humidity)
    return result


if __name__ == "__main__":
    app.run()
