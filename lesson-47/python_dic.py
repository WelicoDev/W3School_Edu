# Misol
# Lug'at yaratish va chop etish:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


print('-------------------------------------------')

# Lug'atning "brend" qiymatini chop eting:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


print('--------------------------------------------')

# Ikki nusxadagi qiymatlar mavjud qiymatlarni qayta yozadi:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print('-------------------------------------------------')

print(len(thisdict))

# Misol
# String, int, boolean va list ma'lumotlar turlari:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

print('-------------------------------------------------')


# Lug'atning ma'lumotlar turini chop eting:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

print('------------------------------------------------')

# Lug'at yaratish uchun dict() usulidan foydalanish:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)