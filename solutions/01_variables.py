"""Solution 01 — Variables & types.  https://pythonbeginner.help/learn/"""

name = "Ada"
age = 36
age_text = str(age)

assert isinstance(name, str) and name != ""
assert isinstance(age, int)
assert age_text == str(age)
print(f"✅ Passed! {name} is {age_text} years old.")
