# Run Checklist (SDLC)

Use this short checklist for consistent execution.

## Start
- Create run folder (`/new-run` or `scripts/new_run.py`)
- Paste raw ticket into `runs/.../ticket.txt`
- Run `/run-orchestrator` (or manual Agent 00)

## Plan
- Run agents in the PipelinePlan order
- Save each JSON artifact into the run folder
- Validate outputs (`/validate-run` or `scripts/validate_run.py`)

## Implement (optional)
- Use Implementer (07A/07B/07C) to create an implementation plan
- Apply changes (07W) and review (08)
- Re-run validations if spec/test changed

## Release (if needed)
- Run `/release-plan` (Agent 09)
- Capture rollout + rollback steps

## Close
- Ensure artifacts are saved and validated
- Optional: update `notes.md` and `decision.md`
