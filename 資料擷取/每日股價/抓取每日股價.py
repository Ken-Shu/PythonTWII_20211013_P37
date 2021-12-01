import requests
import pandas as pd
import io
date = '20211117'
url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=%s&type=ALLBUT0999&_=1637151456900' %date
r = requests.get(url)
#print(r.text)
lines = r.text.split('\n')
print(len(lines))
print(lines[0])
print(lines[790])
print(lines[800])

print(len(lines[0].split('",')))
print(len(lines[790].split('",')))
print(len(lines[800].split('",')))
