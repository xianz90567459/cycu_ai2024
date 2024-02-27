import feedparser

# 設定要爬取的網址
url = "https://news.pts.org.tw/xml/newsfeed.xml"

# 使用 feedparser 解析 RSS feed
feed = feedparser.parse(url)

# 輸出 feed 的標題和項目數量
print("Feed title:", feed.feed.title)
print("Number of entries:", len(feed.entries))

# 遍歷每一個 'entry'
for entry in feed.entries:
    
    #幫我確認標題是否有台中 如果有請將標題印出來
    if "台中" in entry.title:
        print(entry.title)
#幫我把列印出來的標題依序存入一個excel檔案中
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "News"
sheet['A1'] = "Title"
i = 2
for entry in feed.entries:
    if "台中" in entry.title:
        sheet['A'+str(i)] = entry.title
        i += 1
wb.save("news.xlsx")
print("Done!")


