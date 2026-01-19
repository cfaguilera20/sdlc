#!/usr/bin/env python3
"""Validate a run folder's JSON artifacts against repo schemas.

Usage:
  python3 scripts/validate_run.py runs/PROJ-123_some-title_20260115_120000

What it validates (if present):
  - ticket_context.json  -> schemas/ticket_context.schema.json
  - backlog.json         -> schemas/backlog.schema.json
  - spec.json            -> schemas/spec.schema.json
  - spec_frontend.json   -> schemas/spec.schema.json
  - test_suite.json      -> schemas/test_suite.schema.json
  - pipeline_plan.json   -> schemas/pipeline_plan.schema.json

Requires:
  pip install jsonschema
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator


SCHEMA_MAP = {
    "pipeline_plan.json": "schemas/pipeline_plan.schema.json",
    "ticket_context.json": "schemas/ticket_context.schema.json",
    "backlog.json": "schemas/backlog.schema.json",
    "spec.json": "schemas/spec.schema.json",
    "spec_frontend.json": "schemas/spec.schema.json",
    "test_suite.json": "schemas/test_suite.schema.json",
}


def validate(schema_path: Path, json_path: Path) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = json.loads(json_path.read_text(encoding="utf-8"))
    v = Draft202012Validator(schema)
    errors = sorted(v.iter_errors(data), key=lambda e: list(e.path))
    out: list[str] = []
    for e in errors:
        p = ".".join([str(x) for x in e.path]) or "<root>"
        out.append(f"{p}: {e.message}")
    return out


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2

    run_dir = Path(sys.argv[1]).resolve()
    if not run_dir.exists() or not run_dir.is_dir():
        print(f"Run folder not found: {run_dir}")
        return 2

    repo_root = Path(__file__).resolve().parents[1]
    failures = 0
    checked = 0

    for filename, schema_rel in SCHEMA_MAP.items():
        p = run_dir / filename
        if not p.exists():
            continue
        schema_path = (repo_root / schema_rel).resolve()
        if not schema_path.exists():
            print(f"Missing schema: {schema_rel}")
            failures += 1
            continue

        checked += 1
        errs = validate(schema_path, p)
        if errs:
            failures += 1
            print(f"INVALID: {p.relative_to(repo_root) if repo_root in p.parents else p}")
            for msg in errs:
                print(f"- {msg}")
        else:
            print(f"OK: {p.name}")

    if checked == 0:
        print("No known artifacts found to validate in this run folder.")
        return 1

    if failures:
        print(f"\nFAILED: {failures} file(s) invalid.")
        return 1
    print("\nALL OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


