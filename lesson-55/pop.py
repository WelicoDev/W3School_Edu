# Lug'atdan "model" ni olib tashlang:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

print('---------------------------------------------')

# O'chirilgan elementning qiymati pop() usulining qaytish qiymatidir:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")

print(x)