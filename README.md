# 短連結廣告自動判斷程式
version = 1.0

## 使用方法
得到廣告之後，儲存為 "ad_data.json" 檔案，格式如下：

```
{
    "adcontent": "廣告內容",
    "//": "註解，在解析時自動刪除",
    "blacklists": "篩選字串1|篩選字串2"
}
```

黑名單則以 `|` 隔開。

> 注意！這個程式只允許小於 8192 bytes 的 ad_data.json 檔案，
請保證自己的 ad_data.json 小於 8192 bytes。

> ad_data.json 檔案須為 UTF-8 格式。

## 判斷
若該網站的內容符合 blacklists 中的任何內容，則會回傳退出
代碼 `2` ，若不符合則回傳 `1` 。

回傳代碼 `3` 代表未知錯誤，請回報給此程式作者。

## 設定
開啟 main.py 之後，看註解說明以設定項目。<br/>
此處不再多加敘述。

## 作者
pan93412, for anyone who needs the feature.
