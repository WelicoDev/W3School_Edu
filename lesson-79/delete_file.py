# "demofile.txt" faylini olib tashlang:

import os
os.remove("demofile.txt")

# Fayl mavjudligini tekshiring, keyin uni o'chiring:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

print('--------------------------------------------')

# "Mening papkam" jildini olib tashlang:

import os
os.rmdir("myfolder")