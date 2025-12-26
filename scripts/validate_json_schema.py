#!/usr/bin/env python3
"""Validate agent outputs against schemas (offline).

Usage:
  python scripts/validate_json_schema.py schemas/spec.schema.json path/to/output.json

Requires:
  pip install jsonschema
"""

import json, sys
from jsonschema import Draft202012Validator

def main(schema_path, json_path):
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    v = Draft202012Validator(schema)
    errors = sorted(v.iter_errors(data), key=lambda e: e.path)
    if errors:
        print("INVALID:")
        for e in errors:
            path = ".".join([str(p) for p in e.path]) or "<root>"
            print(f"- {path}: {e.message}")
        sys.exit(1)
    print("OK")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2])
