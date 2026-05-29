"""Solution 04 — Loops.  https://pythonbeginner.help/learn/"""

squares = []
for i in range(5):
    squares.append(i * i)

total = 0
for n in range(1, 11):
    total += n

assert squares == [0, 1, 4, 9, 16]
assert total == 55
print("✅ Passed!", "squares:", squares, "total:", total)
