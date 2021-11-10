
import pandas as pd
import matplotlib as mat #繪圖工具
#Series 是一個類似陣列的物件(ㄧ維陣列)
#建立Series 物件 : 使用 list
#s =pd.Series([4, 7, -5, 3] 預設的 index = 0,1,2,3
#s =pd.Series([4, 7, -5, 3] 預設的 index = ['a', 'b', 'c', 'd']
date = pd.date_range('20211101',periods=4)
s = pd.Series([4, 7, -5, 3], index=date)

