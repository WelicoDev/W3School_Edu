# Matnning qayerida "casa" satri oxirgi marta uchraydi?:

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

print('--------------------------------------')

txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)

print('---------------------------------------------')
txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)

print('-------------------------------------------')

txt = "Hello, welcome to my world."

print(txt.rfind("q"))
print(txt.rindex("q"))