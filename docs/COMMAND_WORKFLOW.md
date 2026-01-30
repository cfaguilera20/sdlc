# Command Workflow (Cursor-first)

This doc provides a simple “command vocabulary” (inspired by [`masta-g3/rules`](https://github.com/masta-g3/rules)) that maps to **our orchestrator + agents + run-folder artifacts**.

Goal: every dev follows the same flow and produces the same structured outputs.

## Artifact-only prompting (Ralph loop friendly)

In Cursor, keep each agent run focused on **artifacts**, not chat history:
- Reference `runs/.../*.json` files (use `@` file references when possible).
- Add only a short instruction for the current step.
- Avoid pasting long conversations; they create drift and bloated context.

## The 4 commands

### 1) **prime** (understand + create run folder)

**You do:**
1. Create a run folder:
   - `python3 scripts/new_run.py --ticket PROJ-123 --title "short title"`
2. Paste the raw ticket into:
   - `runs/.../ticket.txt`
3. Run the orchestrator in Cursor to get the pipeline:
   - Agent: `00_orchestrator`
   - Input includes `stack=...`, `commit_type=...`, and the ticket text.

**Output(s):**
- `runs/.../pipeline_plan.json` (orchestrator output)

### 2) **plan** (produce schema-valid JSON artifacts)

Follow the plan phases and run agents in Cursor, saving each output into the run folder:

- `01_ticket_reader` → `ticket_context.json`
- `02_product_analyst` (optional) → `backlog.json`
- `03a_architect_rails` / `03b_architect_laravel` / `03_technical_architect_generic` → `spec.json`
- `04_qa_designer` → `test_suite.json`

**Validate as you go:**
- `python3 scripts/validate_run.py runs/...`

### 3) **execute** (implement)

If implementing now:
- `07a_implementer_rails` or `07b_implementer_laravel` produces an implementation plan inside the spec
- `07w_code_writer` applies changes to the repo and returns `CodeChangeSet`
- `08_code_reviewer` reviews + punch list
- optionally `09_release_ops`

### 4) **commit** (close the loop)

Before merging/PR:
1. Validate the run folder:
   - `python3 scripts/validate_run.py runs/...`
2. Keep any notes/checklists as `.md` **inside the run folder**.

## Features workflow (multi-session velocity)

For larger epics where multiple people work across sessions, use `features.json` to track status and dependencies.

### Create a features file

```bash
python3 scripts/features.py init --project-id PROJ-123 --title "SSO email mismatch" --out features.json
```

### Import backlog stories

```bash
python3 scripts/features.py import-backlog runs/.../backlog.json --features features.json --run-dir runs/PROJ-123_short-title_YYYYMMDD_HHMMSS
```

### Pick the next ready feature

```bash
python3 scripts/features.py next --features features.json
```

Or claim it:

```bash
python3 scripts/features.py next --features features.json --claim
```

### Update status

```bash
python3 scripts/features.py set-status --features features.json --id PROJ-123-1 --status done
```

### Validate features file (optional but recommended)

```bash
python3 scripts/validate_json_schema.py schemas/features.schema.json features.json
```

## Orchestrator + “features” (how they fit together)

- Orchestrator is still the **source of truth** for which agents to run and in what order.
- `features.json` is a **lightweight tracker** for multi-session work, typically driven by `Backlog.stories[]`.
- Recommended approach:
  1. Run Orchestrator → produce `pipeline_plan.json`
  2. Run 01/02 → produce `ticket_context.json` + `backlog.json`
  3. Import backlog into `features.json`
  4. Each dev claims a feature and executes the corresponding spec/implementation work

