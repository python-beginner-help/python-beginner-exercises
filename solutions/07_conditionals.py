"""Solution 07 — Conditionals.  https://pythonbeginner.help/learn/python-if-else-and-elif-explained/"""

n = -7

if n > 0:
    label = "positive"
elif n < 0:
    label = "negative"
else:
    label = "zero"

parity = "even" if n % 2 == 0 else "odd"

assert label == "negative"
assert parity == "odd"
print("✅ Passed!", "label:", label, "| parity:", parity)
