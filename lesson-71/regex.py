# "The" bilan boshlanib, "Spain" bilan tugashini bilish uchun qatorni qidiring:

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print('-----------------------------------------------------------------------')

# Barcha mosliklar roʻyxatini chop eting:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Ro'yxatda ular topilgan tartibda mosliklar mavjud.
#
# Hech qanday moslik topilmasa, bo'sh ro'yxat qaytariladi:
#
# Misol
# Hech qanday moslik topilmasa, bo'sh ro'yxatni qaytaring:

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

print('-------------------------------------------------------------------')

# Satrdagi birinchi bo'sh joy belgisini qidiring:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# Hech qanday moslik topilmasa, qiymat Noneqaytariladi:
#
# Misol
# Hech qanday mos kelmaydigan qidiruvni amalga oshiring:

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

print('------------------------------------------------------------------------')

# Split() funktsiyasi
# Funktsiya split()har bir o'yinda satr bo'lingan ro'yxatni qaytaradi:
#
# Misol
# Har bir bo'sh joy belgisiga bo'ling:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

for n in x:
    print(n)


print('---------------------------------------------------------------------------')

# Parametrni belgilash orqali hodisalar sonini boshqarishingiz mumkin maxsplit :
#
# Misol
# Satrni faqat birinchi marta ajrating:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


print('-----------------------------------------------------------------------------------')

# Sub() funktsiyasi
# Funktsiya sub()mosliklarni siz tanlagan matn bilan almashtiradi:
#
# Misol
# Har bir bo'sh joy belgisini 9 raqami bilan almashtiring:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

print('---------------------------------------------------------------------------------------')

# Siz parametrni belgilash orqali almashtirishlar sonini boshqarishingiz mumkin count :
#
# Misol
# Birinchi 2 ta holatni almashtiring:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

print('-----------------------------------------------------------------------------------------')

# Misol
# Mos ob'ektni qaytaradigan qidiruvni bajaring:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


print('--------------------------------------------')

# Muntazam ibora "S" bosh harfi bilan boshlangan har qanday so'zlarni qidiradi:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x)
print(x.span())

print('-------------------------------------------------------------------------')

# Funktsiyaga kiritilgan satrni chop eting:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

print('--------------------------------------------------------------------------')

# Muntazam ibora "S" bosh harfi bilan boshlangan har qanday so'zlarni qidiradi:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())