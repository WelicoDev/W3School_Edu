thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print('---------------------------------------------')

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Eslatma: Yuqoridagi misollar natijasida ro'yxatlar endi 4 ta elementni o'z ichiga oladi.
print('------------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print('--------------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)