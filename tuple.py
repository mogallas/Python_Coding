tup1 = ('cnu', '32', 'SRE')
tup2 = ('mowna', '30', 'SE')
tup3 = ()
tup4 = (47,)

print(tup1[0])
print(tup2[0])
print(tup3, tup4)

#packing and unpacking
x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x   # tuple unpacking
print(company)
print(emp)
print(profile)

#comparing tuples
a = (3,14,47,63,9)
b = (3, 14, 56, 82,1)
if (a>b): print("a is greater than b")
else: print("b is greater than a")

print(len(a)) # length of tuple
print(min(b))
print(any(a))
print(sorted(a))