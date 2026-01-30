# SDLC Command Reference

This page lists the reusable commands that make the SDLC pipeline feel one-step instead of manual.

## Command Index

| Command | Purpose | Output |
|---------|---------|--------|
| `/run-orchestrator` | Run Agent 00 and return a PipelinePlan JSON | `pipeline_plan.json` |
| `/create-sdlc-config` | Generate project config for consistent planning | `sdlc-config.md` |
| `/update-test-cases` | Update acceptance criteria + test cases for a ticket | `ticket_context.json`, `test_suite.json` |
| `/update-from-main` | Safely update local branch from `main` | Updated local branch |
| `/new-run` | Create a new run folder with placeholders | Run folder path |
| `/validate-run` | Validate all JSON artifacts in a run folder | Validation output |
| `/split-bundle` | Split one-message bundle into run artifacts | Updated run folder |
| `/triage-ticket` | Fast scope clarification (Ticket Reader / Domain Scout) | `ticket_context.json` (+ `domain_scaffold.json`) |
| `/update-spec` | Update spec after requirement changes | `spec.json` |
| `/release-plan` | Generate release/runbook plan | Updated `spec.json` |
| `/update-mcp` | Generate `.cursor/mcp.json` from tool versions | `.cursor/mcp.json` |
| `/feature-implementation-methodology` | Full methodology prompt for feature planning | N/A |

## /run-orchestrator

Use when you want a one-step start to the pipeline.

Inputs:
- `stack` (rails/laravel/other)
- `commit_type` (feat/fix/refactor/perf/style/test/docs/chore/ci/build)
- Ticket text or `runs/.../ticket.txt`

Output:
- PipelinePlan JSON (save as `runs/.../pipeline_plan.json`)

## /create-sdlc-config

Use to set up or update project-specific planning context.

Output:
- `sdlc-config.md` at repo root

Template:
- `templates/sdlc-config.example.md`

## /update-test-cases

Use when acceptance criteria or tests need updates without re-running the full pipeline.

Inputs:
- `ticket_context.json` or raw ticket text
- `spec.json` (optional but recommended)
- `test_suite.json` (if updating tests)

Outputs:
- Updated `ticket_context.json` and/or `test_suite.json`

## /update-from-main

Use to update your branch safely with automatic backups and conflict guidance.

Command:
```
./scripts/update-from-main.sh
```

## /new-run

Use to create a run folder and required placeholders.

Command:
```
python3 scripts/new_run.py --ticket PROJ-123 --title "short title"
```

## /validate-run

Use to validate all JSON outputs in a run folder.

Command:
```
python3 scripts/validate_run.py runs/PROJ-123_slug_YYYYMMDD_HHMMSS
```

## /split-bundle

Use after one-message mode to split `bundle.json`.

Command:
```
python3 scripts/split_one_message_bundle.py runs/.../bundle.json runs/PROJ-123_slug_YYYYMMDD_HHMMSS
```

## /triage-ticket

Use to quickly clarify scope without running the full pipeline.

Outputs:
- `ticket_context.json`
- `domain_scaffold.json` (if domain is ambiguous)

## /update-spec

Use to update `spec.json` after requirement changes.

Inputs:
- Updated ticket context
- Existing `spec.json`

## /release-plan

Use to generate deployment/runbook steps for risky changes.

Inputs:
- Latest `spec.json`

## /update-mcp

Use to generate `.cursor/mcp.json` from `.tool-versions` and the template.

Command:
```
python3 scripts/update_mcp_from_tool_versions.py
```

## /feature-implementation-methodology

Use when you want the full planning/implementation methodology prompt.

Command file:
- `.cursor/commands/feature-implementation-methodology.md`
