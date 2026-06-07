"""Solution 09 — Errors & try/except.  https://pythonbeginner.help/learn/using-try-except-else-and-finally-in-python/"""

def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None


results = [safe_int("42"), safe_int("hi"), safe_int(" 7 ")]

assert safe_int("42") == 42
assert safe_int("hi") is None
assert safe_int(" 7 ") == 7
assert results == [42, None, 7]
print("✅ Passed!", "results:", results)
