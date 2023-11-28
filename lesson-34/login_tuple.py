thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print('-----------------------------------------------')

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

print('-------------------------------------------------------')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Eslatma: Qidiruv 2-indeksda (qo'shilgan) boshlanadi va 5-indeksda (qo'shilmagan) tugaydi.
#
# Esda tutingki, birinchi element 0 indeksiga ega.

print('-----------------------------------------------------------')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

print('---------------------------------------------------------------------')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

print('---------------------------------------------------------------------')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


print('----------------------------------------------------------------------')

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")