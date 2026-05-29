"""Exercise 01 — Variables & types.

Tutorial: https://pythonbeginner.help/learn/

TODO:
  1. Create a variable `name` holding your name as a string.
  2. Create a variable `age` holding an age as an integer.
  3. Create `age_text` that turns `age` into a string using str().

Run:  python exercises/01_variables.py
"""

# --- your code below -------------------------------------------------------
name = ...   # TODO: a string, e.g. "Ada"
age = ...    # TODO: an integer, e.g. 36
age_text = ...  # TODO: str(age)

# --- self-check (don't edit) ----------------------------------------------
assert isinstance(name, str) and name != "", "name should be a non-empty string"
assert isinstance(age, int), "age should be an integer"
assert age_text == str(age), "age_text should be str(age)"
print(f"✅ Passed! {name} is {age_text} years old.")
