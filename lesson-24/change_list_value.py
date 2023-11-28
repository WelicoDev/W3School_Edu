# Ikkinchi elementni o'zgartiring:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print('----------------------------------------')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


print('--------------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

print('----------------------------------------------')
# Ikkinchi va uchinchi qiymatlarni bitta qiymat bilan almashtiring :

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
print('------------------------------------------------------')
# incert

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Eslatma: Yuqoridagi misol natijasida ro'yxat endi 4 ta elementni o'z ichiga oladi.