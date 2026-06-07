"""Exercise 09 — Errors & try/except.

Tutorial: https://pythonbeginner.help/learn/using-try-except-else-and-finally-in-python/

TODO:
  1. Write `safe_int(text)` that returns `int(text)` if possible,
     otherwise returns `None` — without raising an exception.
  2. Test it on a few values and store the results in `results`
     (a list with three entries: safe_int("42"), safe_int("hi"), safe_int(" 7 ")).

Run:  python exercises/09_errors.py
"""

# --- your code below -------------------------------------------------------
def safe_int(text):
    ...  # TODO: try int(text); return None on ValueError


results = [safe_int("42"), safe_int("hi"), safe_int(" 7 ")]

# --- self-check (don't edit) ----------------------------------------------
assert safe_int("42") == 42, "safe_int('42') should return 42"
assert safe_int("hi") is None, "safe_int('hi') should return None"
assert safe_int(" 7 ") == 7, "safe_int(' 7 ') should return 7"
assert results == [42, None, 7], "results list is wrong"
print("✅ Passed!", "results:", results)
