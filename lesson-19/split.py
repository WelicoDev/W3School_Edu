txt = "welcome to the jungle"

x = txt.split()

print(x)

m , n , p = input("Sonlarni kiriting >> ").split()

print(int(m)+int(p))

print('--------------------------------------------------')

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)

print('----------------------------------------------------')

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)

print('----------------------------------------------------')

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 2)

print(x)