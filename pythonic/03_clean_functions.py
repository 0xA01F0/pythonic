# --------------------------------------------------------
# 🧼 Writing Clean, Pythonic Functions
# --------------------------------------------------------

# Functions are the building blocks of any non-trivial Python program.
# Clean functions are short, expressive, and flexible.

# --------------------------------------------------------
# ✅ Keep it short and specific
# --------------------------------------------------------

# A function should do one thing and do it well.

# ✅ Good example: computes square of a number
def square(n):
    return n * n

# ❌ Overloaded function with side effects, formatting, printing, and math
def process_and_print_and_log_and_square(n):
    print(f"processing -> {n}")
    log(n)
    return n * n

def log(msg):
    # Imagine this logs somewhere
    pass

# Keep responsibilities separate.

# --------------------------------------------------------
# ✅ Use clear, expressive names
# --------------------------------------------------------

# ❌ Ambiguous:
def p(x):
    return x + 1

# ✅ Clear:
def increment(number):
    return number + 1

# Clear names = self-documenting code.
#                                                    (( ^^   --> although sometimes short func names can be good, it can sometimes lead to "confusion" i guess. ( can also be very clean tho )

# --------------------------------------------------------
# ✅ Use default arguments wisely
# --------------------------------------------------------

def greet(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

print(greet("Adrian"))          # Hello, Adrian!
print(greet("Aden", "..."))     # Hello, Adem...

# Use default values for optional behaviors.

# ⚠️ Be careful: mutable defaults are dangerous

# ❌
def add_item(item, target=[]):
    target.append(item)
    return target

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b'] 😱

# ✅
def add_item_safe(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

# Use None as default sentinel for mutable types.

# --------------------------------------------------------
# ✅ Use *args and **kwargs for flexibility
# --------------------------------------------------------

def log_event(event, *args, **kwargs):
    print(f"Event -> {event}")
    print("Args ->", args)
    print("Keyword Args ->", kwargs)

log_event("LOGIN", "blahblah123", ip="127.0.0.1", success=True)

# Use these when you want to accept variable numbers of arguments.

# --------------------------------------------------------
# ✅ Use early returns instead of nesting
# --------------------------------------------------------

# ❌ Deep nesting:
def is_valid_email(email):
    if email:
        if "@" in email:
            return True
    return False

# ✅ Early return:
def is_valid_email_clean(email):
    if not email:
        return False
    if "@" not in email:
        return False
    return True

# Flat is better than nested (Zen of Python).

# --------------------------------------------------------
# Summary
# --------------------------------------------------------

# ✅ Keep functions short and focused
# ✅ Use clear names
# ✅ Handle defaults safely
# ✅ Return early to reduce nesting
# ✅ Use *args/**kwargs when needed — but not always
# ✅ Embrace clarity over cleverness
