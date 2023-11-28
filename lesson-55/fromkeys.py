# Misol
# 3 ta tugma bilan lug'at yarating, ularning barchasi 0 qiymatiga ega:

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

print('--------------------------------------------------')

# Yuqoridagi misol, lekin qiymatni ko'rsatmasdan:

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)