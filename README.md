<p align="center">
  <a href="https://pythonbeginner.help">
    <img src="https://pythonbeginner.help/brand/logo-horizontal.png" alt="Python Beginner Help" width="440">
  </a>
</p>

# Python Beginner Exercises 🏋️🐍

> Small, runnable practice exercises for new Python programmers — each with a built-in self-check and a worked solution.

These exercises mirror the learning track on **[pythonbeginner.help](https://pythonbeginner.help)**. Read a topic, then practice it here.

## How to use

1. Make sure you have [Python installed](https://pythonbeginner.help/learn/how-to-install-python-on-windows-macos-and-linux/) (3.8+).
2. Open an exercise in the [`exercises/`](exercises) folder and complete the `TODO`s.
3. Run it — each file checks your answer with `assert` and prints ✅ when it passes:

   ```bash
   python exercises/01_variables.py
   ```

4. Stuck? Compare with the matching file in [`solutions/`](solutions).
5. Run every exercise at once with the bundled runner:

   ```bash
   python run_all.py            # stop on first failure
   python run_all.py --keep     # run them all, report each result
   ```

The runner also reports any unfinished exercise (one that still contains `...` TODO placeholders) as `SKIP` so you can see at a glance what's left to do.

## Exercises

| #  | Exercise                          | Topic                                | Tutorial                                                                                                        |
|----|-----------------------------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| 01 | [Variables & types](exercises/01_variables.py)               | Variables, `int` / `str`             | [Learn →](https://pythonbeginner.help/learn/python-variables-explained-for-beginners/)                          |
| 02 | [String methods](exercises/02_strings.py)                    | Strings, slicing                     | [Learn →](https://pythonbeginner.help/learn/python-strings-explained-basics-and-examples/)                     |
| 03 | [Lists](exercises/03_lists.py)                                | Lists, indexing, `sorted()`          | [Learn →](https://pythonbeginner.help/learn/python-lists-explained-beginner-guide/)                             |
| 04 | [Loops](exercises/04_loops.py)                                | `for` and `range`                    | [Learn →](https://pythonbeginner.help/learn/python-for-loops-explained/)                                        |
| 05 | [Functions](exercises/05_functions.py)                        | `def`, return values                 | [Learn →](https://pythonbeginner.help/learn/python-functions-explained/)                                       |
| 06 | [Dictionaries](exercises/06_dictionaries.py)                  | `dict`, `.get()`, keys               | [Learn →](https://pythonbeginner.help/learn/python-dictionaries-explained/)                                    |
| 07 | [Conditionals](exercises/07_conditionals.py)                  | `if` / `elif` / `else`, ternary      | [Learn →](https://pythonbeginner.help/learn/python-if-else-and-elif-explained/)                                |
| 08 | [Files](exercises/08_files.py)                                | `open`, `read`, `write`              | [Learn →](https://pythonbeginner.help/learn/python-file-handling-basics-read-and-write/)                        |
| 09 | [Errors & try/except](exercises/09_errors.py)                 | `try`, `except ValueError`           | [Learn →](https://pythonbeginner.help/learn/using-try-except-else-and-finally-in-python/)                       |
| 10 | [Classes](exercises/10_classes.py)                            | `class`, `__init__`, methods         | [Learn →](https://pythonbeginner.help/learn/python-classes-and-objects-explained/)                             |

## CI

Every push and pull request runs all of the `solutions/*.py` files through GitHub Actions on Python 3.11, so the answers are always verified to work. See [`.github/workflows/exercises.yml`](.github/workflows/exercises.yml).

## Run all exercises at once

```bash
for f in exercises/*.py; do echo "== $f =="; python "$f"; done
```

…or just use the runner above.

## Companion repos

- 📚 Tutorials: **[pythonbeginner.help](https://pythonbeginner.help)**
- 📋 [Python Cheatsheet](https://github.com/python-beginner-help/python-cheatsheet)
- 🔧 [Python Error Fixes](https://github.com/python-beginner-help/python-error-fixes) — when an exercise throws an error you don't recognise.
- ⭐ [Awesome Python for Beginners](https://github.com/python-beginner-help/awesome-python-for-beginners) — the curated resource list.

## License

Released under [CC0 1.0](LICENSE) by **pythonbeginner.help** — copy, remix, and teach with these freely.
