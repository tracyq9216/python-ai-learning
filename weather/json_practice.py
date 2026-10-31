import json

# ===== 练习 1 =====
words ={"猫":"cat","狗":"dog",
        "苹果":"apple","太阳":"sun"}

with open("words.json","w",encoding="utf-8")as f:
    json.dump(words,f,ensure_ascii=False,indent=2)

with open("words.json","r",encoding="utf-8")as f:
    data = json.load(f)

print(data["苹果"])
print(type(data))

# ===== 练习 2 =====
weather = {
    "city":"上海",
    "current":{"temperature":18.5,
    "wind_speed":9.2},
    "daily":{"date":["10-27", "10-28","10-29"],
    "max_temp":[21.0,19.5,23.1]}
    }

with open("weather.json","w",encoding="utf-8")as f:
    json.dump(weather,f,ensure_ascii=False,indent=2)

with open("weather.json","r",encoding="utf-8")as f:
    weather = json.load(f)

print(weather["current"]["temperature"])
print(weather["daily"]["max_temp"][1])
print(type(weather["current"]["temperature"]))

i=0
for date in weather["daily"]["date"]:
    max_temp = weather["daily"]["max_temp"][i]
    print(f"{date}最高{max_temp}度")
    i=i+1