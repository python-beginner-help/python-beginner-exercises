"""Solution 05 — Functions.  https://pythonbeginner.help/learn/"""


def greet(name):
    return f"Hello, {name}!"


def is_even(n):
    return n % 2 == 0


assert greet("Ada") == "Hello, Ada!"
assert is_even(4) is True
assert is_even(7) is False
print("✅ Passed!", greet("Ada"), "| is_even(4):", is_even(4))
