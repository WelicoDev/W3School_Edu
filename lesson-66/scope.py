# Funktsiya ichida yaratilgan o'zgaruvchi ushbu funktsiya ichida mavjud:

def myfunc():
  x = 300
  print(x)

myfunc()

print('---------------------------------------------------------------------------')

# Mahalliy o'zgaruvchiga funksiya ichidagi funksiyadan kirish mumkin:

def myfunc():
  x = 300
  def myinnerfunc():
    print("x = " ,x)
  myinnerfunc()

myfunc()

print('-------------------------------------------------------------------------------')

# Funktsiyadan tashqarida yaratilgan o'zgaruvchi global bo'lib, har kim foydalanishi mumkin:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

print('---------------------------------------------------------------------------------------')

# Funktsiya mahalliyni x, so'ngra kod globalni chop etadi x:

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

print('------------------------------------------------------------------------------------------')

# Agar siz globalkalit so'zdan foydalansangiz, o'zgaruvchi global qamrovga tegishli:

def myfunc():
  global x
  x = 500

myfunc()

print(x)

print('----------------------------------------------------------------------------------------------')

# Funktsiya ichidagi global o'zgaruvchining qiymatini o'zgartirish uchun kalit so'z yordamida o'zgaruvchiga murojaat qiling global:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)