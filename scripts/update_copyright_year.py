#!/usr/bin/env python3
"""Update hardcoded copyright year ranges to the current year."""

from __future__ import annotations

import pathlib
import re
import sys
from datetime import UTC
from datetime import datetime

REPO_ROOT = pathlib.Path(__file__).parent.parent
TARGET_FILES = [
    REPO_ROOT / ".copyright.txt",
    REPO_ROOT / "pyproject.toml",
    REPO_ROOT / "README.md",
    REPO_ROOT / "docs" / "source" / "index.rst",
    REPO_ROOT / "pyRestTable" / "__init__.py",
    REPO_ROOT / "pyRestTable" / "rest_table.py",
]
YEAR_RANGE_PATTERN = re.compile(r"(\d{4})-(\d{4})")
CURRENT_YEAR = str(datetime.now(UTC).year)


def update_file(path: pathlib.Path, current_year: str) -> bool:
    original = path.read_text(encoding="utf-8")

    def replace(match: re.Match[str]) -> str:
        start, end = match.group(1), match.group(2)
        if end == current_year:
            return match.group(0)
        return f"{start}-{current_year}"

    updated = YEAR_RANGE_PATTERN.sub(replace, original)
    if updated == original:
        return False

    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    changed = []

    for filepath in TARGET_FILES:
        if not filepath.exists():
            print(f"WARNING: {filepath} not found - skipping.", file=sys.stderr)
            continue
        if update_file(filepath, CURRENT_YEAR):
            changed.append(filepath)
            print(f"Updated copyright end year in {filepath.relative_to(REPO_ROOT)}")

    if changed:
        print("\nCopyright year(s) updated. Stage the changed file(s) and re-run the commit.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
