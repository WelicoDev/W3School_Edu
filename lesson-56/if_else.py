a = 33
b = 200
if b > a:
  print("b is greater than a")


x = 40
y = 10
z = 100

if x>y and x<z:
  print("universal x")


print('-------------------------------------------')

# Elif kalit so'zi Pythonning "agar oldingi shartlar to'g'ri bo'lmagan bo'lsa , bu shartni sinab ko'ring" deyish usulidir.


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print('-----------------------------------------------')


# else kalit so'zi oldingi shartlar bilan ushlanmagan hamma narsani ushlaydi.


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


print('-------------------------------------------------')

# Misol
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print('---------------------------------------------------')

# Bir qator if bayonoti:

if a > b: print("a is greater than b")

print('---------------------------------------------------')

# Agar bajarish kerak bo'lgan bitta buyruq mavjud bo'lsa, bittasi if uchun va biri else uchun, barchasini bir qatorga qo'yishingiz mumkin:
#
# Misol
# Bir satr if else ifodasi:

a = 2
b = 330
print("A") if a > b else print("B")


katta = 20
kichik = 18

print("Assalom aleykum") if katta > kichik else print("Valeykum assalom")

"""Ushbu uslub uchlik operatorlar yoki shartli ifodalar sifatida tanilgan ."""


print('---------------------------------------------')

# Bir satr if else iborasi, 3 shart bilan:

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

print('-----------------------------------------------')

# Agar a dan katta bo'lsa b, AND agar c dan katta bo'lsa, test qiling a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

print('-----------------------------------------------')

# OR
# Kalit orso'z mantiqiy operator bo'lib, shartli gaplarni birlashtirish uchun ishlatiladi:
#
# Misol
# Agar adan katta bo'lsa b, OR agar a dan katta bo'lsa, test qiling c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

print('-----------------------------------------------')

# NOT
# Kalit not so'z mantiqiy operator bo'lib, shartli gapning natijasini teskari o'zgartirish uchun ishlatiladi:
#
# Misol
# a Quyidagidan katta bo'lmasa, sinab ko'ring b:

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


print('--------------------------------------------------')

# Siz bayonotlar ifichida bayonotlarga ega bo'lishingiz mumkin, bu ichkiif iboralar deb ataladi . if
#
# Misol
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

print('-----------------------------------------------------------------------------')

# if bayonotlar bo'sh bo'lishi mumkin emas, lekin agar sizda biron sababga ko'ra ifmazmunsiz bayonot bo'lsa, passxatolikka yo'l qo'ymaslik uchun bayonotni kiriting.
#
# Misol
a = 33
b = 200

if b > a:
  pass