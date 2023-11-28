
# Satr oxiridagi oq bo'shliqlarni olib tashlang:

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

print('-----------------------------------------')
txt = "banana,,,,,ssqqqww....."

x = txt.rstrip(",.qsw")

print(x)