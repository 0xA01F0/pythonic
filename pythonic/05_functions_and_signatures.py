# --------------------------------------------------------
# 🧠 Writing Clean, Pythonic Functions
# --------------------------------------------------------

# A Pythonic function:
# - does *one* thing
# - has a descriptive name
# - uses clear, meaningful parameters
# - returns data clearly
# - avoids side effects (unless clearly intended)

# --------------------------------------------------------
# 🔧 Dummy definitions for demonstration
# --------------------------------------------------------
# We define these stubs so later examples run without errors.

def check():
    """Stub: pretend to check a condition."""
    return True

def ready():
    """Stub: pretend to check readiness."""
    return True

def valid():
    """Stub: pretend to validate something."""
    return True

# Example list for lambda example
names = ["Adrian", "aden", "romeo"]

# --------------------------------------------------------
# ✅ Good function naming
# --------------------------------------------------------

# Function names should state what they *do*.

# ❌ Bad:
def handle_data(x):
    # Unclear what the function actually does ( <-- if it's the only function that handles any data in general and it takes room temp iq to figure out what it is, i wouldn't say this is necessary. )
    pass

# ✅ Good:
def normalize_scores(scores):
    # Clearly normalizes scores
    pass

# ✅ Even better (naming the noun being returned):
def get_normalized_scores(scores):
    # Fetches normalized scores
    pass

# --------------------------------------------------------
# ✅ Default parameters and keyword arguments
# --------------------------------------------------------

# Avoid requiring users to remember argument order for boolean flags.

# ❌ "Hard to read":
def fetch_data(user, raw=False, retry=True):
    pass

# ❌ Confusing call:
fetch_data("adrian", True, False)

# ✅ Pythonic:
def fetch_data(user, *, raw=False, retry=True):
    pass

# ✅ Clear usage:
fetch_data("alice", raw=True, retry=False)

# The `*` forces keyword-only arguments.
# It improves readability when you have optional config-like params.

# --------------------------------------------------------
# ✅ Return values
# --------------------------------------------------------

# ❌ Anti-pattern:
def process():
    print("done")

result = process()  # Returns None (maybe we wanted data?)

# ✅ Pythonic: Functions should _return_, not print.
def process(data):
    processed_data = data * 2  # Just an example
    return processed_data

# Let the caller decide what to do with it.

# --------------------------------------------------------
# ⚙️ Don't return multiple types (unless you must)
# --------------------------------------------------------

# ❌ Confusing:
def parse(x):
    if x.startswith("http"):
        return x
    return False  # inconsistent return type

# ✅ More explicit:
def parse(x):
    if not x.startswith("http"):
        return None
    return x

# Or raise if it's an error, not just a missing case.

# --------------------------------------------------------
# 🪄 Use unpacking to return multiple values
# --------------------------------------------------------

def get_bounds(numbers):
    # Returns a tuple with min and max values
    return min(numbers), max(numbers)

low, high = get_bounds([1, 9, 2, 7])
print(low, high)

# ✅ Pythonic: unpacked tuple return values are idiomatic

# --------------------------------------------------------
# 🧼 Don’t overuse *args and **kwargs unless needed
# --------------------------------------------------------

# ❌ Problematic — too vague:
def log_event(*args, **kwargs):
    # It’s unclear what args and kwargs should contain
    pass

# ✅ Better: be specific unless you really need generic flexibility.

def log_event(event_name, timestamp, **extra_info):
    # This is better because we specify the main arguments
    pass

# --------------------------------------------------------
# ⚖️ Avoid too many params
# --------------------------------------------------------

# ❌ Messy:
def connect(host, port, user, password, timeout, retries, use_ssl):
    # Too many params for one function call
    pass

# ✅ Pythonic: bundle related config into a dict or dataclass ( not always needed)
def connect(config):
    pass

# Or, using a dataclass:
from dataclasses import dataclass

@dataclass
class DBConfig:
    host: str
    port: int
    user: str
    password: str
    timeout: int = 5
    retries: int = 3
    use_ssl: bool = True


def connect(cfg: DBConfig):
    pass

# This improves readability, default handling, and avoids long signatures

# --------------------------------------------------------
# 📎 Prefer simple composition over deep nesting
# --------------------------------------------------------

# ❌ Unreadable:
def load():
    if check():
        if ready():
            if valid():
                return True

# ✅ Better:
def load():
    if not check():
        return False
    if not ready():
        return False
    if not valid():
        return False
    return True
#                 ^ but i can definitely understand the argument of one saying that the first example is just cleaner / better looking ( i kind of agree )

# ✅ Even more concise:
def load():
    return all([check(), ready(), valid()])

# --------------------------------------------------------
# ⛓ When to use lambda vs def?
# --------------------------------------------------------

# ✅ Use `lambda` for *simple* inline functions:
sorted(names, key=lambda x: x.lower())

# ❌ But not for anything with logic:
# lambda x: (x * 2 if x < 10 else x / 2)  # 😵‍💫

# ✅ Use `def` for anything with control flow or multiple steps.

# --------------------------------------------------------
# 🧪 Recap: Pythonic function design
# --------------------------------------------------------

# - One purpose per function
# - Descriptive names and args
# - Use keyword-only args to improve clarity
# - Favor returning values over printing
# - Avoid multiple types in returns
# - Bundle config into dicts or dataclasses
# - Avoid deep nesting
# - Use lambda sparingly — only when it truly helps
