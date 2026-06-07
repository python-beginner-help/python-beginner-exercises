"""Exercise 10 — Classes.

Tutorial: https://pythonbeginner.help/learn/python-classes-and-objects-explained/

TODO:
  1. Define a class `Dog` with:
       - __init__(self, name) that stores the name
       - bark(self) that returns "Woof! I'm <name>."
  2. Create a Dog named "Rex" in `rex`, and store its bark() in `sound`.

Run:  python exercises/10_classes.py
"""

# --- your code below -------------------------------------------------------
class Dog:
    def __init__(self, name):
        ...  # TODO: store the name on self

    def bark(self):
        ...  # TODO: return f"Woof! I'm {self.name}."


rex = ...        # TODO: Dog("Rex")
sound = ...      # TODO: rex.bark()

# --- self-check (don't edit) ----------------------------------------------
assert isinstance(rex, Dog), "rex should be a Dog"
assert rex.name == "Rex", "rex.name should be 'Rex'"
assert sound == "Woof! I'm Rex.", f"sound was {sound!r}"
print("✅ Passed!", sound)
