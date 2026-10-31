import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

url="https://api.open-meteo.com/v1/forecast"
params={
    "latitude":float(os.getenv("CITY_LAT")),
    "longitude":float(os.getenv("CITY_LON")),
    "current":
"temperature_2m,wind_speed_10m",
    "daily":
"temperature_2m_max,temperature_2m_min",
    "timezone":"Asia/Shanghai",
    "forecast_days":5,
}

response=requests.get(url,params=params)
print(response.status_code)

data=response.json()
#print(json.dumps(data,ensure_ascii=False,indent=2))

temperature = data["current"]["temperature_2m"]
wind_speed = data["current"]["wind_speed_10m"]
print(f"现在{temperature}度，风速{wind_speed}")

i=0
for date in data["daily"]["time"]:
    temperature_max = data["daily"]["temperature_2m_max"][i]
    temperature_min = data["daily"]["temperature_2m_min"][i]
    print(f"{date}最低{temperature_min}度，最高{temperature_max}度")
    i=i+1