# argumentga 10 qo'shing ava natijani qaytaring:

x = lambda a : a + 10
print(x(5))


fullname = lambda name: f"{name} Xurramov"
print(fullname("Otabek"))

print('---------------------------------------')

# a argumentni b argument bilan ko'paytiring va natijani qaytaring:

x = lambda a, b : a * b
print(x(5, 6))

fullname = lambda name , surname :f"{name} {surname}"
print(fullname("Otabek" , "Xurramov"))

print('---------------------------------------------------')
# Misol
# a,b ,c argumentini umumlashtiring natijani qaytaring:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print('---------------------------------------------------')

def myfunc(n):
  return lambda a : a * 2

my = myfunc()

print(my(7))

print('----------------------------------------------------')

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

print('---------------------------------------------------------')
# Yoki siz yuborgan raqamni har doim uch baravar oshiradigan funktsiyani yaratish uchun bir xil funktsiya ta'rifidan foydalaning :
#
# Misol
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

print('-------------------------------------------------------------------------')

# Yoki ikkala funksiyani bir xil dasturda bajarish uchun bir xil funksiya taʼrifidan foydalaning:
#
# Misol
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


def myfunction(name):
    return f"{name}"

func = myfunc()




def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

# mydoubler = lambda 11:11*2
print(mydoubler(11))
