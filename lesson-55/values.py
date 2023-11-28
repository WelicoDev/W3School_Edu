# Python Dictionary values() usuli
#
# Misol
# Qiymatlarni qaytaring:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)

print('-------------------------------------------')

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

car["year"] = 2018

print(x)