<p align="center">
  <a href="https://pythonbeginner.help">
    <img src="https://pythonbeginner.help/brand/logo-horizontal.png" alt="Python Beginner Help" width="440">
  </a>
</p>

# Python Beginner Exercises 🏋️🐍

> Small, runnable practice exercises for new Python programmers — each with a built-in self-check and a worked solution.

These exercises mirror the learning track on **[pythonbeginner.help](https://pythonbeginner.help)**. Read a topic, then practice it here.

## How to use

1. Make sure you have [Python installed](https://pythonbeginner.help/learn/) (3.8+).
2. Open an exercise in the [`exercises/`](exercises) folder and complete the `TODO`.
3. Run it — each file checks your answer with `assert` and prints ✅ when it passes:

   ```bash
   python exercises/01_variables.py
   ```

4. Stuck? Compare with the matching file in [`solutions/`](solutions).

## Exercises

| # | Exercise | Topic | Tutorial |
|---|----------|-------|----------|
| 01 | [Variables & types](exercises/01_variables.py) | Variables, `int`/`str` | [Learn →](https://pythonbeginner.help/learn/) |
| 02 | [String methods](exercises/02_strings.py) | Strings, slicing | [Learn →](https://pythonbeginner.help/learn/) |
| 03 | [Lists](exercises/03_lists.py) | Lists, indexing | [Learn →](https://pythonbeginner.help/learn/) |
| 04 | [Loops](exercises/04_loops.py) | `for` / `range` | [Learn →](https://pythonbeginner.help/learn/) |
| 05 | [Functions](exercises/05_functions.py) | `def`, return values | [Learn →](https://pythonbeginner.help/learn/) |

## Run all exercises at once

```bash
for f in exercises/*.py; do echo "== $f =="; python "$f"; done
```

## More

- 📚 Tutorials: **[pythonbeginner.help](https://pythonbeginner.help)**
- 📋 [Python Cheatsheet](https://github.com/python-beginner-help/python-cheatsheet)
- 🔧 [Python Error Fixes](https://github.com/python-beginner-help/python-error-fixes) — when an exercise throws an error you don't recognise.

## License

Released under [CC0 1.0](LICENSE) by **pythonbeginner.help** — copy, remix, and teach with these freely.
