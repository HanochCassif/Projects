# This is a sample Python script.
try:
    age = int(input('age:'))
    print(age)
    risk = 2000
    discount = risk/age
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print('age cannot be 0')


