
# Ikkalasida ham mavjud bo'lgan narsalarni olib tashlang x va y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

print('---------------------------------------------------------------')

# 3 to'plamni solishtiring va barcha 3 to'plamda mavjud bo'lgan narsalar bilan to'plamni qaytaring:

x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)
