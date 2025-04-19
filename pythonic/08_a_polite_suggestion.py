# -----------------------------------------------
# NOTE:
# This doesn’t necessarily have anything to do with writing "Pythonic" code.
# I just felt like talking about it — private funcs ('_')
# Still, it’s useful to understand if you’re writing clean, maintainable Python.
# -----------------------------------------------

# -----------------------------------------------
# PRIVATE FUNCTIONS IN PYTHON
# -----------------------------------------------
# In Python, functions (and variables) prefixed with a single underscore _
#        are considered "private" by convention — meaning they are intended
#            for internal use within a module or class.
# 
# Important: This is just a naming convention. Python does NOT enforce access restrictions.
# Any code can still access a _function from outside its module or class.
# This is part of the "we're all consenting adults here" philosophy of Python.
# -----------------------------------------------

# This function is meant for internal use.
# We prefix it with an underscore to signal: "don't call this from outside unless you know what you're doing."
def _hello(name):
    # Even though it's "private", this is a normal function under the hood.
    # The underscore just tells other devs: "Hey, this is internal."
    return f"Hello, {name}!"

# A public function that wraps around the internal _hello function.
# This is what we *want* external users to call.
def greet(name):
    # By wrapping _hello() in greet(), we can:
    # - sanitize input
    # - add logging
    # - change the implementation of _hello() later without affecting users
    # - test _hello() in isolation, but only expose greet() to the world
    print(_hello(name))

# -----------------------------------------------
# WHY USE PRIVATE FUNCTIONS?
# -----------------------------------------------
# 1. Encapsulation — hide complexity behind simple interfaces.
# 2. Maintainability — if users only call greet(), you can refactor _hello() freely.
# 3. API clarity — external users see only what they need to use.
# 4. Testing — you can still test private functions directly if needed.
# 5. Collaboration — make intent clear to teammates (e.g., "this isn't part of the contract").

# -----------------------------------------------
# WHAT HAPPENS IF YOU IMPORT THIS FILE?
# -----------------------------------------------
# If another file does:
#     from private_functions import *
# The _hello function will NOT be imported. 
# This is because of how Python treats the wildcard import. <-- the wildcard import is just the "*" import, meaning it allows you to get all the public names from a module
# Only names without a leading underscore are pulled in.
#
# But direct access still works:
#     from private_functions import _hello  # This still works manually.
#     _hello("you")                         # Will print just fine.
# -----------------------------------------------

# This is a standard pattern for testing modules directly.
# Only runs when this file is run as a script.
if __name__ == "__main__":
    greet("Adrian")

# -----------------------------------------------
# TL;DR:
# - Leading underscores are a convention, not a rule.
# - Use _ to hide functions/variables that aren't part of your public API.
# - Trust is given to the developer. It's up to you to respect boundaries 😖
# -----------------------------------------------
