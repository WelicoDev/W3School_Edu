# "demofile2.txt" faylini oching va faylga tarkibni qo'shing:

f = open("demofile2.txt", "a")
f.write("Assalom aleykum WelicoDev !")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

print('----------------------------------------------------')
# "demofile3.txt" faylini oching va tarkibni qayta yozing:

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

print('-----------------------------------------------------')

# Misol
# "myfile.txt" nomli fayl yarating:

f = open("myfile.txt", "x")


f.write("You are Python Backend developer")

f.close()