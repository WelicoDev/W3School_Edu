# Usul pop()belgilangan kalit nomi bilan elementni olib tashlaydi:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

print('---------------------------------------------------')

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

print('---------------------------------------------------------')

# Kalit delso'z belgilangan kalit nomi bilan elementni olib tashlaydi:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

print('-------------------------------------------')

# Usul clear()lug'atni bo'shatadi:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)