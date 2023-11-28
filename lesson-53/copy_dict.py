# Usul bilan lug'at nusxasini yarating copy():

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

print('--------------------------------------')

# Nusxa olishning yana bir usuli - o'rnatilgan funksiyadan foydalanish dict().
#
# Misol
# Funktsiyaga ega lug'at nusxasini yarating dict() :

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)