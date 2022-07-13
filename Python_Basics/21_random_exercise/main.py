import random


class Dice:
    def __init__(self):
        print("")

    def roll(self):
        #first = random.randint(1, 6)
        #second = random.randint(1, 6)
        return random.randint(1, 6)


        # returns result as tuple
        #return first, second


dice = Dice()
for i in range(10):
    print(dice.roll())
    print(dice.roll())
    print()
