# This is a sample Python script.

class Mammal:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f"{self.name } is walking")


class Dog(Mammal):
    def barking(self):
        return "barking"


class Cat(Mammal):
    def crying(self):
        return "crying"


dog1 = Dog("ringo")
cat1 = Cat("lily")

dog1.walk()
print(dog1.barking())

cat1.walk()
print(cat1.crying())