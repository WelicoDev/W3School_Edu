# X nomli xususiyatga ega MyClass nomli sinf yarating:

class MyClass:
  x = 20

MyClass()


# Misol
# value1 nomli ob'ekt yarating va x qiymatini chop eting:

value1 = MyClass()
print(value1.x)

# Person nomli sinf yarating, ism va yosh uchun qiymatlarni belgilash uchun __init__() funksiyasidan foydalaning:

print('----------------------------------------------------')

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

value = Person("John", 36)

print(value.name)
print(value.age)

print('------------------------------------------------------')

class Poople:
    def __init__(self , first_name , last_name , age , gender , address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address

myvalue = Poople("Otabek" , "Xurramov" , 20 , 'male' , "Olmazor , Tashkent")

print(myvalue.age)

print('-------------------------------------------------------------')


# Misol
# __str__() funksiyasi BO‘LMAGAN obyektning satrli tasviri:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

value = Person("John", 36)

print(value)

print('-----------------------------------------------------------')

# Misol
# __str__() funksiyasi BILAN ob'ektning qator ko'rinishi:

class Person:
  def __init__(self, name,surname ,  age):
    self.name = name
    self.surname = surname
    self.age = age

  def __str__(self):
    return f"{self.name}  {self.surname}"

value = Person("Otabek", "Xurramov" , 20)

print(value)

print('--------------------------------------------------------')

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

value = Person("John", 36)
value.myfunc()

print('Eslatma: Parametr selfsinfning joriy nusxasiga havola bo\'lib, sinfga tegishli o\'zgaruvchilarga kirish uchun ishlatiladi.')


print('-----------------------------------------------------------------------------------------------------------------')

# self o'rniga mysillyobject va abc so'zlarini ishlating :

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

print('------------------------------------------------------------------')

# Misol
class Person:
  pass

