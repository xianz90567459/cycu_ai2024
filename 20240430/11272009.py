#https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/
#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/

import os
import requests
import pandas as pd
from datetime import datetime, timedelta

def download_and_save(url, directory, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果請求失敗，這將引發一個異常
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, filename), 'wb') as f:
            f.write(response.content)
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err} for url: {url}")

import datetime

#下載資料

# 定義基礎 URL 和日期範圍
base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/"
start_date = datetime.date(2024, 4, 29)
end_date = datetime.date(2024, 4, 29)

# 定義每小時的分鐘數
minutes = [f"{i:02d}" for i in range(0, 60, 5)]

# 對於日期範圍內的每一天
current_date = start_date
while current_date <= end_date:
    # 對於每個小時和分鐘
    for hour in range(24):
        for minute in minutes:
            # 生成 URL 和檔案名稱
            date_str = current_date.strftime("%Y%m%d")
            time_str = f"{hour:02d}{minute}00"
            url = f"{base_url}{date_str}/{hour:02d}/TDCS_M03A_{date_str}_{time_str}.csv"
            filename = f"TDCS_M03A_{date_str}_{time_str}.csv"

            # 下載和保存檔案
            download_and_save(url, '20240430/VehicleType', filename)

    # 移到下一天
    current_date += datetime.timedelta(days=1)

# 定義第二個基礎 URL 和日期範圍
base_url_2 = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/"
start_date_2 = datetime.date(2024, 4, 29)
end_date_2 = datetime.date(2024, 4, 29)

# 對於日期範圍內的每一天
current_date_2 = start_date_2
while current_date_2 <= end_date_2:
    # 對於每個小時和分鐘
    for hour in range(24):
        for minute in minutes:
            # 生成 URL 和檔案名稱
            date_str_2 = current_date_2.strftime("%Y%m%d")
            time_str_2 = f"{hour:02d}{minute}00"
            url_2 = f"{base_url_2}{date_str_2}/{hour:02d}/TDCS_M05A_{date_str_2}_{time_str_2}.csv"
            filename_2 = f"TDCS_M05A_{date_str_2}_{time_str_2}.csv"

            # 下載和保存檔案
            download_and_save(url_2, '20240430/SpaceMeanSpeed', filename_2)

    # 移到下一天
    current_date_2 += datetime.timedelta(days=1)