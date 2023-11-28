# Misol

x = "Hello World!"

print(len(x))

print('---------------------------------------------------------------------')

# Tuple
# Kortejlar uchun len()kortejdagi elementlar sonini qaytaradi:
#
# Misol

mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

print('------------------------------------------------------------------------')

# Lug'at
# Lug'atlar uchun len()lug'atdagi kalit/qiymat juftlari sonini qaytaradi:
#
# Misol

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964 ,
  "color": "white",
}

print(len(thisdict))

print('----------------------------------------------------------------------')

# Sinf polimorfizmi
# Polimorfizm ko'pincha Class usullarida qo'llaniladi, bu erda biz bir xil usul nomi bilan bir nechta sinflarga ega bo'lishimiz mumkin.
#
# Masalan, bizda uchta sinf bor deylik: Car, Boat, va Plane, va ularning barchasida , deb nomlangan usul bor move():
#
# Misol
# Xuddi shu usul bilan turli sinflar:


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

print('----------------------------------------------------------------------------------------------------------------')
print('Vehicle nomli klass yaratib Car , Boat , Plane meros qoldirish mumkin !')
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
  print('-----------------------')