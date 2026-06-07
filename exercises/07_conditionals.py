"""Exercise 07 — Conditionals.

Tutorial: https://pythonbeginner.help/learn/python-if-else-and-elif-explained/

TODO: classify a number:
  1. Set `label` to "positive", "zero", or "negative" based on `n`.
  2. Set `parity` to "even" or "odd" using a ternary expression.

Run:  python exercises/07_conditionals.py
"""

n = -7

# --- your code below -------------------------------------------------------
if n > 0:
    label = ...   # TODO: "positive"
elif n < 0:
    label = ...   # TODO: "negative"
else:
    label = ...   # TODO: "zero"

parity = ...  # TODO: "even" if n % 2 == 0 else "odd"

# --- self-check (don't edit) ----------------------------------------------
assert label == "negative", "for n = -7, label should be 'negative'"
assert parity == "odd", "for n = -7, parity should be 'odd'"
print("✅ Passed!", "label:", label, "| parity:", parity)
