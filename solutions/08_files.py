"""Solution 08 — Files.  https://pythonbeginner.help/learn/python-file-handling-basics-read-and-write/"""

import os

lines = ["Hello, world!", "Welcome to Python.", "Goodbye."]

path = "greeting.txt"

with open(path, "w") as f:
    for line in lines:
        f.write(line + "\n")

with open(path) as f:
    contents = f.read()

assert contents == "Hello, world!\nWelcome to Python.\nGoodbye.\n", \
    f"contents was {contents!r}"
print("✅ Passed!", "file contents:", repr(contents))

os.remove(path)
