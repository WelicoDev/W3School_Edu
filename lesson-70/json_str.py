# Misol
# Python obyektlarini JSON satrlariga aylantiring va qiymatlarni chop eting:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print('----------------------------------------------------------------------------')

# Misol
# Barcha qonuniy ma'lumotlar turlarini o'z ichiga olgan Python ob'ektini aylantiring:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x , indent=4 , separators=(". ", " = ") , sort_keys=True))
