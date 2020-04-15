import codecs
from flask import Flask, request
from roadtrip.weather import get_current_weather_api
from roadtrip.database import get_current_weather_database, add_current_weather


app = Flask(__name__)


@app.route("/")
def homepage():
    file = codecs.open("homepage.html", "r", "utf-8")
    return file.read()


@app.route("/cityweather", methods=["POST"])
def cityweather():
    city = request.form["city"]
    temp = 0
    if get_current_weather_database(city) is not None:
        temp = get_current_weather_database(city)
    else:
        temp = get_current_weather_api(city)
        add_current_weather(city, temp)
    result = "<h1>"+city+"'s weather</h1>" "<h3>Temperature(Celsius):</h3>" + str(temp)
    return result


if __name__ == "__main__":
    app.run()
