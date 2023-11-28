fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

print('---------------------------------------------------------')
# 2-usul

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
print('------------------------------------------------------------------------')
name = ["Otabek" , 'Zohidjon' , 'Javohir' , 'Islom' , 'Ozodbek' , 'Suhrob' , 'Jonibek' , 'Dilsora']
group = [n for n in name if "a" in n]
print(group)

print('-------------------------------------------------------------------------')

# newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

print('-----------------------------------------------------------')

newlist = [x for x in range(10)]

print(newlist)

print('---------------------------------------------------------------')
newlist = [x for x in range(10) if x < 5]

print(newlist)


print('-----------------------------------------------------------------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

print('-----------------------------------------------------------------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

print('----------------------------------------------------------------')

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

# Yuqoridagi misoldagi ibora shunday deydi:
#
# "Agar banan bo'lmasa, uni qaytaring, agar banan bo'lsa, apelsinni qaytaring".