##https://scweb.cwa.gov.tw/zh-tw/earthquake/data/

from selenium import webdriver
import time

# 建立一個新的 Chrome 瀏覽器實例
driver = webdriver.Chrome('/path/to/your/chromedriver')  # 請將此路徑替換為您的 ChromeDriver 的實際路徑

# 訪問 CSV 文件的 URL
driver.get('https://scweb.cwa.gov.tw/zh-tw/earthquake/csv/2024%E5%B9%B44%E6%9C%88')

# 等待一段時間，讓瀏覽器完成下載
time.sleep(5)

# 關閉瀏覽器
driver.quit()