# --------------------------------------------------------
# 🧠 Iterators and Generators: Writing Memory-Efficient Pythonic Code
# --------------------------------------------------------

# In Python, an iterator is any object that implements the __iter__() and __next__() methods.
# Iterators allow you to traverse through all the elements in a collection, like a list or tuple,
# without having to store the entire collection in memory at once.

# A generator is a special type of iterator that is defined with a function using the 'yield' keyword.

# --------------------------------------------------------
# ✅ What Makes Generators Pythonic?
# --------------------------------------------------------

# Generators provide a memory-efficient way to handle large data sets.
# Instead of returning a complete list, they yield items one by one, on-demand.

# Example: A generator that yields squares of numbers
def square_numbers(n: int):
    for i in range(n):
        yield i ** 2  # Yielding instead of returning

# Using the generator:
squares = square_numbers(5)

# Iterate over the generator:
for square in squares:
    print(square)

# Output:
# 0
# 1
# 4
# 9
# 16

# Notice that the generator doesn't generate all squares at once, only when we iterate over it.

# --------------------------------------------------------
# ✅ Advantages of Generators Over Lists
# --------------------------------------------------------

# - Generators are more memory-efficient, especially for large datasets.
# - They can represent infinite sequences (e.g., Fibonacci series).
# - They allow lazy evaluation, meaning they only produce values when needed.

# --------------------------------------------------------
# ✅ Writing a Generator Function
# --------------------------------------------------------

# Generator functions are written just like regular functions, but they use the 'yield' keyword.
# When the 'yield' statement is called, the function returns a value and pauses. 
# The function’s state is saved, and when the generator is resumed, it continues from where it left off.

def count_up_to(max: int):
    count = 1
    while count <= max:
        yield count
        count += 1

# Create a generator object:
counter = count_up_to(5)

# Iterate over the generator:
for num in counter:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5

# --------------------------------------------------------
# ✅ Using Generator Expressions
# --------------------------------------------------------

# Generator expressions are like list comprehensions, but instead of returning a list, they return a generator.
# Syntax: (expression for item in iterable)

# Example: Generator expression for squares:
gen = (x ** 2 for x in range(5))

# This doesn't create a list; instead, it returns a generator that we can iterate over:
for value in gen:
    print(value)

# Output:
# 0
# 1
# 4
# 9
# 16

# --------------------------------------------------------
# ✅ Combining Iterators and Generators for Efficiency
# --------------------------------------------------------

# You can combine iterators and generators with tools from the 'itertools' module.
# For example, 'itertools.count()' is an infinite iterator that generates an unbounded sequence.

import itertools

# Use itertools.count() to create an infinite sequence of numbers
counter = itertools.count(10, 5)  # Starts at 10, increments by 5

for _ in range(5):  # Print the first 5 values
    print(next(counter))

# Output:
# 10
# 15
# 20
# 25
# 30

# --------------------------------------------------------
# ✅ Using Generators to Process Large Files
# --------------------------------------------------------

# Generators are particularly useful for reading and processing large files.
# Instead of loading the entire file into memory, we can process each line one at a time.

def read_large_file(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Yield each line one by one

# For demonstration, let's assume we have a large file:
# (For testing, you can use any large text file on your system)

# generator = read_large_file('large_text_file.txt')
# for line in generator:
#     print(line)

# --------------------------------------------------------
# ✅ Key Takeaways:
# --------------------------------------------------------

# - Generators allow for lazy evaluation and are more memory-efficient.
# - They are useful for processing large data sets or infinite sequences.
# - Use the 'yield' keyword to create generators in Python.
# - Use itertools and generator expressions for concise, efficient code.
