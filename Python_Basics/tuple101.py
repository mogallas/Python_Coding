tuple1 = ("cnu", "babu", "mowna", "mowna")
print(tuple1)

list1 = list(tuple1)
print(list1)
list1.insert(3,"aarvi")
tuple1 = tuple(list1)
print(tuple1)


#unpacking tuple

(name1, name2, *name3) = tuple1
print(name1, name2, name3)


#loop
for x in tuple1:
    print(x)

#loop by index
for i in range(len(tuple1)):
    print(tuple1[i])

"""
Union and intersection
"""
tuple2 = ("Renuka", "Lakshmi")
print(tuple1 + tuple2)