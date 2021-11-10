def getRabbitAndChicken(amount , feet):

        rabbit_count = (feet - (amount * 2)) / 2
        chicken_count = amount - rabbit_count
        return  rabbit_count , chicken_count

if __name__ == "__main__":
    ra , ch = getRabbitAndChicken(83,240)
    print(ra , ch)