# Har bir mevani mevalar ro'yxatida chop eting:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print('--------------------------------')

# Misol
# "Banan" so'zidagi harflarni aylantiring:

for x in "banana":
  print(x)

print('-----------------------------------------')

# x  "Banan" bo'lganda sikldan chiqing :

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print('----------------------------------------------')
# Misol
# "Banan" bo'lganda tsikldan chiqing x, lekin bu safar tanaffus chop etishdan oldin keladi:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print('-----------------------------------------------------')

# Bananni chop qilmang:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print('---------------------------------------------------------')

# range() funktsiyasidan foydalanish:

for x in range(6):
  print(x)

print('-----------------------------------------------------------')

# Misol
# Boshlash parametridan foydalanish:

for x in range(2, 6):
  print(x)

print('------------------------------------------------------')

# Misol
# Tartibni 3 ga oshiring (standart 1):

for x in range(2, 30, 3):
  print(x)


print('-----------------------------------------------------------')

# 0 dan 5 gacha bo'lgan barcha raqamlarni chop eting va tsikl tugagandan so'ng xabarni chop eting:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

print('-----------------------------------------------------------')

# Misol
# 3 bo'lganda tsiklni buzing xva elseblok bilan nima sodir bo'lishini ko'ring:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


print('-------------------------------------------------------------')

# Har bir meva uchun har bir sifatni chop eting:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


print('---------------------------------------------------------------')

# Misol
for x in [0, 1, 2]:
  pass