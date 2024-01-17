import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

MY_LAT = 53.258663
MY_LNG = -2.119287

TWILIO_URL = "https://www.twilio.com"
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_NUMBER_UK = os.getenv("TWILIO_NUMBER_UK")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": WEATHER_API_KEY
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
data = response.json()["list"]

will_rain = False
for hour_data in data:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Bring a brolly ☔",
        from_=TWILIO_NUMBER_UK,
        to='INSERT_HERE'
    )
