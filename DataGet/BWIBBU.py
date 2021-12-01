import requests

def getdata(yyyy,mm,dd):
 yyyymmdd = str(yyyy)+str(mm)+str(dd)
 url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=%s&selectType=ALL'%yyyymmdd
 data = requests.get(url).text
 data = data.split("\r\n")
 print(data)
 list = [] #用來存放已經整理好的資料
 for d in data:
     d = d.replace('"', '')
     array = d.split(",")
     if len(array) == 8 and array[0] != '證券代號':
         row =(
             array[0],
             array[1],
             float(array[2]) if array[2] != '-' else -1,
             float(array[4]) if array[4] != '-' else -1,
             float(array[5]) if array[5] != '-' else -1,
             str(yyyy)+"-"+str(mm)+"-"+str(dd)
         )
         list.append(row)
 return list

'''
if __name__ == '__main__':
    list = getdata(2021,11,3)
    print(len(list),list)
'''