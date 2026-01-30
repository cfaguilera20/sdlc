#!/usr/bin/env python3
"""Lightweight features.json helper for multi-session velocity.

This is inspired by simple "feature list" workflows (like masta-g3/rules):
  - keep a single features file
  - statuses: pending -> in_progress -> done (or blocked/cancelled)
  - deps via depends_on

Usage:
  # Create a new features.json
  python3 scripts/features.py init --project-id PROJ-123 --title "SSO email mismatch" --out features.json

  # Import backlog stories as features
  python3 scripts/features.py import-backlog runs/.../backlog.json --features features.json --run-dir runs/... --overwrite-spec-file

  # Show next ready feature (by priority, then id)
  python3 scripts/features.py next --features features.json

  # Mark status
  python3 scripts/features.py set-status --features features.json --id PROJ-123-1 --status in_progress

  # List
  python3 scripts/features.py list --features features.json
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


STATUSES = {"pending", "in_progress", "done", "blocked", "cancelled"}


def now_iso() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_features(path: Path) -> Dict[str, Any]:
    data = read_json(path)
    if not isinstance(data, dict) or "features" not in data:
        raise ValueError("Invalid features file (expected object with 'features')")
    return data


def is_ready(feature: Dict[str, Any], by_id: Dict[str, Dict[str, Any]]) -> bool:
    if feature.get("status") != "pending":
        return False
    deps = feature.get("depends_on") or []
    for dep in deps:
        d = by_id.get(dep)
        if not d:
            return False
        if d.get("status") != "done":
            return False
    return True


def cmd_init(args) -> int:
    out = Path(args.out).resolve()
    if out.exists() and not args.force:
        raise FileExistsError(f"Refusing to overwrite: {out} (pass --force)")

    data = {
        "version": "1.0",
        "project": {
            "id": args.project_id,
            "title": args.title,
            "created_at": now_iso(),
            "run_dir": args.run_dir,
        },
        "features": [],
    }
    write_json(out, data)
    print(str(out))
    return 0


def cmd_import_backlog(args) -> int:
    backlog_path = Path(args.backlog_json).resolve()
    features_path = Path(args.features).resolve()
    data = load_features(features_path)

    backlog = read_json(backlog_path)
    stories = backlog.get("stories") if isinstance(backlog, dict) else None
    if not isinstance(stories, list):
        raise ValueError("Backlog JSON missing stories[]")

    existing = {f["id"] for f in data.get("features", [])}
    run_dir = args.run_dir
    now = now_iso()

    added = 0
    for idx, st in enumerate(stories):
        if not isinstance(st, dict):
            continue
        fid = st.get("story_id") or f"story-{idx+1}"
        fid = str(fid)
        if fid in existing and not args.force_add_duplicates:
            continue

        desc = st.get("title") or st.get("user_story") or "(no title)"
        pri = st.get("priority")
        try:
            pri = int(pri) if pri is not None else 0
        except Exception:
            pri = 0

        feature = {
            "id": fid,
            "description": str(desc),
            "status": "pending",
            "priority": pri,
            "depends_on": [str(x) for x in (st.get("dependencies") or [])],
            "discovered_from": None,
            "spec_file": None,
            "owner": None,
            "created_at": now,
            "updated_at": None,
        }

        if run_dir:
            # Default per-story spec file path for traceability (optional)
            feature["spec_file"] = f"{run_dir}/spec.json"

        if fid in existing and args.force_add_duplicates:
            # Make it unique if duplicates are allowed
            suffix = 2
            new_id = f"{fid}-{suffix}"
            while new_id in existing:
                suffix += 1
                new_id = f"{fid}-{suffix}"
            feature["id"] = new_id
            fid = new_id

        existing.add(fid)
        data["features"].append(feature)
        added += 1

    # stable sort: priority desc, then id
    data["features"] = sorted(
        data["features"],
        key=lambda f: (-int(f.get("priority") or 0), str(f.get("id") or "")),
    )
    write_json(features_path, data)
    print(f"Imported {added} feature(s) into {features_path}")
    return 0


def cmd_next(args) -> int:
    features_path = Path(args.features).resolve()
    data = load_features(features_path)
    feats = data.get("features") or []
    by_id = {f.get("id"): f for f in feats if isinstance(f, dict) and f.get("id")}

    ready = [f for f in feats if isinstance(f, dict) and is_ready(f, by_id)]
    ready = sorted(ready, key=lambda f: (-int(f.get("priority") or 0), str(f.get("id") or "")))

    if not ready:
        print("No ready features.")
        return 1

    f = ready[0]
    print(json.dumps({"id": f.get("id"), "description": f.get("description"), "priority": f.get("priority")}, indent=2))

    if args.claim:
        for ff in feats:
            if ff.get("id") == f.get("id"):
                ff["status"] = "in_progress"
                ff["updated_at"] = now_iso()
        write_json(features_path, data)
        print(f"\nCLAIMED: {f.get('id')} -> in_progress")

    return 0


def cmd_set_status(args) -> int:
    if args.status not in STATUSES:
        raise ValueError(f"Invalid status: {args.status}")
    features_path = Path(args.features).resolve()
    data = load_features(features_path)
    feats = data.get("features") or []

    found = False
    for f in feats:
        if isinstance(f, dict) and f.get("id") == args.id:
            f["status"] = args.status
            f["updated_at"] = now_iso()
            found = True
            break

    if not found:
        raise ValueError(f"Feature not found: {args.id}")

    write_json(features_path, data)
    print(f"OK: {args.id} -> {args.status}")
    return 0


def cmd_list(args) -> int:
    features_path = Path(args.features).resolve()
    data = load_features(features_path)
    feats = data.get("features") or []

    # simple table-ish output
    for f in feats:
        if not isinstance(f, dict):
            continue
        print(f"{str(f.get('id')).ljust(18)} {str(f.get('status')).ljust(12)} p={str(f.get('priority')).ljust(3)} {f.get('description')}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init")
    p_init.add_argument("--project-id", required=True)
    p_init.add_argument("--title", required=True)
    p_init.add_argument("--out", default="features.json")
    p_init.add_argument("--run-dir", default=None, help="Optional default runs/<...>/ folder")
    p_init.add_argument("--force", action="store_true")
    p_init.set_defaults(func=cmd_init)

    p_imp = sub.add_parser("import-backlog")
    p_imp.add_argument("backlog_json")
    p_imp.add_argument("--features", required=True)
    p_imp.add_argument("--run-dir", default=None, help="Optional runs/<...>/ folder to set spec_file pointers")
    p_imp.add_argument("--force-add-duplicates", action="store_true")
    p_imp.set_defaults(func=cmd_import_backlog)

    p_next = sub.add_parser("next")
    p_next.add_argument("--features", required=True)
    p_next.add_argument("--claim", action="store_true", help="Mark returned feature as in_progress")
    p_next.set_defaults(func=cmd_next)

    p_set = sub.add_parser("set-status")
    p_set.add_argument("--features", required=True)
    p_set.add_argument("--id", required=True)
    p_set.add_argument("--status", required=True)
    p_set.set_defaults(func=cmd_set_status)

    p_list = sub.add_parser("list")
    p_list.add_argument("--features", required=True)
    p_list.set_defaults(func=cmd_list)

    args = ap.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())


