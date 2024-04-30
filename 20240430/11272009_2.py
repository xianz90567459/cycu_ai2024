import pandas as pd
import os
import datetime

# 定義一個函數來特徵化每一行
def feature(row):
    # 時間特徵
    time = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M')
    time_feature = (time.hour * 60 + time.minute) // 5 + 1

    # 地點特徵
    if row[1][:2] == '01':
        location_feature = int(''.join([c for c in row[1][2:7] if not c.isalpha()]))
    else:
        location_feature = row[1]

    # 方向特徵
    direction_feature = 1 if row[2] == 'N' else 2

    # 車種特徵
    vehicle_type = row[3]
    vehicle_count = row[4]
    vehicle_features = [0, 0, 0, 0, 0]
    if vehicle_type == 31:
        vehicle_features[0] = vehicle_count
    elif vehicle_type == 32:
        vehicle_features[1] = vehicle_count
    elif vehicle_type == 41:
        vehicle_features[2] = vehicle_count
    elif vehicle_type == 42:
        vehicle_features[3] = vehicle_count
    elif vehicle_type == 5:
        vehicle_features[4] = vehicle_count

    return [time_feature, location_feature, direction_feature] + vehicle_features

# 讀取並特徵化所有 CSV 檔案
features = []
for filename in os.listdir('/workspaces/cycu_ai2024/20240430/VehicleType'):
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join('/workspaces/cycu_ai2024/20240430/VehicleType', filename), header=None)
        for index, row in df.iterrows():
            # 檢查 '地點' 列的前兩個字符
            if str(row[1])[:2] != '01':
                continue  # 如果前兩個字符不是 '01'，則跳過該行
            features.append(feature(row))

# 假設 features 是一個包含所有特徵向量的列表
df = pd.DataFrame(features, columns=['時間', '地點', '方向', '小客車', '小貨車', '大客車', '大貨車', '聯結車'])

# 將相同時間、相同地點、相同方向的行合併在一起，並對 '小客車', '小貨車', '大客車', '大貨車', '聯結車' 的列求和
df = df.groupby(['時間', '地點', '方向']).sum().reset_index()

# 顯示前 5 行
print(df.head(5))

# 顯示有多少行
print(len(df))

# 將特徵保存到 CSV 檔案
df.to_csv('/workspaces/cycu_ai2024/20240430/11272009_2.csv', index=False)