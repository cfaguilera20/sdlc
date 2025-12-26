#!/usr/bin/env python3
"""Create a unique run folder for a ticket and drop placeholders.

Usage:
  python scripts/new_run.py --ticket PROJ-123 --title "SSO email mismatch"

Creates:
  runs/PROJ-123_sso-email-mismatch_<timestamp>/
    ticket.txt
    pipeline_plan.json
    ticket_context.json
    spec.json
    test_suite.json
"""
import argparse, re, json
from datetime import datetime
from pathlib import Path

def slugify(s: str, max_len: int = 42) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s[:max_len] or "run"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticket", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out-dir", default="runs")
    args = ap.parse_args()

    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    folder = f"{args.ticket}_{slugify(args.title)}_{ts}"
    out_dir = Path(args.out_dir) / folder
    out_dir.mkdir(parents=True, exist_ok=False)

    (out_dir / "ticket.txt").write_text("PASTE TICKET HERE\n", encoding="utf-8")
    (out_dir / "pipeline_plan.json").write_text("{\n  \"stack\": \"<rails|laravel>\",\n  \"commit_type\": \"<feat|fix|...>\",\n  \"phases\": []\n}\n", encoding="utf-8")
    (out_dir / "ticket_context.json").write_text("{\n}\n", encoding="utf-8")
    (out_dir / "spec.json").write_text("{\n}\n", encoding="utf-8")
    (out_dir / "test_suite.json").write_text("{\n}\n", encoding="utf-8")

    print(str(out_dir))

if __name__ == "__main__":
    main()
