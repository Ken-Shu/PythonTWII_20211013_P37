from functools import reduce

#1. lambda parameter_list : expression
max = lambda a, b: a if a> b else b
print(max(10,20))

#2. (lambda parameter_list : expression)(arguoment)
print((lambda a: a*a)(5))

#3. filter(lambda parameter_list : expression , iterable)
#iterable = 數組陣列 可以尋訪的資料結構
nums = [50, 2, 10, 40]
print(type(nums))
#想過濾出大於 20 的資料
result = filter(lambda x : x>20 , nums)
print(result , list(result)) # filter 出來是物件 所以要轉回來

#4. map(lambda parameter(參數) : expression(運算式) , iterable)
#轉換
scores = [50, 80, 90, 30] #[False ,True , True ,False]
result = map(lambda x : x>=60 , scores)
result2 = map(lambda x : 'True' if x>=60 else 0, scores)
print(scores , list(result)) # filter 出來是物件 所以要轉回來

#5. reduce(lambda parameter(參數) : expression(運算式) , iterable)
# reduce 歸納
scores = [50, 80, 90, 30]
result = reduce(lambda  x , y : x + y , scores)
print(result)

#6. sorted(iterable key =lambda parameter(參數) : expression(運算式) )
scores = [50, 80, 90, 30]
print(sorted(scores , reverse=True))
prices = [('2330.TW',599),('2317.TW',108),('3008.TW',2080)]
# p = 每一個陣列的位置 p[1] 代表每一個陣列裡面的 第幾號位置 此處 p[1] 分別代表 599 ,108 , 2080
print(sorted(prices, key= lambda p : p[1] , reverse=True))