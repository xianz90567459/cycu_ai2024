import os
import glob
import pandas as pd

print(f"Current working directory: {os.getcwd()}")

# 獲取 "ETC" 資料夾中所有的 CSV 文件
csv_files = sorted(glob.glob("20240326/ETC/TDCS_M04A_20240325_*.csv"))

# 列印出找到的 CSV 文件
print(f"Found {len(csv_files)} CSV files: {csv_files}")

# 創建一個空的 DataFrame 來儲存所有的資料
combined_df = pd.DataFrame()

# 迴圈讀取每個 CSV 文件
for file in csv_files:
    # 讀取 CSV 文件，並命名欄位名稱為c1, c2, c3, c4, c5, c6
    df = pd.read_csv(file, names=["c1", "c2", "c3", "c4", "c5", "c6"])
    
    # 將新讀取的資料添加到已存在的 DataFrame 中
    combined_df = pd.concat([combined_df, df])

# 創建一個新的資料夾 "20240326/combine"
os.makedirs("20240326/combine", exist_ok=True)

# 將合併後的 DataFrame 儲存到新資料夾中的一個 CSV 文件
combined_df.to_csv("20240326/combine/combined.csv", index=False)