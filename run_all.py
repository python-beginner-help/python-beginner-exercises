#!/usr/bin/env python3
"""Run all exercises in exercises/ and report pass/fail.

Usage:
    python run_all.py            # run every exercise, stop on first failure
    python run_all.py --keep     # don't stop on first failure, report all

Exercises that contain `...` (a TODO placeholder) are skipped with a clear
message — that is how unfinished work shows up.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
import traceback
from pathlib import Path

EXERCISES_DIR = Path(__file__).parent / "exercises"


def iter_exercise_files() -> list[Path]:
    return sorted(p for p in EXERCISES_DIR.glob("*.py") if not p.name.startswith("_"))


def has_todo(path: Path) -> bool:
    return "..." in path.read_text(encoding="utf-8").split("# --- self-check")[0]


def run_one(path: Path) -> str:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        return "load-error"
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except AssertionError as exc:
        return f"FAIL: {exc}"
    except Exception:
        return "ERROR:\n" + "".join(traceback.format_exc())
    return "pass"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--keep", action="store_true",
                        help="don't stop on first failure; run every exercise")
    args = parser.parse_args()

    files = iter_exercise_files()
    if not files:
        print("No exercises found in", EXERCISES_DIR)
        return 1

    passed = skipped = failed = 0
    for path in files:
        print(f"== {path.name} ", end="")
        print("-" * max(1, 60 - len(path.name)))

        if has_todo(path):
            print("  SKIP (still has TODO placeholders)")
            skipped += 1
            continue

        result = run_one(path)
        if result == "pass":
            print("  PASS")
            passed += 1
        else:
            print("  " + result.replace("\n", "\n  "))
            failed += 1
            if not args.keep:
                return 1

    print()
    print(f"Summary: {passed} passed, {skipped} skipped, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
