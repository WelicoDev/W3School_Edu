thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

print('----------------------------------')


thisset = {"apple", "banana", "cherry"}

thisset.discard("apple")

print(thisset)


print('-----------------------------------------')

# Usul yordamida tasodifiy elementni olib tashlang pop() :

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



# Usul clear() to'plamni bo'shatadi:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


print('--------------------------------------------')

# Misol
# Kalit delso'z to'plamni butunlay o'chirib tashlaydi:

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)