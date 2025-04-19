# --------------------------------------------------------
# 🧠 Understanding Type Hinting in Python
# --------------------------------------------------------

# Type hinting is an optional feature introduced in Python 3.5,
#      allowing developers to add metadata to function signatures,
#           improving code readability, and enabling static analysis tools.

# --------------------------------------------------------
# ✅ Basic Syntax of Type Hints
# --------------------------------------------------------

# Here's how we write basic type hints for function signatures:

def add(x: int, y: int) -> int:
    return x + y

# We are specifying that `x` and `y` should be integers,
# and the return value of `add()` is also an integer.

# --------------------------------------------------------
# ✅ Type Hinting with Collections (Lists, Dicts, etc.)
# --------------------------------------------------------

from typing import List, Dict

def process_names(names: List[str]) -> List[str]:
    # A function that processes a list of strings and returns a list of strings
    return [name.upper() for name in names]

# This is a common pattern when working with collections.
# Here, `List[str]` tells us the function expects a list of strings.

def get_user_info(user_id: int) -> Dict[str, str]:
    # The return type is a dictionary with keys and values as strings
    return {"user_id": str(user_id), "username": "blahblah123"}

# --------------------------------------------------------
# ✅ Type Hinting with Optional and Union
# --------------------------------------------------------

# Sometimes, a variable or return value can have multiple possible types.
# For that, we use `Union` or `Optional` (which is a shorthand for `Union[Type, None]`).

from typing import Union, Optional

def parse_value(val: str) -> Union[int, float, None]:
    # The return type can either be an int, a float, or None
    if val.isdigit():
        return int(val)
    elif val.replace('.', '', 1).isdigit():
        return float(val)
    return None

def get_optional_value(val: Optional[int]) -> int:
    # This means that `val` can be an integer or None.
    # If None, we return a default value of 0.
    return val if val is not None else 0

# --------------------------------------------------------
# ✅ Type Hinting for Functions that Return Multiple Values
# --------------------------------------------------------

# In Python, a function can return multiple values, often as a tuple.
# Type hints allow us to annotate this as well.

from typing import Tuple

def get_coordinates() -> Tuple[int, int]:
    # The function returns a tuple containing two integers
    return (10, 20)

x, y = get_coordinates()
print(x, y)

# --------------------------------------------------------
# ✅ Advanced: Callable (Function as a Type)
# --------------------------------------------------------

# You can even use type hints for functions that accept or return other functions.
# Here's an example of a function that takes another function as an argument.

from typing import Callable

def run_operation(op: Callable[[int, int], int], x: int, y: int) -> int:
    return op(x, y)

# `op` is a function that takes two integers and returns an integer.
# Let's test it with addition:

def add(x: int, y: int) -> int:
    return x + y

result = run_operation(add, 3, 4)
print(result)  # <- Output: 7

# --------------------------------------------------------
# ✅ Type Aliases: Making Complex Types Easier to Read
# --------------------------------------------------------

# For complex types, you can use type aliases to make things more readable.

from typing import List, Dict

# Example: Define a type alias for a dictionary of string to integer mappings
UserData = Dict[str, int]

def get_user_data() -> UserData:
    return {"age": 15, "height": 175}

# --------------------------------------------------------
# 🧑 Type Hinting in Practice
# --------------------------------------------------------

# While type hinting is optional in Python, it ( not always) greatly improves:
# - Code readability
# - Documentation (no need to dig through the code to figure out types)
# - IDE support and autocompletion
# - Static analysis (tools like mypy can check for type consistency)

# NOTE have in mind that sometimes type hinting is also just useless and unnecessary, but it's especially good when e.g. writing docs

# --------------------------------------------------------
# ✅ Key Takeaways:
# --------------------------------------------------------

# - Use type hints for clarity: functions, parameters, return values.
# - Use `List`, `Dict`, `Tuple`, `Union`, `Optional` for complex types.
# - Avoid overuse — type hints should enhance, not complicate.
# - Type hints are optional, but they add a lot of value when used properly.