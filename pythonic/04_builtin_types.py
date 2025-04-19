# --------------------------------------------------------
# 🧱 Pythonic Use of Built-in Types: list, dict, set, tuple
# --------------------------------------------------------

# Python gives us 4 core built-in collection types:
# - list: ordered, mutable, allows duplicates
# - dict: key-value pairs, fast lookup
# - set: unordered, unique items
# - tuple: ordered, immutable

# Knowing *when and how* to use them is key to writing Pythonic code.

# --------------------------------------------------------
# 📦 list — ordered, mutable, allows duplicates
# --------------------------------------------------------

# ✅ Idiomatic list usage:
names = ["Adrian", "Adrian", "Adrian"]

# ❌ Un-Pythonic:
names = list()
names.append("Adrian")
names.append("Adrian")
names.append("Adrian")

# ^ looks ass by the way. 

# ✅ Pythonic way to build or transform:
squares = [n ** 2 for n in range(10) if n % 2 == 0]

# ✅ Useful built-ins:
# len(), sorted(), reversed(), enumerate(), zip(), map()

# Pythonic unpacking:
first, second, *rest = names

# --------------------------------------------------------
# 🧭 enumerate() over range(len(...)) — always
# --------------------------------------------------------

# ❌ Old-school, un-Pythonic:
for i in range(len(names)):
    print(i, names[i])

# ✅ Pythonic:
for i, name in enumerate(names):
    print(i, name)

# --------------------------------------------------------
# 🧩 tuple — like a list, but immutable
# --------------------------------------------------------

# Tuples are great for:
# - fixed structure data
# - function return values
# - dictionary keys

# Example:
coords = (3, 5)

# ✅ Tuple unpacking:
x, y = coords

# ✅ Used to return multiple values:
def divide(x, y):
    return x // y, x % y

quotient, remainder = divide(17, 5)

# --------------------------------------------------------
# 🧺 dict — key-value pairs with fast lookup
# --------------------------------------------------------

# ✅ Idiomatic dict:
user = {
    "username": "adrian",
    "active": True,
    "roles": ["admin", "editor"],
}

# ✅ Dictionary comprehension:
squares = {n: n**2 for n in range(5)}

# ✅ Use .get() to avoid KeyErrors:
email = user.get("email", "<not set>")

# ✅ Unpacking dicts as kwargs:
def greet(name, greeting="hi"):
    print(f"{greeting}, {name}!")

options = {"name": "Adrian", "greeting": "Hello.👋"}
greet(**options)

# --------------------------------------------------------
# 🧪 set — unordered, unique elements
# --------------------------------------------------------

# Sets are great for:
# - removing duplicates
# - fast membership checks
# - set algebra (union, intersection, etc.)

# ✅ Creating a set:
unique_values = set([1, 2, 2, 3, 4, 4, 4])

# ✅ Set operations:
a = {1, 2, 3}
b = {3, 4, 5}

intersection = a & b      # {3}
union = a | b             # {1, 2, 3, 4, 5}
difference = a - b        # {1, 2}
symmetric = a ^ b         # {1, 2, 4, 5}

# ✅ Membership is O(1):
if 3 in a:
    print("3 is in set a")

# --------------------------------------------------------
# ⚠️ Anti-patterns
# --------------------------------------------------------

# ❌ Using list for set-like behavior:
tags = ["python", "dev", "python", "code"]
unique_tags = list(set(tags))  # ✅ but consider starting with a set if order doesn't matter

# ❌ Using dict for structured data instead of dataclasses/namedtuples:
person = {"name": "Adrian", "age": 15}
# ✅ Better__ - ⬇️
from collections import namedtuple
Person = namedtuple("Person", ["name", "age"])
alice = Person(name="Adrian", age=15)

# Or:
# from dataclasses import dataclass

# --------------------------------------------------------
# ✅ Recap: Be intentional
# --------------------------------------------------------

# - Use list when you care about order or duplicates
# - Use tuple when values are fixed (coords, RGB, return vals)
# - Use dict when mapping values by keys
# - Use set when you need uniqueness or set math

# Choose based on semantics — Pythonic = "clear intent"
