#20240402/RSS/RSS_dowmload
#https://www.cwa.gov.tw/rss/forecast/36_01.xml
import pandas as pd
print(pd.__version__)
import os
import re
from xml.etree import ElementTree as ET

# 生成檔案名稱列表
file_names = [f"36_{str(i).zfill(2)}.xml" for i in range(1, 23)]

# 初始化一個空的 DataFrame
df = pd.DataFrame(columns=['city', 'temperature'])

# 讀取和顯示XML檔案的標題
for file_name in file_names:
    file_path = os.path.join('20240402/RSS/RSS_dowmload', file_name)
    if os.path.exists(file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # 提取和顯示標題
        for item in root.findall('.//item'):
            title = item.find('title').text if item.find('title') is not None else 'No title'
            if "一週天氣預報(04/02 17:00發布)" not in title:
                city = re.search(r'(.{3})(?=\d)', title)
                temperature = re.search(r'溫度: (.+?)(?= 降雨機率)', title)
                if city and temperature:
                    city = city.group(1)
                    temperature = temperature.group(1)
                    # 將城市和溫度添加到 DataFrame
                    df = df._append({'city': city, 'temperature': temperature}, ignore_index=True)

# 將 DataFrame 保存為 CSV 文件
df.to_csv('weather.csv', index=False)
print('已保存為 CSV 文件')

#讀取20240402/taiwan/COUNTY_MOI_1090820.shp 檔案 並使用matplotlib繪製地圖
import geopandas as gpd
import matplotlib.pyplot as plt

# 讀取shp檔案 取名為Taiwan
Taiwan = gpd.read_file('20240402/taiwan/COUNTY_MOI_1090820.shp')


#將weather.csv檔案讀取並合併到Taiwan，以city對應到Taiwan的COUNTYNAME，並使用left join
weather = pd.read_csv('weather.csv')
weather = weather.rename(columns={'city': 'COUNTYNAME'})
Taiwan = Taiwan.merge(weather, on='COUNTYNAME', how='left')
print(Taiwan)

fig, ax = plt.subplots()

# 在每個縣市的中心點上顯示溫度
for x, y, label in zip(Taiwan.geometry.centroid.x, Taiwan.geometry.centroid.y, Taiwan['temperature']):
    ax.text(x, y, str(label), fontsize=8)

# 繪製地圖，但不顯示圖例
Taiwan.plot(column='temperature', ax=ax, legend=False, cmap='coolwarm')

# 設定X軸和Y軸的範圍
ax.set_xlim(119, 123)
ax.set_ylim(21.5, 25.5)

# 增加標題
plt.title('11272009_CHANG, HSIEN-CHENG')

plt.show()

# 將地圖保存為PNG文件
plt.savefig('taiwan.png')
print('已保存為 PNG 文件')