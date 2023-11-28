# Usul union()ikkala to'plamdagi barcha elementlar bilan yangi to'plamni qaytaradi:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print('-------------------------------------------------------------')

# Usul update()set2dagi elementlarni set1ga kiritadi:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

print('---------------------------------------------------------------')

# Ikkala to'plamda mavjud bo'lgan narsalarni saqlang consolga o'rnating :

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple" , "banana"}

x.intersection_update(y)

print(x)
#
# Usul faqat ikkala to'plamda mavjud bo'lgan narsalarni o'z ichiga olgan yangiintersection() to'plamni qaytaradi .
#
# Misol

print('---------------------------------------------------------------------')
x = {"apple", "banana", "cherry" , "google"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

print('--------------------------------------------------------------------------')

# Misol
# Ikkala to'plamda mavjud bo'lgan elementlarni o'z ichiga olgan to'plamni qaytaring consolga o'rnating :

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


# Ikkala to'plamda ham mavjud bo'lmagan narsalarni saqlang:
print('--------------------------------------------------------')


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

print('-----------------------------------------------------------------')

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

print('-----------------------------------------------------------------------')

# Misol
# True va 1bir xil qiymat hisoblanadi:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)