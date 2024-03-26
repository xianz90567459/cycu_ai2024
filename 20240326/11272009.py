##https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/
import os
import requests
import pandas as pd
from io import StringIO

base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/"
output_file = "combined.csv"

# 創建一個空的 DataFrame 來儲存所有的資料
combined_df = pd.DataFrame()

# 迴圈讀取每個小時的資料夾
for hour in range(24):
    # 迴圈讀取每個小時內的 csv 文件
    for minute in range(0, 60, 5):
        # 建立 csv 文件的名稱
        csv_file = f"TDCS_M04A_20240325_{hour:02d}{minute:02d}00.csv"
        # 建立 csv 文件的網路路徑
        csv_url = os.path.join(base_url, f"{hour:02d}", csv_file)
        # 讀取 csv 文件
        response = requests.get(csv_url)
        # 如果讀取成功，則將 csv 文件的內容轉換為 pandas DataFrame
        if response.status_code == 200:
            df = pd.read_csv(StringIO(response.text))
            # 將新讀取的資料添加到已存在的 DataFrame 中
            combined_df = pd.concat([combined_df, df])

# 將合併後的 DataFrame 儲存到一個 csv 文件
combined_df.to_csv(output_file, index=False)