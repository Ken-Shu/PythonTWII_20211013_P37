import math


if __name__ == '__main__':
    r = 123
    # 求出圓面積 與 求體積
    pi = math.pi
    area = math.pow(r,2)*pi
    r3 = math.pow(r,3)
    volume = 4/3*(pi*r3)
    print("圓面積 : %.2f"%area)
    print(f"圓面積 ={area} 球體積 = {volume}")
    #加上千分位
    #area = format(area,",")

    print(area , type(area))
    print('%.2f'%area)
    print(format(float('%.2f'%area),","))