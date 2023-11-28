# Agar to'plamda barcha elementlar ymavjud bo'lsa, True qiymatini qaytaring x:

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

print('---------------------------------------------------------')

# Agar to'plamdagi barcha elementlar yto'plamda mavjud bo'lmasa, False qiymatini qaytaring x:

x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)