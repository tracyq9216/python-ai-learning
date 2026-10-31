import os
from dotenv import load_dotenv
print(load_dotenv())
name = os.getenv("MY_NAME")
key = os.getenv("API_KEY")
city = os.getenv("CITY_LAT")
print(f"你好 {name}，密码是 {key}")
print(type(city))

print(round(float(city)+1,2))