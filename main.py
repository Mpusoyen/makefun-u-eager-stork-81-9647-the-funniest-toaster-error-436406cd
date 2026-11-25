"""The Funniest Toaster Error Message — make.fun mini entry.

Writes one original toaster error line to entry.txt.
Reads the output directory from MAKEFUN_OUTPUT_DIR, defaulting to /output.
Python stdlib only.
"""

import os

LINE = "ERR 12: Slot 2 held hostage by one blueberry from Tuesday's bagel. Toast cancelled. Negotiations have failed."


def main() -> None:
    assert 1 <= len(LINE) <= 120 and LINE.strip(), "line out of gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
