##https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CD02C824-45C5-48C8-B631-98B205A2E35A

import os
import requests
import zipfile
import geopandas as gpd

# 下載zip檔案
url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CD02C824-45C5-48C8-B631-98B205A2E35A'
response = requests.get(url)
if response.headers['content-type'] == 'application/zip':
    with open('taiwan.zip', 'wb') as f:
        f.write(response.content)
else:
    print("The URL does not point to a ZIP file.")

# 解壓縮zip檔案
with zipfile.ZipFile('taiwan.zip', 'r') as zip_ref:
    zip_ref.extractall('taiwan')

# 讀取shp檔案
shp_file = [f for f in os.listdir('taiwan') if f.endswith('.shp')][0]
df = gpd.read_file(os.path.join('taiwan', shp_file))