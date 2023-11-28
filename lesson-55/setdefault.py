# Misol
# "Model" elementining qiymatini oling:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

print('------------------------------------------------')

# "Rang" elementining qiymatini oling, agar "rang" elementi mavjud bo'lmasa, "rang" ni "oq" qiymati bilan kiriting:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)