
import pandas as pd

#Series 是一個類似陣列的物件(ㄧ維陣列)
#建立Series 物件 : 使用 list
#s =pd.Series([4, 7, -5, 3] 預設的 index = 0,1,2,3
#s =pd.Series([4, 7, -5, 3] 預設的 index = ['a', 'b', 'c', 'd']
date = pd.date_range('20211101',periods=4)
s = pd.Series([4, 7, -5, 3], index=date)

print(s)
print(s[1])
print(s[0:3])
print(s[0:]) #印出全部
print('s.index',s.index) #出來是物件類型 後方加上.values 就會是內容
print('(s.values',s.values )
print('s.loc[20211103]',s.loc['20211103'])
print('s.iloc[1]',s.iloc[1])
print('s.loc[s>0]',s.loc[s>0])
x=s>0
print(s.loc[x])