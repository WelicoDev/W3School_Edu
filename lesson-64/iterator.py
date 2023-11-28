# Kortejdan iteratorni qaytaring va har bir qiymatni chop eting:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print('---------------------------------------------------------')

# Satrlar, shuningdek, belgilar ketma-ketligini o'z ichiga olgan takrorlanadigan ob'ektlardir:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print('----------------------------------------------------------')

# Iterator orqali aylanish
# Biz fortakrorlanadigan ob'ektni takrorlash uchun tsikldan ham foydalanishimiz mumkin:
#
# Misol
# Kortej qiymatlarini takrorlang:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

print('---------------------------------------------------------')

# Misol
# Satr belgilarini takrorlang:

mystr = "banana"

for x in mystr:
  print(x)

print('---------------------------------------------------------------')

# Misol
# 1 dan boshlab raqamlarni qaytaruvchi iterator yarating va har bir ketma-ketlik bittaga ko'payadi (qaytaruvchi 1,2,3,4,5 va hokazo):

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print('------------------------------------------------------------')

# Misol
# 20 ta takrorlashdan keyin to'xtating:

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)