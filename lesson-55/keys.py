# Python Dictionary kalitlari() usuli
#
# MisolO'zingizning Python serveringizni oling
# Kalitlarni qaytaring:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)

print('---------------------------------------------')

# Lug'atga biror narsa qo'shilsa, ko'rish ob'ekti ham yangilanadi:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"

print(x)