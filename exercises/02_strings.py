"""Exercise 02 — String methods & slicing.

Tutorial: https://pythonbeginner.help/learn/

TODO: given `phrase`, produce:
  1. `shout`  -> the phrase in UPPERCASE
  2. `first5` -> the first 5 characters
  3. `words`  -> a list of the words

Run:  python exercises/02_strings.py
"""

phrase = "python is fun"

# --- your code below -------------------------------------------------------
shout = ...    # TODO: phrase.upper()
first5 = ...   # TODO: phrase[0:5]
words = ...    # TODO: phrase.split()

# --- self-check (don't edit) ----------------------------------------------
assert shout == "PYTHON IS FUN", "shout should be the phrase uppercased"
assert first5 == "pytho", "first5 should be the first 5 characters"
assert words == ["python", "is", "fun"], "words should be the split words"
print("✅ Passed!", shout, "|", first5, "|", words)
