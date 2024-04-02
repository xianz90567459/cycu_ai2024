import geopandas as gpd
import matplotlib.pyplot as plt

# 讀取shp檔案
df = gpd.read_file('20240402/taiwan/COUNTY_MOI_1090820.shp')

# 顯示內容
print(df.head())

#使用matplotlib繪製地圖
df.plot()
plt.show()
#存成PNG檔案
plt.savefig('20240402/taiwan/11272009_taiwan.png')