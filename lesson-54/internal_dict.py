# Misol
# Uchta lug'atdan iborat lug'at yarating:

myfamily = {
  "child1" : {
    "name" : "Otabek",
    "year" : 2004
  },
  "child2" : {
    "name" : "Islom",
    "year" : 2007
  },
  "child3" : {
    "name" : "Farangiz",
    "year" : 2011
  }
}

print(myfamily)

print('-----------------------------------------------------------')

# Misol
# Uchta lug'at yarating, so'ngra qolgan uchta lug'atni o'z ichiga olgan bitta lug'at yarating:

child1 = {
  "name" : "Otabek",
  "year" : 2004
}
child2 = {
  "name" : "Javohir",
  "year" : 2007
}
child3 = {
  "name" : "Madina",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

print('--------------------------------------------------------')

# 2-bolaning ismini chop eting:

print(myfamily["child2"]["name"])