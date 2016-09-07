# b1u3c1ph3r's weather.py file
# OM Python - Week 3 

import forecastio
from geopy.geocoders import Nominatim
import os

# Opted to set the API key here since it was easier than trying
# to push it over from live_slackbot.py
api_key=os.environ.get('WEATHER_API_KEY')

def get_location(user_location):
    geolocator = Nominatim()
    # Check to make sure an actual string is passed to the locator
    if user_location == "":
        return None
    else:
        try:
            location = geolocator.geocode(user_location, timeout=10)
            return location
        except GeocoderTimedOut as e:
            return None

def get_weather(req_location):
    location = get_location(req_location)
    if location == None:
        # Making sure to return something in case the Geocoder times out
        weather_return = "The super secret squirrel locator is sleeping right now.  Check back in a bit."
    else:
        forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
        weather_return = "The weather in {} is: {} and {} degrees".format(location,
                            forecast.summary, forecast.temperature)
    return weather_return
