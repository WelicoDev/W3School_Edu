fruits = ("apple", "banana", "cherry")
print(fruits)

# Ammo, Python-da bizga qiymatlarni o'zgaruvchilarga qaytarishga ruxsat beriladi. Bunga "ochish" deyiladi:
#
# Misol
# Tupleni ochish:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


print('------------------------------------------------------------')

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

print('------------------------------------------------------------')

# Agar yulduzcha boshqa oʻzgaruvchi nomiga oxirgisidan koʻra qoʻshilsa, qolgan qiymatlar soni qolgan oʻzgaruvchilar soniga toʻgʻri kelguncha Python oʻzgaruvchiga qiymatlarni tayinlaydi.
#
# Misol
# "Tropik" o'zgaruvchiga qiymatlar ro'yxatini qo'shing:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
