# Faylning bir qatorini o'qing:

f = open("demofile.txt", "r")

print(f.readline())

print(f.readline())

print('------------------------------------------------')


# Fayl satrlari bo'ylab aylanish orqali siz butun faylni satrga qarab o'qishingiz mumkin:
#
# Misol
# Faylni satr bo'yicha aylantiring:

f = open("demofile.txt", "r")
for x in f:
  print(x)

print('----------------------------------------------------------------------------------')

# Ishni tugatgandan so'ng faylni yoping:

f = open("demofile.txt", "r")
print(f.readline())
f.close()

