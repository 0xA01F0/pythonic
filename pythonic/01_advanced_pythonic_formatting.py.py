# --------------------------------------------------------
# ⚡ Advanced Pythonic Formatting & Edge-Case Idioms
# --------------------------------------------------------

# Here we cover nuanced cases where you might intentionally bend or break
#       standard style rules for improved readability or expressiveness.

# --------------------------------------------------------
# 👨‍💻 PEP8 ≠ Pythonic (Reminder Only) <-- this statement means that just because code is pep8, you can't always automatically assume that it's pythoni
#                                              ^ -> this refers to the comment argument that says: "if code is not pep8, it's not pythonic"
# --------------------------------------------------------
# PEP8 is about style consistency; Pythonic code is about readability and intent.#
#                                 ^ although in a lot of cases, they strive for the same goal

# --------------------------------------------------------
# 🔧 Multiline Function Signatures
# --------------------------------------------------------
def do_thing(
    user,
    options,
    debug,
):
    """Non-PEP8 style but clear vertical alignment."""
    pass

def do_other_thing(
        user, options, debug):  # PEP8 hanging indent style
    """PEP8 hanging indent."""
    pass

# --------------------------------------------------------
# 📌 Method Chaining & Hanging Dots
# --------------------------------------------------------
class MockQuery:
    def filter_by(self, **kwargs):
        return self
    def limit(self, n):
        return self
    def all(self):
        return ["result"]

class MockDB:
    def query(self):
        return MockQuery()

db = MockDB()

# Standard style:
results = db.query().filter_by(active=True).limit(5).all()

# Hanging-dot style:
results = (
    db.query()
      .filter_by(active=True)
      .limit(5)
      .all()
)

# --------------------------------------------------------
# 🎨 Dict Key Alignment (Readability Over Rule)
# --------------------------------------------------------
user = {
    "id"      : 123,
    "name"    : "Adrian",
    "is_admin": True,
}

# --------------------------------------------------------
# 🔄 Vertical Collections
# --------------------------------------------------------
numbers = [
    1,
    2,
    3,
    4,
    5,
]

# --------------------------------------------------------
# 🔗 Chaining Context Managers
# --------------------------------------------------------
with open("a.txt") as fa, \
     open("b.txt") as fb:
    data = fa.read() + fb.read()

# --------------------------------------------------------
# 🧠 Zen of Python Reminder
# --------------------------------------------------------
# import this  # Beautiful is better than ugly. Readability counts.

# --------------------------------------------------------
# 🚀 Summary
# --------------------------------------------------------
# - Use these advanced formatting tricks judiciously. <-- use it well-judging
# - Always prioritize clarity for others
# - Break rules when it makes code more readable.
