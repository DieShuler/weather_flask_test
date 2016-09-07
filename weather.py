# b1u3c1ph3r's weather.py file
# OM Python - Week 3 

import forecastio
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Opted to set the API key here since it was easier than trying
# to push it over from live_slackbot.py
api_key=os.environ.get('WEATHER_API_KEY')

def get_location(user_location):
    geolocator = Nominatim()
    # Check to make sure an actual string is passed to the locator
    if user_location == "":
        return None
    else:
        location = geolocator.geocode(user_location)
        return location

def get_weather(req_location):
    location = get_location(req_location)
    if location == None:
        # Making sure to return something in case the user doesn't supply a location
        weather_return = "I have no idea where that is."
    else:
        forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
        weather_return = "The weather in {} is: {} and {} degrees".format(location,
                            forecast.summary, forecast.temperature)
    return weather_return
