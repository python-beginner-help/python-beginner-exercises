"""Solution 03 — Lists.  https://pythonbeginner.help/learn/"""

nums = [3, 1, 2]

nums.append(5)
first = nums[0]
last = nums[-1]
ordered = sorted(nums)

assert nums == [3, 1, 2, 5]
assert first == 3
assert last == 5
assert ordered == [1, 2, 3, 5]
print("✅ Passed!", nums, "first:", first, "last:", last, "ordered:", ordered)
