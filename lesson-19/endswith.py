# Satr tinish belgisi (.) bilan tugashini tekshiring:

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

name = input("Firstname >>")
surname = input("Lastname >>")
if surname.endswith("va"):
    print("ayol")
else:
    print("erkak")

# Ta'rifi va qo'llanilishi
# Usul endswith(), agar satr belgilangan qiymat bilan tugasa, True qiymatini qaytaradi, aks holda False.

# Sintaksis
# string.endswith(value, start, end)