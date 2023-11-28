# Misol
# Blok tryistisno hosil qiladi, chunki xaniqlanmagan:

# x = "Assalom aleykum"
try:
  print(x)
except:
  print("An exception occurred")

print('---------------------------------------------------------')

# Agar try bloki a NameErrorva boshqa xatolarni ko'tarsa, bitta xabarni chop eting:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


print('-----------------------------------------------------------')

# Boshqa
# elseHech qanday xatolik yuzaga kelmasa, bajariladigan kod blokini aniqlash uchun kalit so'zdan foydalanishingiz mumkin :
#
# Misol
# Ushbu misolda tryblok hech qanday xato yaratmaydi:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print('----------------------------------------------------------------')

# Nihoyat
# Blok finally, belgilangan bo'lsa, urinib ko'rish bloki xatolik tug'diradimi yoki yo'qmi, qat'iy nazar bajariladi.
#
# Misol
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


print('------------------------------------------------------------------------------------------------')
# Misol
# Yozish mumkin bo'lmagan faylni ochishga va unga yozishga harakat qiling:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

print('-----------------------------------------------------------------------------')

# Xatoni ko'taring va agar x 0 dan past bo'lsa, dasturni to'xtating:

# x = -1
#
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

print('---------------------------------------------------------------------------------')

# Agar x butun son bo'lmasa, TypeErrorni ko'taring:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")