# --------------------------------------------------------
# 🐍 Pythonic Idioms and Anti-Patterns
# --------------------------------------------------------

# Python offers a rich set of language features that let us write clean,
#      expressive code. Let's explore some common anti-patterns — and their
#         more Pythonic alternatives.

# --------------------------------------------------------
# ❌ Anti-pattern: Manual looping with indexing
# ✅ Idiomatic: Use `enumerate()`
# --------------------------------------------------------

# Imagine we want to print each item in a list with its index:

fruits = ["apple", "banana", "cherry"]

# ❌ Un-Pythonic:
for i in range(len(fruits)):
    print(i, fruits[i])

# ✅ Pythonic:
for i, fruit in enumerate(fruits):
    print(i, fruit)

# enumerate() gives us both index and value, more clearly and safely.


# --------------------------------------------------------
# ❌ Anti-pattern: Checking for empty lists with len()
# ✅ Idiomatic: Just use the list in a boolean context
# --------------------------------------------------------

# ❌
if len(fruits) > 0:
    print("we have fruits!!")

# ✅
if fruits:
    print("we have fruits!!")

# Empty containers evaluate to False in Python <-- clean & expressive


# --------------------------------------------------------
# ❌ Anti-pattern: Using temporary variables for swaps
# ✅ Idiomatic: Tuple unpacking
# --------------------------------------------------------
 
a = 1 
b = 2

# ❌
temp = a
a = b
b = temp

# ✅
a, b = b, a

# Python lets you swap values in a single, readable line.


# --------------------------------------------------------
# ❌ Anti-pattern: Building lists with .append() in a loop
# ✅ Idiomatic: Use list comprehensions
# --------------------------------------------------------

# Suppose we want the square of every number from 0 to 9.

# ❌
squares = []
for i in range(10):
    squares.append(i ** 2)

# ✅
squares = [i ** 2 for i in range(10)]

# List comprehensions are more compact and often more readable.


# --------------------------------------------------------
# ❌ Anti-pattern: Chained `if` statements for simple mappings
# ✅ Idiomatic: Use dictionaries
# --------------------------------------------------------

# Let's say we want to convert status codes to messages:

# ❌
status = 404
if status == 200:
    message = "OK"
elif status == 404:
    message = "Not Found"
elif status == 500:
    message = "Server Error"
else:
    message = "N/A"

# ✅
messages = {
    200: "OK",
    404: "Not Found",
    500: "Server Error"
}
message = messages.get(status, "N/A")

# simply way better ( subjective, but i don't see an argument that would speak against it) __<-- it's cleaner, gives a faster lookup & is easier to extend / maintain.


# --------------------------------------------------------
# Summary
# --------------------------------------------------------

# The idiomatic Python mindset is:
# - Use built-in functions and patterns
# - Prefer clarity over cleverness
# - Avoid reinventing what's already elegant in the language
