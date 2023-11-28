# Misol
# "Model" elementining qiymatini oling:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

print('-------------------------------------------')

# Mavjud bo'lmagan elementning qiymatini qaytarishga harakat qiling:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)