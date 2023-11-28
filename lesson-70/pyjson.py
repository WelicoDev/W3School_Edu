# json modulini import qiling:

import json

# Misol
print('JSON-dan Python-ga aylantirish:')


# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

print(y)
# the result is a Python dictionary:
print(y["age"])


print('---------------------------------------------------------------------------------------------------------------')

print('Python-dan JSON-ga aylantirish:')

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)