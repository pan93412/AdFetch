#!/usr/bin/python3
try:
    import requests
    import os, sys, json, re
except ModuleNotFoundError:
    print("安裝方法：pip install requests")
    raise ModuleNotFoundError("[ERR] 請安裝 requests 函式庫！")

if os.path.exists("ad_data.json") and os.path.isfile("ad_data.json"):
    pass
else:
    raise Exception("您的 json 檔案不存在！請參閱 'README.md' 檔案了解用法。")

# * 使用者可設定項目 *
## 需要處理的網址
CheckURLs = [
    'bit.ly'
]
CheckURLPatterns = {
    'bit.ly': r'(http|https)://(.*)(bit.ly)/(.+)',
}

## 檔案讀取 bytes 上限
## 建議 2048 - 10240 之間，不宜過大或過小。
read_bytes = 8192

## 檔案編碼方式
## 預設以 UTF-8 讀取，但也可以變更。
encoding_method = "UTF-8"

## 瀏覽器標頭
## 建議定期更新標頭檔案，以防止廣告程式封鎖此 User Agent.
Headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}

## 詳細模式
## 選擇性開啟。(關閉 False，開啟 True)
VerboseMode = False

# 載入檔案
ad_data_raw = os.open("ad_data.json", os.O_RDONLY)
raw_content = os.read(ad_data_raw, read_bytes).decode(encoding_method)
if VerboseMode:
    print(raw_content)
ad_json = json.loads(raw_content)
ad_json.pop('//')
os.close(ad_data_raw)

# 定義參數
AdvContent = ad_json['adcontent']
BlackLists = ad_json['blacklists'].split(r'|')

# 開始處理
for i in CheckURLs:
    if AdvContent.find(i):
        search_pattern = re.compile(CheckURLPatterns[i])
        short_url_dat = search_pattern.findall(AdvContent)
        break

AdURL = '{0}://{1}{2}/{3}'.format(
    short_url_dat[0][0], 
    short_url_dat[0][1], 
    short_url_dat[0][2], 
    short_url_dat[0][3]
)
if VerboseMode:
    print("短網址連結：" + AdURL)

AdContent_Raw = requests.get(AdURL, headers = Headers)
AdContent = AdContent_Raw.text

if VerboseMode:
    print(AdContent_Raw)
    print(AdContent)

for i in BlackLists:
    if AdContent.find(i) != -1:
        print("[INFO] 確定為廣告網站！")
        exit(2)
    else:
        print("[INFO] 可能不是廣告網站。")
        exit(1)
        
exit(3)
