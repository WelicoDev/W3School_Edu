mytuple = ("apple", "banana", "cherry")


# Tuple yarating:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

myfriends = ("Islom" , "Javohir" , "Otabek" , "Suhrob" ,"Zohidjon" , "Sarvar" , "Abdullo" , "Jonibek" , "Jahongir")
for friend in myfriends:
    print(friend)

print('------------------------------------------------------')

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print('---------------------------------------------------')

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print('------------------------------------------------------')

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print('-----------------------------------------------------')

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(type(tuple3))
print(type(tuple2))
print(type(tuple1))

print('---------------------------------------------------------')
# Satrlar, butun sonlar va mantiqiy qiymatlardan iborat kortej:

tuple1 = ("abc", 34, True, 40, "male")

print(type(tuple1))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print('-------------------------------------------------------------------------')
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



