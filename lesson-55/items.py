# Lug'atning kalit-qiymat juftliklarini qaytaring:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)

print('------------------------------------------------')

# Lug'atdagi element qiymatni o'zgartirganda, ko'rish ob'ekti ham yangilanadi:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)