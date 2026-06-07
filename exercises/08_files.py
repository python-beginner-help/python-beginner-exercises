"""Exercise 08 — Files.

Tutorial: https://pythonbeginner.help/learn/python-file-handling-basics-read-and-write/

TODO:
  1. Write the lines in `lines` to a temp file called `greeting.txt`.
  2. Read the same file back into `contents` (as a single string).

The file should live in the current working directory and is cleaned up
automatically after the self-check runs.

Run:  python exercises/08_files.py
"""

import os

lines = ["Hello, world!", "Welcome to Python.", "Goodbye."]

# --- your code below -------------------------------------------------------
path = "greeting.txt"

# TODO: open(path, "w") and write each line in `lines` (remember "\n")

contents = ...  # TODO: open(path) and read the whole file

# --- self-check (don't edit) ----------------------------------------------
assert contents == "Hello, world!\nWelcome to Python.\nGoodbye.\n", \
    f"contents was {contents!r}"
print("✅ Passed!", "file contents:", repr(contents))

os.remove(path)
