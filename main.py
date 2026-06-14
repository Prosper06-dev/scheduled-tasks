import requests
import os
from twilio.rest import Client

OWM_api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": os.environ.get("ISOLO_LAT"),
    "lon": os.environ.get("ISOLO_LONG"),
    "appid": OWM_api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for time_stamp in weather_data["list"]:
    if time_stamp["weather"][0]["id"] < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="\nIt's going to rain today. Remember to bring an Umbrella 🌂",
        from_="+15863105290",
        to="+2347033912091",
    )
    print(message.status)
