# Satrni verguldan so'ng bo'sh joy (, ) qo'yib, ro'yxatga ajrating:

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

print("Satrni maksimal 2 ta elementdan iborat roʻyxatga ajrating:")

txt = "apple, banana, cherry"

print("#setting the maxsplit parameter to 1, will return a list with 2 elements!")
x = txt.rsplit(", ", 1)

print(x)
