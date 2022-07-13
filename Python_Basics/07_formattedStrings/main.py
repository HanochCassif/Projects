# This is a sample Python script.


# ******** #1 old style string **************
error_no =-1004
name = "bob"
print("hey %s there is error number %d" % (name, error_no))




# ******** #2 new style (str.format) **************
print("hey {n} there is error number {e}" .format (n=name, e=error_no))





# ******** #3 string interpolation - f string  **************
a = 5
b = 10
c = "hanoch"
print(f'{c} claims that  five plus ten is {a+b} and not {2*(a+b)}')





# ******** #4 template string  **************
from string import Template
t = Template('Hey, $name !')
print(t.substitute(name = name))


templ_string = 'Hey $name, there is a $error error!'
print(Template(templ_string).substitute( name=name, error=(error_no)))
