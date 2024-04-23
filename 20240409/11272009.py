import pandas as pd
import folium
from IPython.display import display

# 讀取 CSV 文件，跳過第一行
df = pd.read_csv('20240409/地震活動彙整.csv', skiprows=1, encoding='cp950')

# 將地震時間轉換為 datetime 對象，注意時間格式已經改變
df['地震時間'] = pd.to_datetime(df['地震時間'], format='%Y-%m-%d %H:%M:%S')

# 定義時間範圍，注意時間格式已經改變
start_time = pd.to_datetime('2024-04-03 07:58:09', format='%Y-%m-%d %H:%M:%S')
end_time = pd.to_datetime('2024-04-10 00:00:00', format='%Y-%m-%d %H:%M:%S')

# 選擇在指定時間範圍內的地震
selected_earthquakes = df[(df['地震時間'] > start_time) & (df['地震時間'] <= end_time)]

# 創建一個地圖，中心點設為選擇的地震的第一個地點
m = folium.Map(location=[selected_earthquakes.iloc[0]['緯度'], selected_earthquakes.iloc[0]['經度']], zoom_start=6)

import matplotlib.pyplot as plt
import matplotlib.colors

# 創建一個從黃色到紅色的顏色映射
cmap = plt.cm.get_cmap('YlOrRd')

import folium.plugins

# 創建一個 GeoJSON 物件，包含所有地震的資訊
features = [
    {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [row['經度'], row['緯度']],
        },
        'properties': {
            'time': row['地震時間'].isoformat(),
            'style': {'color': matplotlib.colors.rgb2hex(cmap(row['規模'] / selected_earthquakes['規模'].max()))},
            'icon': 'circle',
            'iconstyle': {
                'fillColor': matplotlib.colors.rgb2hex(cmap(row['規模'] / selected_earthquakes['規模'].max())),
                'fillOpacity': 0.8,
                'stroke': 'true',
                'radius': 5
            },
            'popup': f"時間: {row['地震時間']}, 規模: {row['規模']}, 緯度: {row['緯度']}, 經度: {row['經度']}",
        }
    }
    for index, row in selected_earthquakes.iterrows()
]

# 將 GeoJSON 物件添加到地圖上，並添加時間軸
folium.plugins.TimestampedGeoJson(
    {'type': 'FeatureCollection', 'features': features},
    period='PT1H',
    add_last_point=False,
    auto_play=True,
    loop=False,
    max_speed=1,
    loop_button=True,
    date_options='YYYY/MM/DD HH:mm:ss',
    time_slider_drag_update=True
).add_to(m)

# 定義地圖儲存的路徑
map_path = 'earthquake_map.html'

# 儲存地圖為 HTML 文件
m.save(map_path)

# 顯示文件的路徑
print('file://' + map_path)