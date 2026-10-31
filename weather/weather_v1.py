import requests


def get_weather(lat,lon):
    url="https://api.open-meteo.com/v1/forecast"
    params={
        "latitude":lat,
        "longitude":lon,
        "current":
    "temperature_2m,wind_speed_10m",
        "daily":
    "temperature_2m_max,temperature_2m_min",
        "timezone":"Asia/Shanghai",
        "forecast_days":5,
    }

    try:
        response=requests.get(url,params=params,timeout=10)
    except requests.exceptions.RequestException:
        print("连不上天气网站，请检查网络")
        return None
    if response.status_code != 200:
        print(f"天气网站出错了，状态码：{response.status_code}")
        return None

    data=response.json()
    if "current" not in data:
        print("天气数据不完整")
        return None
    return data

def show_weather(data):
    temperature = data["current"]["temperature_2m"]
    wind_speed = data["current"]["wind_speed_10m"]
    print(f"现在{temperature}度，风速{wind_speed}")

    i=0
    for date in data["daily"]["time"]:
        temperature_max = data["daily"]["temperature_2m_max"][i]
        temperature_min = data["daily"]["temperature_2m_min"][i]
        print(f"{date}最低{temperature_min}度，最高{temperature_max}度")
        i=i+1

cities={
    "上海":{"lat":31.23,"lon":121.47},
    "北京":{"lat":39.90,"lon":116.40},
    "广州":{"lat":23.13,"lon":113.26},
}

def main():
    city=input("想查哪个城市？").strip()

    if city in cities:
        lat=cities[city]["lat"]
        lon=cities[city]["lon"]
        print(f"{city}的天气：")
        data=get_weather(lat,lon)
        if data is not None:
            show_weather(data)
    else:
        print(f"抱歉，还没有{city}的位置")


main()