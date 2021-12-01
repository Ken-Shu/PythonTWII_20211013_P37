import requests
import pandas as pd
import io
date = '20211117'
url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1637151456900' %date
r = requests.get(url)
#print(r.text)
lines = r.text.split('\n')
newlines = []
for line in lines:
    if(len(line.split('",')) == 17):
        newlines.append(line)
#將 line 轉為 dataframe
data = "\n".join(newlines).replace('=','')
df =pd.read_csv(io.StringIO(data))
#將資料全部變為 str
df = df.astype(str)
#將內容有,的去除
df = df.apply(lambda s:s.str.replace(',',''))
#將證券代號設定為 index
df = df.set_index('證券代號')
#去除非數字的資料
df = df.apply(lambda s:pd.to_numeric(s,errors='coerce')) #coerce 略過錯誤
#將欄位內容是 NaN 的資料刪除'all'全部刪除
df = df.dropna(axis=1, how='all')
print(df)
#顯示所有欄位/列數 None代表全部
#pd.set_option('display.max_columns',None)
#pd.set_option('display.max_rows',None)
#查出收盤價比開盤價高出10%的股票
print(df[df['收盤價']/df['開盤價'] > 1.1])