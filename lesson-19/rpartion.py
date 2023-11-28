# "Banan" so'zining oxirgi takrorlanishini qidiring va uchta elementdan iborat kortejni qaytaring:
#
# 1 - "o'yin" dan oldingi hamma narsa
# 2 - "o'yin"
# 3 - "o'yin" dan keyin hamma narsa

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

print('---------------------------------')

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("apples")

print(x)