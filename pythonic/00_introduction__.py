# --------------------------------------------------------
# 🐍 Introduction to Pythonic Code
# --------------------------------------------------------

# quite simply put, pythonic code is just writing code that adheres to the conventions and design principles 
#    that make Python a clear, readable, and elegant language. While the term "Pythonic" is often used          <- ^
#       as a shorthand for adhering to PEP8, it encompasses more than just style—it’s about writing code           <- ^
#           that is intuitive, efficient, and well-structured in a way that takes advantage of Python's strengths.     <- ^

# --------------------------------------------------------
# ✅ What is Pythonic Code?
# --------------------------------------------------------

# "Pythonic" code is writing that reflects the core of py
# The goal is to make code that is clean, concise, and easy to understand—taking full advantage of Python’s features.
#                                  ^ clean is probably a factor that is most important to a lot of people, i also like writing pythonic code
#                                                                                           because it just looks better( eyecandy )

# Pythonic code is about:
# - Writing code that is __simple__, not complex or unnecessarily clever.
# - Leveraging Python's built-in tools and libraries for readability and efficiency.
# - Following conventions that make your code consistent with the larger Python "ecosystem".
# - Striking a balance between clarity and compactness.

# Pythonic code often avoids unnecessary complications and keeps things as simple as possible while still being expressive.

# --------------------------------------------------------
# ✅ Why is Pythonic Code Important?
# --------------------------------------------------------

# Writing Pythonic code is important for several reasons:

# 1. --> Readability: Python emphasizes readability. Code is written to be understood easily by others and yourself in the future.
# 2. --> Maintainability: Simple and clear code is easier to maintain and re-work on / refactor
# 3. --> Efficiency: Using Python's built-in features leads to more efficient, faster, and less error-prone code. ( <- most of the time)
# 4. --> Collaboration: When multiple developers work on the same project, using Pythonic patterns can be good for consistency
# 5. --> Ease of Learning: Pythonic code is beginner-friendly because it sticks to the core principles of the language. ( yet most devs don't make use of it lol)

# --------------------------------------------------------
# ✅ What Makes Code _Not_ Pythonic?
# --------------------------------------------------------

# While PEP8 and other Pythonic practices help guide writing Pythonic code, some patterns are *not* Pythonic:
# 1. --> Overcomplicating Things: For example, creating overly complex or convoluted solutions where simpler ones exist ( imo this is an issue a LOT of devs face in general, just writing inefficient,"unnecessary" code)
# 2. --> Reinventing the Wheel: Python comes with an extensive standard lib(s). Rewriting common patterns or functionality without leveraging built-in functions is often un-Pythonic.
# 3. --> Excessive Cleverness: Sometimes developers make their code "clever" (short or tricky) to save space or lines, but at the cost of readability. ( wannabes)

# --------------------------------------------------------
# ✅ Pythonic Code vs. Non-Pythonic Code: Example Comparison
# --------------------------------------------------------

# we can go over some example(s) to understand pythonic <--> non-pythonic code

# __Non-Pythonic Example__:
# Here we try to manually create a list of squares using a for-loop.

numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)  # <- Output: [1, 4, 9, 16, 25]

# __Pythonic Example__:
# Instead of manually appending to a list, Python provides an elegant solution using list comprehensions.

squares = [num ** 2 for num in numbers]

print(squares)  # <- Output: [1, 4, 9, 16, 25]

# ^ more concise, readable, efficient etc..

# --------------------------------------------------------
# ❓ Why Do Many Developers Not Write Pythonic Code?
# --------------------------------------------------------

# Despite the advantages of Pythonic code, there are a few reasons why many developers (especially those new to or those mostly skidding code(e.g. using AI))
# might not write Pythonic code:                                                                                                                               <-^

# 1. __used to other langs__: devs transitioning from other programming languages (like Java, C++, or JavaScript)
#           may find Python's conventions / flexibility unusual, since languages as such often emphasize verbosity / structure rather than simplicity.
# 2. __Overusing "Clever" Code__: Some devs may prioritize brevity, trying to write compact code at the cost of readability. ( as kind of said before )
# 3. --> __Lack of Familiarity with Python's Idioms__: Newcomers to Python may not be aware of some of the tools and idioms that make Pythonic code efficient (e.g., `enumerate()`, `zip()`, list comprehensions).
# 4. __Speed Over Readability__: In some cases, devs might sacrifice readability for performance, especially when working on performance-critical systems. But in Python, this CAN lead to convoluted code that defeats the purpose of the language's design.
#                                                                                                              ^ -> although in most cases, i would agree that performance > readability.

# --------------------------------------------------------
# ✅ Key Principles of Pythonic Code
# --------------------------------------------------------

# Let’s summarize the core principles that make code Pythonic:

# 1. **Readability Counts**: Write code that’s easy to understand. Aim for simplicity and clarity.
#    Example: Use descriptive variable names and avoid cryptic abbreviations. ( although the abbrevation part is meh ( <-- doesn't rlly matter ))
#    ```
#    # Non-Pythonic:
#    x = 10
#    y = 20
#    z = x + y
#    
#    # Pythonic:
#    total_price = 10
#    tax_rate = 0.2
#    total_with_tax = total_price + (total_price * tax_rate)
#    ```

# 2. **There Should Be One—And Preferably Only One—Obvious Way to Do It**:
#    Python embraces consistency and avoids having too many ways to accomplish the same task. This principle is captured in the <<Zen>> of Python.
#    Example: Instead of having multiple ways to loop over a list, Python encourages the use of `for` loops and the built-in `enumerate()`.

# 3. **Avoid Overcomplicating**:
#    Simple code is almost always better than complex, over-engineered solutions.
#    Example:
#    ```
#    # Non-Pythonic (too complex):
#    def complex_sum(a, b):
#        result = a
#        for i in range(1, b):
#            result += i
#        return result
#    
#    # Pythonic (simpler):
#    result = sum(range(a, b))
#    ```

# 4. **Make Use of Python's Built-In Functions and Libraries**:
#    Python’s standard library is vast, and there are often built-in tools that save time and make your code more concise and readable.
#    Example:
#    ```
#    # Non-Pythonic:
#    def find_max(numbers):
#        max_num = numbers[0]
#        for num in numbers:
#            if num > max_num:
#                max_num = num
#        return max_num
#    
#    # Pythonic:
#    max_num = max(numbers)
#    ```

# 5. **Don't Reinvent the Wheel**:
#    Python has a rich <<ecosystem>> of libraries and built-in features that should be leveraged for common tasks.
#     ^ -> Avoid manually implementing things that are already available in the standard library or through third-party modules. ( second point can vary )

# --------------------------------------------------------
# --> __ Conclusion __ 
# --------------------------------------------------------

# Writing Pythonic code isn't just about adhering to PEP8 or using the latest features. It's about:
# - Striking a balance between clarity, efficiency, and simplicity.
# - Leveraging Python's built-in tools and libraries to write concise, readable, and maintainable code.
# - Writing code that is easy to understand by others and yourself, even "years" down the line.

# Pythonic code doesn't just make things easier for developers today—it makes it easier for developers in the future,
#                 fostering "collaboration", maintainability, and scalability in codebases.

# Now that you have a foundational understanding of Pythonic code, we can go deeper into topics such as PEP8,
#         advanced idiomatic patterns, and more in subsequent files.
