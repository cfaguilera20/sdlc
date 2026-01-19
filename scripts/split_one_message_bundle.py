#!/usr/bin/env python3
"""Split a mode=one_message orchestrator JSON bundle into run-folder artifacts.

This script helps avoid data loss and standardize file outputs across developers.

Usage:
  # Split into an existing run folder
  python3 scripts/split_one_message_bundle.py path/to/bundle.json runs/PROJ-123_slug_20260115_120000

  # Create a new run folder and split
  python3 scripts/split_one_message_bundle.py path/to/bundle.json --ticket PROJ-123 --title "short title"

Notes:
  - It writes JSON files (pretty-printed).
  - It does NOT overwrite existing files unless you pass --overwrite.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


def slugify(s: str, max_len: int = 42) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s[:max_len] or "run"


def write_json(path: Path, data, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Refusing to overwrite: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def ensure_run_dir(repo_root: Path, args) -> Path:
    if args.run_dir:
        p = Path(args.run_dir).resolve()
        if not p.exists():
            raise FileNotFoundError(f"Run dir not found: {p}")
        return p

    if not args.ticket or not args.title:
        raise ValueError("Either provide run_dir, or provide --ticket and --title")

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    folder = f"{args.ticket}_{slugify(args.title)}_{ts}"
    out_dir = (repo_root / "runs" / folder).resolve()
    out_dir.mkdir(parents=True, exist_ok=False)
    return out_dir


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("bundle_json", help="Path to JSON bundle produced by mode=one_message orchestrator")
    ap.add_argument("run_dir", nargs="?", help="Existing run folder to write into (optional)")
    ap.add_argument("--ticket", help="Ticket id (used only if run_dir not provided)")
    ap.add_argument("--title", help="Short title for slug (used only if run_dir not provided)")
    ap.add_argument("--overwrite", action="store_true", help="Allow overwriting existing files")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    bundle_path = Path(args.bundle_json).resolve()
    bundle = json.loads(bundle_path.read_text(encoding="utf-8"))

    out_dir = ensure_run_dir(repo_root, args)

    # Known keys from orchestrator one_message contract
    mapping = {
        "ticket_context": "ticket_context.json",
        "backlog": "backlog.json",
        "spec": "spec.json",
        "test_suite": "test_suite.json",
        "integration_plan": "integration_plan.json",
        "data_migration_plan": "data_migration_plan.json",
        "modernization_plan": "modernization_plan.json",
    }

    written = []
    for key, filename in mapping.items():
        if key in bundle and bundle[key] is not None:
            write_json(out_dir / filename, bundle[key], overwrite=args.overwrite)
            written.append(filename)

    # Multiple-stories variant
    if "specs" in bundle and bundle["specs"] is not None:
        write_json(out_dir / "specs.json", bundle["specs"], overwrite=args.overwrite)
        written.append("specs.json")
    if "test_suites" in bundle and bundle["test_suites"] is not None:
        write_json(out_dir / "test_suites.json", bundle["test_suites"], overwrite=args.overwrite)
        written.append("test_suites.json")

    # Always persist notes for audit/debug (even if empty)
    if "notes" in bundle:
        write_json(out_dir / "notes.json", bundle.get("notes"), overwrite=args.overwrite)
        written.append("notes.json")

    print(str(out_dir))
    if written:
        print("WROTE:")
        for f in written:
            print(f"- {f}")
    else:
        print("No recognized keys found in bundle. Nothing written.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


