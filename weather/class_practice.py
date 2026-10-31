import requests

class Student:#类
    def __init__(self,name,age):
        self.name=name#属性
        self.age=age

    def introduce(self):#方法
        print(f"我叫{self.name}，今年{self.age}岁")
    def birthday(self):
        self.age=self.age+1
        print(f"生日快乐！现在{self.age}岁")

xiaoming=Student("小明",6)#对象
xiaohong=Student("小红",5)
xiaoling=Student("小玲",7)
xiaohong.age=6
xiaoming.introduce()
xiaoming.birthday()
xiaoming.birthday()
xiaoming.introduce()
xiaoling.introduce()
print(xiaohong.age)

# ===== 练习3 =====
class City:
    def __init__(self,name,lat,lon):
        self.name=name
        self.lat=lat
        self.lon=lon

    def show_weather(self):
        url="https://api.open-meteo.com/v1/forecast"
        params={
            "latitude":self.lat,
            "longitude":self.lon,
            "current":"temperature_2m",}
        response=requests.get(url,params=params)
        data=response.json()
        city=self.name
        temperature=data["current"]["temperature_2m"]
        print(f"{city}现在{temperature}度")

shanghai=City("上海",31.23,121.47)
beijing=City("北京",39.90,116.40)

shanghai.show_weather()
beijing.show_weather()