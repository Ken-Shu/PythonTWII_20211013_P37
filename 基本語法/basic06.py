
"""
雞兔同籠
雞加兔子共有 83 隻，雞的腳加上兔子的腳共有 240 隻腳，求雞與兔子各有幾隻?

"""

chicken = 2
rabbit = 4
amount = 83
feet = 240


if amount * 2 <= feet <= amount *4 :
    rabbit_count = (feet - (amount * chicken)) / 2
    chicken_count = amount - rabbit_count
    print("雞 : ",chicken_count,"兔 : ",rabbit_count)
    print((rabbit_count * 4) + (chicken_count * 2))
    print(f"rabbit = {rabbit_count}")
    print(f"chicken = {chicken_count}")
else :
    print("設定不正確")