# Ro'yxatni alifbo tartibida tartiblang:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print('--------------------------------------------------------')

# Ro'yxatni raqamlar bo'yicha tartiblang:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
print('----------------------------------------------------------------------')

# Kamaytirish bo'yicha tartiblash uchun argument kalit so'zidan foydalaning reverse = True:
# Ro'yxatni kamayishiga qarab tartiblang:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


print('------------------------------------------------------------')
# Ro'yxatni kamayishiga qarab tartiblang:

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

print('-------------------------------------------------------------')

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print('----------------------------------------------------------------')
# Katta-kichik harflarga qarab tartiblash kutilmagan natija berishi mumkin:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

print('------------------------------------------------------------------')

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Ro'yxat elementlarining tartibini o'zgartiring:
print('-------------------------------------------------')

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)