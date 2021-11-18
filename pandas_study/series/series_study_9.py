

import pandas as pd

print(pd.__version__)

# 綜合練習 Series 2
# A 股票 2021-11-01~07 價格10
# A 股票 2021-11-08~10 價格15
# 求 Series
s = pd.Series(10, index=pd.date_range('20211101', periods=10))
print(s)
#s.loc['2021-11-08':'2021-11-10']+=5
s.loc['2021-11-08':]+=5 #從2021-11-08 開始
#s.loc[:'2021-11-08']+=5 從頭開始
print(s)
