"""Exercise 03 — Lists.

Tutorial: https://pythonbeginner.help/learn/

TODO: starting from `nums`:
  1. Append the number 5.
  2. Store the first item in `first` and the last in `last`.
  3. Store a NEW sorted list in `ordered` (don't change `nums`).

Run:  python exercises/03_lists.py
"""

nums = [3, 1, 2]

# --- your code below -------------------------------------------------------
# TODO: nums.append(5)
first = ...     # TODO: nums[0]
last = ...      # TODO: nums[-1]
ordered = ...   # TODO: sorted(nums)

# --- self-check (don't edit) ----------------------------------------------
assert nums == [3, 1, 2, 5], "did you append 5 to nums?"
assert first == 3, "first should be nums[0]"
assert last == 5, "last should be nums[-1]"
assert ordered == [1, 2, 3, 5], "ordered should be a sorted copy of nums"
print("✅ Passed!", nums, "first:", first, "last:", last, "ordered:", ordered)
