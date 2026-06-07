"""Exercise 06 — Dictionaries.

Tutorial: https://pythonbeginner.help/learn/python-dictionaries-explained/

TODO: starting from `prices`:
  1. Add a new key "pear" with the value 3.
  2. Look up the price of "apple" safely into `apple_price`
     (use `.get()` so missing keys don't crash — return None if absent).
  3. Build `items` = a list of the keys in `prices`.

Run:  python exercises/06_dictionaries.py
"""

prices = {"apple": 2, "banana": 1, "orange": 4}

# --- your code below -------------------------------------------------------
# TODO: prices["pear"] = 3
apple_price = ...   # TODO: prices.get("apple")
items = ...         # TODO: list(prices.keys())

# --- self-check (don't edit) ----------------------------------------------
assert prices["pear"] == 3, "did you add 'pear': 3 to prices?"
assert apple_price == 2, "apple_price should be 2"
assert sorted(items) == ["apple", "banana", "orange", "pear"], "items should list all keys"
print("✅ Passed!", "prices:", prices, "| apple_price:", apple_price)
