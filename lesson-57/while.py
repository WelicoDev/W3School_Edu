# i 6 dan kichik bo'lsa, i ni chop eting:

i = 1
while i < 6:
  print(i)
  i += 1


print('------------------------------------------------')

# Misol
# i 3 bo'lganda sikldan chiqing:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


print('------------------------------------------------')

# Misol
# Agar i 3 bo'lsa, keyingi iteratsiyaga o'ting:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print('--------------------------------------------------')

# Misol
# Shart noto'g'ri bo'lsa, xabarni chop eting:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")