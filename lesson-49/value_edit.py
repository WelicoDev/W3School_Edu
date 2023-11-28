# "Yil" ni 2018 yilga o'zgartiring:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

print(thisdict)

print('------------------------------------')

# Ushbu usul yordamida avtomobilning "yilini" yangilang update() :

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)