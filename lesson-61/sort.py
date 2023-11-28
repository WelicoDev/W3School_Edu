# Ro'yxatni alifbo tartibida tartiblang:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)

print('---------------------------------------')

# Misol
# Ro'yxatni kamayishiga qarab tartiblang:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)

print('---------------------------------------')

# Misol
# Ro'yxatni qiymatlar uzunligi bo'yicha tartiblang:

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print('----------------------------------------')

# Misol
# Lug'atlar ro'yxatini lug'atlarning "yil" qiymatiga qarab tartiblang:

# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)

print('----------------------------------------------')

# Ro'yxatni qiymatlar uzunligi bo'yicha tartiblang va teskari:

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)