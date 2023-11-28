thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

print('-----------------------------------------------')

# Misol
# Barcha elementlarni indeks raqamiga qarab chop eting:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(f"value{i+1} >> ",thislist[i])

# Yuqoridagi misolda yaratilgan iterativ hisoblanadi [0, 1, 2].
print('---------------------------------------------------')
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


print('--------------------------------------------------------')

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print('----------------------------------------------------------------')

cars = ['malibu' , 'gentra' , 'cobalt' , 'byd' , 'ferarri' , 'nexia' , 'tracker']
[print(y) for y in cars]