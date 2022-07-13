import random

# 1st example
for i in range(3):
    print(random.random())


# 2nd example
for i in range(3):
    print(random.randint(1,10))


# 3nd example
members = ["Hanoch", "Tammy", "Ariel","Tal"]
for i in range(3):
    leader = random.choice(members)
    print(leader)
