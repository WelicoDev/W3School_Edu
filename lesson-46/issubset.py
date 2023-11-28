# Agar to'plamdagi barcha elementlar xto'plamda mavjud bo'lsa, True qiymatini qaytaring y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

print('-----------------------------------------------------------------------------')

# Agar to'plamdagi barcha elementlar xto'plamda mavjud bo'lmasa, False qiymatini qaytaring y:

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}

z = x.issubset(y)

print(z)