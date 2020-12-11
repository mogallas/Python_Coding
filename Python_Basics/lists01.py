list1 = ["india", "USA", "UK","47", "03", "AUS"]
print(list1)
print(list1[1:3])
print(list1[:4])
print(list1[-4:-1])

if "USA1" in list1:
    print("Yes, Its USA")


# Update the List
#insert,append
 
print(list1)
list1[3:5] = ["09", "11"]
print(list1)
list1.insert(3,"UAE")
print(list1)
lits2 = ["Pakistan", "Bangladesh", "china"]
print("Second list is ",lits2)
list1.extend(lits2)
print(list1)


#Remove 
list1.remove("china")
print(list1)

list1.pop(8)

lits2.clear()
print(list1, lits2)

#Iterate
for i in list1:
    print(i)
#Iterate by referring index
for x in range(len(list1)):
    print(list1[x])

#List Compreshension 
newlist = []
for i in list1:
    if isinstance(1, str):
        newlist.append(i)
print(newlist)

#Sort Lists
list1.sort(reverse= True)
print(list1)


