"""Exercise 05 — Functions.

Tutorial: https://pythonbeginner.help/learn/

TODO:
  1. Write `greet(name)` that returns "Hello, <name>!".
  2. Write `is_even(n)` that returns True if n is even, else False.

Run:  python exercises/05_functions.py
"""

# --- your code below -------------------------------------------------------
def greet(name):
    ...  # TODO: return f"Hello, {name}!"


def is_even(n):
    ...  # TODO: return n % 2 == 0


# --- self-check (don't edit) ----------------------------------------------
assert greet("Ada") == "Hello, Ada!", "greet should return 'Hello, Ada!'"
assert is_even(4) is True, "is_even(4) should be True"
assert is_even(7) is False, "is_even(7) should be False"
print("✅ Passed!", greet("Ada"), "| is_even(4):", is_even(4))
