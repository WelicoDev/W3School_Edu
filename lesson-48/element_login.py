# "Model" kalitining qiymatini oling:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

print(x)
print('----------------------------------------')

x = thisdict.get("model")

print(x)
print('-------------------------------------------')


# Kalitlar ro'yxatini oling:

x = thisdict.keys()

print(x)

# Asl lug'atga yangi element qo'shing va kalitlar ro'yxati ham yangilanishini ko'ring:
print('----------------------------------------')
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


# Usul values()lug'atdagi barcha qiymatlar ro'yxatini qaytaradi.
#
# Misol
# Qadriyatlar ro'yxatini oling:

x = thisdict.values()

print(x)

print('----------------------------------------------------------')

# Asl lug'atga o'zgartirish kiriting va qiymatlar ro'yxati ham yangilanishini ko'ring:

car = {
"brand": "Ford",
"model": "Mustang",




"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x)

print('----------------------------------------------------------------')
# Asl lug'atga yangi element qo'shing va qiymatlar ro'yxati ham yangilanishini ko'ring:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

print('--------------------------------------------')
x = thisdict.items()
print(x)

for n in x:
  print(n)

print('-------------------------------------------------')

# Asl lug'atga o'zgartirish kiriting va elementlar ro'yxati ham yangilanishini ko'ring:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

print('------------------------------------------------------------')\

# Asl lug'atga yangi element qo'shing va elementlar ro'yxati ham yangilanishini ko'ring:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

print('---------------------------------------------------')

# Lug'atda "model" mavjudligini tekshiring:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

