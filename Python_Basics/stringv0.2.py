import datetime
#This is for string examples with various functions
print("""Hello, Cnu
Lets practice Strings!\n""")
# strip() function
a = " Hello World!"
print(a)
print(a.strip())
print(a.strip("!"))
#lower() and upper() functions
print(a.lower())
print(a.upper())

#split function
print(a.split(" "))
check = "ll" in a
print(check)

#format
b = "Hello, Cnu! your age is {}, todays date is {}"
age = 30
date1 = datetime.datetime.now().year
print(b.format(age, date1))
