# dictionary exercise
phone_num =input("phone: ")

digits = {
    '0':  "zero",
    '1':  "one",
    '2':  "two" ,
    '3':  "three",
    '4':  "four",
    '5':  "five",
    '6':  "six",
    '7':  "seven",
    '8':  "eight",
    '9':  "nine"

}


out =""

for ch in phone_num:
    out += ' '+digits.get(ch, '@@')
print(out)



