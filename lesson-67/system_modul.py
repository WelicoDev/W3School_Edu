# O'rnatilgan modullar
# Python-da bir nechta o'rnatilgan modullar mavjud bo'lib, ularni xohlagan vaqtda import qilishingiz mumkin.

# Misol
# Modulni import qiling va foydalaning platform:

import platform

x = platform.system()

print(x)

# Platforma moduliga tegishli barcha belgilangan nomlarni sanab o'ting:

import platform

x = dir(platform)

print(x)