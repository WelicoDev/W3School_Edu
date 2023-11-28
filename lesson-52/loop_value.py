thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Lug'atdagi barcha asosiy nomlarni birma-bir chop eting:

for x in thisdict:
  print(x)

print('--------------------------------------------------')
# Lug'atdagi barcha qiymatlarni birma-bir chop eting:

for x in thisdict:
  print(thisdict[x])


print('-------------------------------------------------------')

# Misol
# values()Lug'at qiymatlarini qaytarish uchun usuldan ham foydalanishingiz mumkin :

for x in thisdict.values():
  print(x)

print('---------------------------------------------------------')

# Misol
# keys()Lug'at kalitlarini qaytarish uchun siz quyidagi usuldan foydalanishingiz mumkin :

for x in thisdict.keys():
  print(x)

print('------------------------------------------------------------')

# Misol
# Usuldan foydalanib, ikkala kalit va qiymatlar bo'ylab aylantiring items():

for x, y in thisdict.items():
  print(x, y)