# "Banan" ni olib tashlang:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print('-----------------------------------------------')

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

print('---------------------------------------------------')
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


print('----------------------------------------------------')
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

print('-----------------------------------------------------')
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

print('---------------------------------------------------------')
thislist = ["apple", "banana", "cherry"]
del thislist


print('------------------------------------------------------------')
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("Clear")
print(thislist)