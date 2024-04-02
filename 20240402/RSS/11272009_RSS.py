##https://www.cwa.gov.tw/V8/C/S/eservice/rss.html
##https://www.cwa.gov.tw/rss/forecast/36_01.xml

import os
import requests

# 設定目標資料夾
folder = '20240402/RSS/RSS_dowmload'
if not os.path.exists(folder):
    os.makedirs(folder)

# 下載檔案
for i in range(1, 23):
    num_str = str(i).zfill(2)  # 轉換為兩位數的字串
    url = f'https://www.cwa.gov.tw/rss/forecast/36_{num_str}.xml'
    response = requests.get(url)
    with open(os.path.join(folder, f'36_{num_str}.xml'), 'wb') as f:
        f.write(response.content)

print('下載完成')

