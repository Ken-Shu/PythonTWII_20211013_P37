

import pandas as pd

print(pd.__version__)

s = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('20211101' , periods=5))
print(s)
print("max : ", s.max())
print("min : ", s.min())
print("sum : ", s.sum())
print("avg : ", s.avg())
print("mean : ", s.mean())
print("std : ", s.std())