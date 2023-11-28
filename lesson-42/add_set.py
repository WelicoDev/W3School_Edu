# Quyidagi usul yordamida to'plamga element qo'shing add() :

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# To'plamlarni qo'shish
# Joriy to'plamga boshqa to'plamdan elementlar qo'shish uchun update() usuldan foydalaning.
#
# Misol
# dan elementlar tropicalqo'shing thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


print('----------------------------------------------------------------------------------------')

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)