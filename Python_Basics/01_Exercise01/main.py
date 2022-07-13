## mySecond program

weight = float (input("Weight: "))

units = input("K(g) or L(bs)")

if units.upper() == 'L':
    weight *= 0.45359237
    print(" Weight in Kilograms: " + str(weight))
elif units.upper() == 'K':
    print(" Weight in Kilograms: " + str(weight))

else:
    print("wrong units ")

