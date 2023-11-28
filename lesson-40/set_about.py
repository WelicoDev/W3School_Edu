myset = {"apple", "banana", "cherry"}

print(myset)

print('--------------------------------------------------------------------')
print('To\'plam yaratish:')

thisset = {"apple", "banana", "cherry"}
print(thisset)

print('----------------------------------------------')
# Ikki nusxadagi qiymatlar e'tiborga olinmaydi:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

print('----------------------------------------------------------------------')

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

print('----------------------------------------------------------------------')

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

print('------------------------------------------------------------------------')

# To'plamdagi elementlar sonini oling:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


print('----------------------------------------------------------------------------')


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set3)
print(set2)
print(set1)

myset = {"apple", "banana", "cherry"}
print(type(myset))

print('----------------------------------------------------------------------------------------')

thisset = set(("apple", "banana", "cherry"))
# note the double round-brackets
print(thisset)
