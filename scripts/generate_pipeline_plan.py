#!/usr/bin/env python3
"""Generate a PipelinePlan JSON based on conventional commit type + stack.

You can print to stdout OR write to a unique run folder under /runs.

Examples:
  # Print to stdout
  python scripts/generate_pipeline_plan.py --stack rails --type feat

  # Write to a unique run folder (recommended)
  python scripts/generate_pipeline_plan.py --stack laravel --type fix --ticket PROJ-123 --title "SSO email mismatch"

  # Override defaults
  python scripts/generate_pipeline_plan.py --stack rails --type perf --perf --release --ticket PERF-9 --title "Optimize search endpoint"

Outputs when using --ticket:
  runs/<ticket>_<slug>_<YYYYMMDD_HHMMSS>/pipeline_plan.json
"""

import argparse, json, re
from datetime import datetime
from pathlib import Path

def slugify(s: str, max_len: int = 42) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s[:max_len] or "run"

def build_plan(commit_type, stack, impl, release, security, perf, backlog, include_fe=False):
    # Map agent per stack
    spec_agent = "03_technical_architect_generic"
    if stack == "rails":
        spec_agent = "03a_architect_rails"
    elif stack == "laravel":
        spec_agent = "03b_architect_laravel"

    phases = [
        {"name":"Context","agents":[{"id":"01_ticket_reader","input":"<paste Jira/Linear ticket text here>","expects":"TicketContext"}]}
    ]
    if backlog:
        phases.append({"name":"Backlog (optional split)","agents":[{"id":"02_product_analyst","input":"<TicketContext JSON>","expects":"Backlog"}]})
        story_input = "<One story JSON from Backlog.stories + TicketContext JSON>"
    else:
        story_input = "<TicketContext JSON + (optional) single story summary>"

    phases.append({"name":"Spec (Backend)","agents":[{"id":spec_agent,"input":story_input,"expects":"DeveloperReadySpec"}]})

    if include_fe:
        phases.append({"name":"Spec (Frontend)","agents":[{"id":"03c_architect_frontend","input":"<Story + TicketContext + (optional) BE Spec JSON>","expects":"DeveloperReadySpec"}]})

    if security:
        phases.append({"name":"Security & Privacy","agents":[{"id":"05_security_privacy","input":"<Spec JSON>","expects":"DeveloperReadySpec"}]})
    if perf:
        phases.append({"name":"Performance & Observability","agents":[{"id":"06_perf_observability","input":"<Spec JSON>","expects":"DeveloperReadySpec"}]})

    phases.append({"name":"QA","agents":[{"id":"04_qa_designer","input":"<Final Spec JSON>","expects":"TestSuite"}]})

    if impl:
        impl_agent = "07a_implementer_rails" if stack=="rails" else ("07b_implementer_laravel" if stack=="laravel" else "07a_implementer_rails")
        phases.append({"name":"Implement (Backend)","agents":[{"id":impl_agent,"input":"<Final Spec JSON + relevant repo snippets>","expects":"DeveloperReadySpec"}]})
        if include_fe:
            phases.append({"name":"Implement (Frontend)","agents":[{"id":"07c_implementer_frontend","input":"<Final FE Spec JSON + relevant FE snippets>","expects":"DeveloperReadySpec"}]})
        phases.append({"name":"Review","agents":[{"id":"08_code_reviewer","input":"<Final Spec JSON + diff/changed files + test output>","expects":"TestSuite"}]})

    if release:
        phases.append({"name":"Release/Ops","agents":[{"id":"09_release_ops","input":"<Final Spec JSON + env/deploy notes>","expects":"DeveloperReadySpec"}]})

    stop_conditions = [
        "If acceptance criteria for critical paths are missing, ask the ticket author.",
        "If a breaking change is required, produce a migration/rollout plan and get approval."
    ]
    notes = [
        "Paste outputs between agents as raw JSON to keep them deterministic.",
        "Use Security for auth/PII/tenancy/webhooks; use Perf for hot paths and list/search endpoints.",
        "If FE is impacted, set --fe to include FE spec/implement phases."
    ]

    return {
        "stack": stack,
        "commit_type": commit_type,
        "phases": phases,
        "stop_conditions": stop_conditions,
        "notes": notes
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stack", required=True, choices=["rails","laravel","generic"])
    ap.add_argument("--type", required=True, choices=["feat","fix","refactor","perf","style","test","docs","build","ops","chore"])
    ap.add_argument("--impl", action="store_true")
    ap.add_argument("--release", action="store_true")
    ap.add_argument("--security", action="store_true")
    ap.add_argument("--perf", dest="perf_flag", action="store_true")
    ap.add_argument("--no-backlog", action="store_true")
    ap.add_argument("--fe", action="store_true", help="Include FE architect/implementer phases")

    # output organization
    ap.add_argument("--ticket", help="Ticket id (e.g., PROJ-123, LIN-44). If provided, writes to runs/<ticket>_<slug>_<timestamp>/pipeline_plan.json")
    ap.add_argument("--title", help="Short description used for folder slug when --ticket is provided")
    ap.add_argument("--out-dir", default="runs", help="Base output directory for run folders (default: runs)")
    args = ap.parse_args()

    # sensible defaults if user doesn't set flags:
    default = {
        "feat":  {"impl":True,  "release":True,  "security":True,  "perf":False, "backlog":True},
        "fix":   {"impl":True,  "release":True,  "security":True,  "perf":False, "backlog":False},
        "refactor":{"impl":True,"release":False, "security":False, "perf":False, "backlog":False},
        "perf":  {"impl":True,  "release":True,  "security":False, "perf":True,  "backlog":False},
        "style": {"impl":True,  "release":False, "security":False, "perf":False, "backlog":False},
        "test":  {"impl":True,  "release":False, "security":False, "perf":False, "backlog":False},
        "docs":  {"impl":False, "release":False, "security":False, "perf":False, "backlog":False},
        "build": {"impl":True,  "release":True,  "security":False, "perf":False, "backlog":False},
        "ops":   {"impl":True,  "release":True,  "security":True,  "perf":True,  "backlog":False},
        "chore": {"impl":True,  "release":False, "security":False, "perf":False, "backlog":False},
    }[args.type]

    impl = args.impl or default["impl"]
    release = args.release or default["release"]
    security = args.security or default["security"]
    perf = args.perf_flag or default["perf"]
    backlog = (not args.no_backlog) and default["backlog"]

    plan = build_plan(args.type, args.stack, impl, release, security, perf, backlog, include_fe=args.fe)

    # If ticket is provided, write to run folder (no overwrites)
    if args.ticket:
        title = args.title or args.ticket
        ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        folder = f"{args.ticket}_{slugify(title)}_{ts}"
        out_base = Path(args.out_dir)
        out_dir = out_base / folder
        out_dir.mkdir(parents=True, exist_ok=False)
        out_file = out_dir / "pipeline_plan.json"
        out_file.write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
        print(str(out_file))
        return

    # Otherwise print to stdout
    print(json.dumps(plan, indent=2))

if __name__ == "__main__":
    main()
