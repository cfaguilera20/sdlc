# SDLC Pipeline Rules (Team-wide)

These rules are intended to make agent outputs **copy/paste safe**, **schema-valid**, and **consistent across developers**.

## Non-negotiables

1) **JSON-only when a schema is specified**
- If an agent prompt says "Return ONLY JSON" / references `/schemas/...`, output **only** a single JSON object (or array if the schema says so).
- No markdown fences, no prose, no extra keys.

2) **Always validate against schemas**
- After producing any artifact, validate it with:
  - `python3 scripts/validate_json_schema.py schemas/<schema>.schema.json <path-to-json>`
- Fix schema issues immediately; do not push invalid JSON downstream.
- **All schemas:** `ticket_context`, `backlog`, `spec`, `test_suite`, `test_code_set`, `test_coverage_report`, `spec_compliance_report`, `spec_diff_report`, `code_change_set`, `codebase_architecture`, `integration_plan`, `pipeline_plan`, `domain_knowledge_pack`, `domain_scaffold`, `data_migration_plan`, `features`

3) **Use run folders for persistence**
- All outputs for a ticket belong under:
  - `runs/<TICKET>_<short-slug>_<YYYYMMDD_HHMMSS>/`
- Create the folder first:
  - `python3 scripts/new_run.py --ticket PROJ-123 --title "short title"`

4) **One-message mode: persist incrementally**
- If you run `mode=one_message`, you must not "hold everything in memory" until the end.
- Save each artifact into the run folder as soon as it is produced. If the chat crashes, you still keep partial results.
- **Save incrementally:** `ticket_context.json`, `backlog.json`, `spec.json`, `test_suite.json`, `test_code_set.json`, `codebase_architecture.json`, `integration_plan.json`, `pipeline_plan.json` as each is generated.

5) **Markdown files go in the run folder**
- Any generated `.md` (notes, decisions, checklists) must be saved under the run folder (not repo root).

6) **Domain scaffolding must be materialized**
- When `01x_domain_agent_scout` outputs `materialize.files[]`, the files **must exist in the repo**.
- Apply via:
  - `python3 scripts/apply_materialize.py <01x_output.json>`

7) **Create Rails/Laravel projects via Docker when local tools aren't installed**
- **IMPORTANT:** All new projects MUST be created in the `projects/` folder
- Laravel: `docker run --rm -v $(pwd)/projects:/app -w /app composer:latest create-project laravel/laravel <project_name>`
- Rails: `docker run --rm -v $(pwd)/projects:/app -w /app ruby:latest rails new <project_name>`
- If tools are available locally: `cd projects && [rails new|composer create-project] <project_name> && cd ..`

8) **Test-Driven Development (TDD) workflow**
- When TDD mode is enabled or requested:
  - Agent 07T (Test Writer) writes test code **before** implementation
  - Tests should initially fail (this is expected in TDD)
  - Agent 08C (Test Coverage Validator) validates all spec elements have tests
  - Agent 07A/07B (Implementer) implements code to make tests pass
  - Save `test_code_set.json` and `test_coverage_report.json` in run folder

9) **Spec-driven development enforcement**
- All code must have a corresponding `DeveloperReadySpec`
- Agent 08A (Spec Compliance Validator) validates code matches spec
- Agent 08C (Test Coverage Validator) ensures all spec elements are tested
- Save `spec_compliance_report.json` and `test_coverage_report.json` in run folder

10) **Codebase analysis before specs**
- When starting on a new codebase or unfamiliar area:
  - Run Agent 00A (Codebase Analyzer) first
  - Use `codebase_architecture.json` to inform spec creation
  - Save `codebase_architecture.json` in run folder

11) **Commit type is required**
- Orchestrator MUST always ask for `commit_type` if not provided
- Present conventional commit options: feat, fix, refactor, perf, style, test, docs, chore, ci, build
- Validate commit_type matches one of the options before proceeding

12) **Fast-track mode for small tickets**
- Automatically enabled for: `fix`, `refactor`, `style`, `test`, `docs` commit types
- Can be manually overridden with `fast_track=true` or `fast_track=false`
- Fast-track skips optional agents but maintains quality (QA + Review still required)
- Uses lightweight architect mode for simplified specs


