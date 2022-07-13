# This is a sample Python script.

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi! my name is {self.name}")


p1 = Person("Hanoch")
p2 = Person("Zagor")

p1.talk()
p2.talk()