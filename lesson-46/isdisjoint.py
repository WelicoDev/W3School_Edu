# Agar to'plamda hech qanday element xbo'lmasa, True qiymatini qaytaring y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

print('---------------------------------------------------------------------')

# Ikkala to'plamda bir yoki bir nechta element mavjud bo'lsa, False qiymatini qaytaring:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.isdisjoint(y)

print(z)