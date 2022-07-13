# This is a sample Python script.
list = ["moshe", "Hanoch", "Michal", "Noa", "Rafi"]

print (list)
print(list[2])
print(list[-1])

list[0]="Moshe"
print(list[0:3])

list.append("Rahehli")
print(list)

list.insert(1,"Shai")
print(list)

if "Shay" in list:
    list.remove("Shay")
    print(list)
else:
    print("Sahi" in list)

print(len(list))

list.clear()
print(list)