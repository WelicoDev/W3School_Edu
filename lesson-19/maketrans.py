txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

print('-----------------------------------')
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

print('------------------------------------')

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(str.maketrans(x, y, z))
