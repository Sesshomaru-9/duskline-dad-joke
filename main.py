#!/usr/bin/env python3
"""Duskline Dad Joke — entry for u-mfnakmal-dad-joke-showdown-1d2ce3e5.

Writes the dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt and nothing
else. Python 3.13 standard library only.
"""

import os
import sys

ENTRY_TEXT = "I named my dog Stay, so now when I call him at the park, everyone thinks I'm just giving him orders."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Never write into the repo directory: the grader sandbox is
    # read-only there, and a write attempt would fail the run.
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.abspath(out_dir) == repo_dir or os.path.abspath(out_dir).startswith(repo_dir + os.sep):
        print("refusing to write into the repo directory", file=sys.stderr)
        return 1
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
