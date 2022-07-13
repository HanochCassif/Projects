# This is a sample Python script.
class Point:
    x = 0
    y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b


    def move(self):
        print(f'move to {self.x} , {self.y}')



    def draw(self):
        print('draw')


# class object (instance of a class )
pt1 = Point(0, 1)
pt2 = Point(30, 40)

print(pt1.x, pt1.y)

# change attributes defaults values
pt1.x = 10
pt1.y = 20

pt1.move()
pt1.draw()


print(pt1.x, pt1.y)

pt2.move()
print(pt2.x,  pt2.y)
