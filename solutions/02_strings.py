"""Solution 02 — String methods & slicing.  https://pythonbeginner.help/learn/"""

phrase = "python is fun"

shout = phrase.upper()
first5 = phrase[0:5]
words = phrase.split()

assert shout == "PYTHON IS FUN"
assert first5 == "pytho"
assert words == ["python", "is", "fun"]
print("✅ Passed!", shout, "|", first5, "|", words)
