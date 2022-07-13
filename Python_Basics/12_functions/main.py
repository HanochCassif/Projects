# This is a sample of a Python function.

def hello_world_func():
    print("hello world")


def greet_user(first_name, last_name):
    print(f'hi {first_name} {last_name}!')
    print("welcome aboard!")


# a 'return value' function
def square(number):
    return number*number
    # ***** !!!! by default a non returns value function returns NONE !!!! ****


# main program ... space of 2 lines after each function
print("start")
hello_world_func()

# position argument example
greet_user('Hanoch', 'Cassif')

# keyword argument example
greet_user(last_name="Cassif", first_name="Hanoch")
print(square(3))
print("end")



