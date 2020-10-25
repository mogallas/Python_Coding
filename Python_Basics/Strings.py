#multiline strings
a = "We are the so-called \"Vikings\" from the north."
print(a.lower())
print(a.split(", "))

y = "you" in a
print(y)
b = "test"
print("value is", b)
if b == reversed(b):
    print("String is pallindrome")
else: print("String is not pallindrom")

#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
maths = 99
science = 90
english = 89
txt = "my maths percentage is {} , science is {} and english {} respectevily"
print(txt.format(maths, science,english))