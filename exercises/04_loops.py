"""Exercise 04 — Loops.

Tutorial: https://pythonbeginner.help/learn/

TODO: using a loop,
  1. Build `squares` = [0, 1, 4, 9, 16] (squares of 0..4).
  2. Set `total` = the sum of the numbers 1..10 inclusive.

Run:  python exercises/04_loops.py
"""

# --- your code below -------------------------------------------------------
squares = []
# TODO: loop over range(5) and append i * i to squares

total = 0
# TODO: loop over range(1, 11) and add each number to total

# --- self-check (don't edit) ----------------------------------------------
assert squares == [0, 1, 4, 9, 16], "squares should be the squares of 0..4"
assert total == 55, "total should be 1+2+...+10"
print("✅ Passed!", "squares:", squares, "total:", total)
