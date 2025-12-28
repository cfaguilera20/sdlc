#!/usr/bin/env python3
"""Apply 01X Domain Agent Scout materialize payload to the repo.

Usage:
  python3 scripts/apply_materialize.py path/to/suggested_domain_agents.json

The input file is the JSON output from Agent 01X and must contain:
  materialize.files[] = [{path,type,content,reason}, ...]

It will create/overwrite files relative to repo root.
"""

from __future__ import annotations
import json
import os
import sys
from pathlib import Path

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/apply_materialize.py <suggested_domain_agents.json>")
        return 2

    in_path = Path(sys.argv[1])
    data = json.loads(in_path.read_text(encoding="utf-8"))

    files = (data.get("materialize") or {}).get("files") or []
    if not files:
        print("No materialize.files[] found. Nothing to do.")
        return 1

    root = Path(".").resolve()
    written = 0

    for f in files:
        rel = f.get("path")
        content = f.get("content", "")
        if not rel:
            continue

        out_path = root / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
        written += 1
        print(f"WROTE: {rel}")

    print(f"Done. Wrote {written} file(s).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
