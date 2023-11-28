# O'zgartirish imkoniyatiga ega bo'lish uchun ro'yxatni ro'yxatga aylantiring:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
print('-----------------------------------------------------------------')


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

print('---------------------------------------------------------')

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

print('--------------------------------------------------------')

# Misol
# Tupleni ro'yxatga aylantiring, "olma" ni olib tashlang va uni yana kortejga aylantiring:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

print('------------------------------------------------------------')

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists