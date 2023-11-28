# Ikkala to'plamdagi barcha elementlarni o'z ichiga olgan to'plamni qaytaring, dublikatlar bundan mustasno:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)

print('--------------------------------------------------------')

# Misol
# 2 dan ortiq to'plamni birlashtiring:

x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)

print(result)