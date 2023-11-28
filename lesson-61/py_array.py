cars = ["malibu" , "gentra" , "byd" , "kia"]

print(cars[0])

x = len(cars)

print(x)

print('-----------------------------------------------')

for car in cars:
    print(car)

cars.append("Honda")

print(cars)

print('-------------------------------------------------')

# Massivning ikkinchi elementini o'chiring cars:

cars.pop(1)
print(cars)

print('------------------------------------------------')

cars.remove("byd")
print(cars)

