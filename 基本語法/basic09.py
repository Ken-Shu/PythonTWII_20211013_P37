import re
# Python 基本資料結構
# list   列表[]    (元素內容可以重複, 元素內容可以修改)
# tuple  列表()    (唯讀, Fast)
# set    列表    (元素內容不可重複, 元素內容可以修改)
# dict   字典列表{} (元素內容可以重複, 元素內容可以修改)

#list 列表
score1 = [100,90]
score2 = [80,70]
score1[1] = 95
score1.append(70)
score3 = score1+score2
print(score3)

#tuple 列表 (唯獨 不可修改 也不可增加)
score1 =(100,90)
#score1[1] = 95 不可修改
#score1.append(95) 不可增加
print(score1)

#list 與 tupel 互轉
scores = (100,90)
scores = list(scores)
print(type(scores) , scores)
scores = tuple(scores)
print(type(scores) , scores)

#set 列表
empIds = [1,3,5,2,3,1]
empIds = set(empIds)
print(type(empIds) , empIds)
print(len(empIds))

#dict 字典列表 (key : value)
#key 的值不可重複
#value 的值可以重複
a = {'symbol' : '2330.TW','price' : 599}
b = {'symbol' : '2317.TW','price' : 108}
c = {'symbol' : '3008.TW','price' : 2080}
prices = [a,b,c]
print(type(prices) , prices)
for p in prices :
    print(p , p.get('symbol'), p.get('price'))

# 切割字串 split
# 股名,價格,殖利率,本益比,股價淨值比
s = "2330.TW,599,1.67,28.03,7.8"
s = s.split(",")
print(type(s) , '本益比',s[3])
#多符號切割
s = "2330.TW,599,1.67,28.03,7.8"
s = re.split(',|#|!' ,s)
print(type(s), '本益比',s[3])

#split 轉 dict(字典格式 key , value)
# 股名,價格,殖利率,本益比,股價淨值比
s = "股名=2330.TW,價格=599,殖利率=1.67,本益比=28.03,股價淨值比=7.8"
s = dict( ex.split("=") for ex in s.split(","))
print(type(s) , s , s.get('本益比'))