#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/M05A_20240101.tar.gz

import os
import requests
from datetime import timedelta, date
from datetime import date, timedelta


from datetime import date, timedelta

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

# 定義一個函數來下載檔案並保存到本地
def download_file(url, local_filename, date_str):
    try:
        # 嘗試從給定的URL下載檔案
        with requests.get(url, stream=True, timeout=60) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
        # 如果下載成功，打印一條消息
        print(f"Downloaded {local_filename}")
    except Exception as e:
        # 如果下載失敗，打印一條消息並嘗試下載每小時的檔案
        print(f"Failed to download {local_filename}. Error: {e}")
        download_hourly_files(date_str)


start_date = date(2024, 1, 1)
end_date = date(2024, 4, 30)

for single_date in daterange(start_date, end_date):
    date_str = single_date.strftime("%Y%m%d")
    url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/M05A_{date_str}.tar.gz"
    local_filename = f"M05A_{date_str}.tar.gz"
    download_file(url, local_filename, date_str)



def download_hourly_files(date_str):
    # 創建基礎URL和分鐘數列表
    base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/"
    minutes = [f"{i:02d}" for i in range(0, 60, 5)]
    # 對於每個小時和每個分鐘，創建一個URL和一個檔案名稱
    for hour in range(24):
        for minute in minutes:
            time_str = f"{hour:02d}{minute}00"
            url = f"{base_url}{date_str}/{hour:02d}/TDCS_M05A_{date_str}_{time_str}.csv"
            filename = f"TDCS_M05A_{date_str}_{time_str}.csv"
            # 打印出生成的URL
            print(f"Generated URL: {url}")
            # 創建儲存檔案的路徑
            save_path = f'20240521/MIDpy/1_download/{date_str}'
            # 如果路徑不存在，創建它
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            # 嘗試下載並保存該檔案
            response = requests.get(url)
            if response.status_code == 200:
                with open(os.path.join(save_path, filename), 'wb') as file:
                    file.write(response.content)
            else:
                print(f"Failed to download file from {url}")