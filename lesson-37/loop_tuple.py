# Elementlarni takrorlang va qiymatlarni chop eting:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


print('-------------------------------------------------------------')

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(f"{i+1} - item >> " , thistuple[i])


print('-----------------------------------------------------------------')

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(f"{i+1} - item >> " ,thistuple[i])
  i = i + 1