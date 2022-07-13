# This is a sample Python script.
class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


# class object (instance of a class )
pt1 = Point()
pt2 = Point()

pt1.move()
pt1.draw()

# add class attributes at any stage of the script also to an instance
pt1.x = 10
pt1.y = 20

print(pt1.x, pt1.y)
pt2.move()

# !!! this line code will create  error since no attribute x for object pt2
print(pt2.x)



