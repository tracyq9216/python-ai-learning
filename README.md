# Python AI 学习记录

我 12 周学用 AI 做产品的练习代码。

## 项目

1. 单词小测验：`week1/quiz_v1.py`
   考中英文单词，答错的词会反复考，直到全对。
2. 记账本：`week1/ledger.py`
   记一笔账存进 CSV，按类别统计花费。
3. 天气查询：`weather/weather_v0.py`
   调用 Open-Meteo 接口，显示现在的天气和未来几天的最高、最低气温。

## 运行天气查询

    cd weather
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

在 weather 文件夹里新建 .env，写上城市的纬度和经度：

    CITY_LAT=31.23
    CITY_LON=121.47

然后运行 python3 weather_v0.py