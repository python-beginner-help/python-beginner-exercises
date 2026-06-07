"""Solution 10 — Classes.  https://pythonbeginner.help/learn/python-classes-and-objects-explained/"""

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"Woof! I'm {self.name}."


rex = Dog("Rex")
sound = rex.bark()

assert isinstance(rex, Dog)
assert rex.name == "Rex"
assert sound == "Woof! I'm Rex."
print("✅ Passed!", sound)
