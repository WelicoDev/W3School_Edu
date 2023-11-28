# Misol
def my_function():
  print("Hello from a function")

my_function()

print('----------------------------------------------------------------')

# Misol
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

print('---------------------------------------------------------------')

# Misol
# Bu funksiya 2 ta argumentni kutadi va 2 ta argumentni oladi:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

print('---------------------------------------------------------------')


# Misol
# Agar argumentlar soni noma'lum bo'lsa, *parametr nomidan oldin a qo'shing:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

print('-----------------------------------------------------------------')

# Shunday qilib, argumentlar tartibi muhim emas.
#
# Misol
def my_function(child3, child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print('---------------------------------------------------------------------')

# Agar kalit so'z argumentlari soni noma'lum bo'lsa, **parametr nomidan oldin ikkita qo'shing:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

print('----------------------------------------------------------------------------')

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Misol
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print('-------------------------------------------------------------------')


# Funktsiyaga qiymat qaytarishiga ruxsat berish uchun quyidagi return bayonotdan foydalaning:

# Misol
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

print('---------------------------------------------------------------------------')

# Rekursiyaga misol

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)