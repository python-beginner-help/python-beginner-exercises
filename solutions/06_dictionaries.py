"""Solution 06 — Dictionaries.  https://pythonbeginner.help/learn/python-dictionaries-explained/"""

prices = {"apple": 2, "banana": 1, "orange": 4}

prices["pear"] = 3
apple_price = prices.get("apple")
items = list(prices.keys())

assert prices["pear"] == 3
assert apple_price == 2
assert sorted(items) == ["apple", "banana", "orange", "pear"]
print("✅ Passed!", "prices:", prices, "| apple_price:", apple_price)
