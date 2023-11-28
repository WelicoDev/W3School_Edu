# Ikkala to'plamda mavjud bo'lgan elementlarni o'z ichiga olgan to'plamni qaytaring xva o'rnating y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

print('---------------------------------------------------------')

# 3 to'plamni solishtiring va barcha 3 to'plamda mavjud bo'lgan narsalar bilan to'plamni qaytaring:

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)