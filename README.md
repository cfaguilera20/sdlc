# SDLC Multi‑Agent Pipeline for Cursor (Rails + Laravel)

This repo is a **copy‑paste friendly** multi-agent workflow:
- A single **Orchestrator** decides which agents to run for a ticket.
- Every agent uses a **standard input/output contract** (JSON schemas).
- Works for **Jira** or **Linear** tickets by pasting the ticket text.

> You can use these as **Cursor custom agents** (paste prompt content) or as templates to keep consistent workflows across teams.

## Folder layout
- `agents/` — the agent prompts (Markdown)
- `schemas/` — JSON schemas for standardized outputs
- `templates/` — pipeline plan template
- `examples/` — sample ticket + sample structured outputs
- `.cursor/rules/` — optional Cursor rules file (team-wide behavior)

## Quick start (manual run inside Cursor)
1. Create agents in Cursor:
   - Orchestrator: `agents/00_orchestrator.md`
   - Ticket Reader: `agents/01_ticket_reader.md`
   - Product Analyst: `agents/02_product_analyst.md`
   - Architect (Rails): `agents/03a_architect_rails.md`
   - Architect (Laravel): `agents/03b_architect_laravel.md`
   - QA Designer: `agents/04_qa_designer.md`
   - Optional: Security, Perf/Obs, Implementer, Reviewer, Release/Ops

2. Paste a ticket into **Orchestrator** and tell it your stack:
   - `stack=rails` or `stack=laravel`
   - Provide any repo conventions (auth, tenancy, test framework)

3. Run each phase:
   - Agent 01 → produce `TicketContext`
   - Agent 02 → produce `Backlog` (if needed)
   - Agent 03A/03B → produce `DeveloperReadySpec`
   - Agent 04 → produce `TestSuite`

4. (Optional) Implement:
   - Agent 07A/07B creates a precise edit plan (file-by-file)
   - You apply the edits in Cursor
   - Agent 08 reviews the diff and creates a punch list

## Standard contracts
All JSON outputs should validate against:
- `schemas/ticket_context.schema.json`
- `schemas/backlog.schema.json`
- `schemas/spec.schema.json`
- `schemas/test_suite.schema.json`

## Example run
Use the included example ticket:

- Raw ticket: `examples/jira_linear/ticket_raw.txt`
- Example TicketContext: `examples/jira_linear/ticket_context.json`

Suggested pipeline for a typical backend change:
1) 01_ticket_reader  
2) 02_product_analyst (only if scope > 1 small story)  
3) 03A (Rails) or 03B (Laravel)  
4) 05_security_privacy (if auth/PII/tenancy)  
5) 06_perf_observability (if performance‑sensitive)  
6) 04_qa_designer  
7) 07 implementer (optional)  
8) 08 reviewer  
9) 09 release_ops (optional)

## Adding a new agent
Create a new prompt in `agents/` and ensure:
- It consumes one of the existing JSON outputs (or raw ticket text).
- It outputs JSON matching an existing schema (or add a new schema).
- It lists concrete `files_touched` when proposing code changes.

## Notes for Jira/Linear
If you can paste the ticket as text, Agent 01 is enough.
If you have API access, you can later add a small fetch script, but this repo keeps things **tool-agnostic** so it works anywhere.

---

Generated: 2025-12-25


## PipelinePlans by Conventional Commit type

You asked for **ready-to-use PipelinePlan examples** for common ticket types (mapped to conventional commits).

They live in:
- `examples/pipeline_plans/`  
  e.g. `examples/pipeline_plans/rails_feat.pipeline_plan.json`

### What PipelinePlan means in Cursor
A `PipelinePlan` is just a **runbook**: it tells you which agent to run next and what to paste.

**You do not need an external orchestrator tool.** The orchestrator is just another Cursor agent prompt.

### How to use this in Cursor (step-by-step)

1) **Create the agents**
- In Cursor → Agents (Custom Agents) → Create:
  - Name: `SDLC Orchestrator`
  - Prompt: paste the full content of `agents/00_orchestrator.md`
- Repeat for the other agents you want (Ticket Reader, Architect, QA, etc) using the files in `agents/`.

2) **Run the Orchestrator**
- Open the Jira/Linear ticket.
- Copy **title + description + key comments**.
- In Cursor chat, select agent **SDLC Orchestrator** and send:

Example (Rails + feat):
```
stack=rails
commit_type=feat

TICKET:
<PASTE JIRA/LINEAR TEXT HERE>
```

The orchestrator should return a **PipelinePlan JSON**.

3) **Execute the plan**
- Run each agent listed in the plan **in order**.
- For each step:
  - Copy the **JSON output** from the previous agent
  - Paste it as input to the next agent (no extra prose)

4) **Implementation workflow**
- After you have the final `DeveloperReadySpec` + `TestSuite`,
  run `07A/07B Implementer` to get a file-by-file edit plan.
- Apply the edits in the editor (Cursor).
- Then run `08 Code Reviewer` with:
  - the final spec JSON
  - the diff/changed files
  - test output (if available)

### Using the generator script (optional)
If you want a quick starting PipelinePlan without running the orchestrator first:

```bash
python scripts/generate_pipeline_plan.py --stack rails --type feat > pipeline_plan.json
python scripts/generate_pipeline_plan.py --stack laravel --type fix > pipeline_plan.json
python scripts/generate_pipeline_plan.py --stack rails --type perf > pipeline_plan.json
```

Then follow the plan manually by running those agents in Cursor.

### When should you still use the Orchestrator?
- When the ticket is ambiguous and needs assumptions/questions.
- When you suspect multiple stories are hidden in one ticket.
- When you want the pipeline to auto-add Security/Perf/Release phases based on content.

### Mapping cheat sheet
- `feat` → use Backlog + Spec + QA + Implement + Review (+ Release)
- `fix` → Spec + QA + Implement + Review (+ Security if auth/tenancy)
- `refactor` → Spec (light) + QA (focus regression) + Review
- `perf` → Spec + Perf/Obs + QA + Review (+ Release if risky)
- `style`/`test`/`docs` → minimal pipeline (often skip backlog)

Generated: 2025-12-25


## Frontend agent (FE)

Added:
- `agents/03c_architect_frontend.md` — FE spec generator
- `agents/07c_implementer_frontend.md` — FE implementer

### When to run FE agents
- The ticket touches **UI**, **UX**, **forms**, **client-side validation**, **routing**, **state**, or **frontend performance**.
- Or when the BE change requires coordinated FE updates (new endpoint, new payload, etc.).

### Minimal FE pipeline (example)
1) 01 Ticket Reader  
2) 03A/03B BE Architect (if API changes)  
3) 03C FE Architect  
4) 04 QA  
5) 07C FE Implementer (optional)  
6) 08 Reviewer

### Less copy/paste: "One-message Orchestrator" mode
In Cursor, ask the orchestrator to return everything in one JSON bundle.

Example prompt:
```
stack=laravel
commit_type=feat
mode=one_message

Run the pipeline end-to-end and return ONE JSON with:
- ticket_context
- backlog (only if needed)
- spec (include BE + FE implementation_plan)
- test_suite

TICKET:
<paste jira/linear ticket>
```


## Output organization (avoid overwrites)

If you reuse the same agents across multiple projects, **do not write outputs to a single shared `output/` folder**.
Instead, store each run under a unique folder keyed by **ticket id + short slug + timestamp**.

Recommended structure:
- `runs/<TICKET>_<short-slug>_<YYYYMMDD_HHMMSS>/`
  - `ticket.txt` (raw pasted ticket)
  - `pipeline_plan.json`
  - `ticket_context.json`
  - `spec.json`
  - `test_suite.json`

This prevents overwrites and makes it easy to compare runs.

### Quick run creation
Create a run folder skeleton:
```bash
python scripts/new_run.py --ticket PROJ-123 --title "SSO email mismatch"
```

Generate a plan into a unique folder (no overwrite):
```bash
python scripts/generate_pipeline_plan.py --stack rails --type feat --ticket PROJ-123 --title "SSO email mismatch"
# prints the path to runs/.../pipeline_plan.json
```

### Git hygiene
This repo includes a `.gitignore` entry for `runs/*` so you can keep runs local.
If you *do* want to commit certain runs (for audits), remove that line or move the run into a tracked folder.

Generated: 2025-12-26


### Orchestrator modes
- **interactive (default):** Orchestrator returns a `PipelinePlan`. You run each agent step-by-step.
- **one_message:** Orchestrator returns a single combined JSON bundle: `ticket_context`, optional `backlog`, `spec`/`specs`, `test_suite`/`test_suites`.

Example (one_message):
```
stack=rails
commit_type=fix
mode=one_message

Run the pipeline end-to-end and return ONE JSON bundle.

TICKET:
<paste jira/linear ticket>
```

Generated: 2025-12-26


## Integration & Platform Planner (02A)

Added:
- `agents/02a_integration_planner.md` — identifies service boundaries + contracts + integration risks
- `schemas/integration_plan.schema.json`

### Where it fits in the pipeline
Run it **after Ticket Reader** and **before Backlog** when the ticket involves other services or creating a new service:

1) 01 Ticket Reader → `TicketContext`  
2) 02A Integration Planner → `IntegrationPlan`  
3) 02 Product Analyst → backlog includes explicit integration stories + dependencies  
4) Architect(s) → specs align to integration contracts  

### Orchestrator (interactive) prompt example
```
stack=rails
commit_type=feat
mode=interactive

Ticket affects other services. Include IntegrationPlan.
TICKET:
<paste ticket>
```

Generated: 2025-12-26


## Data Migration Strategist (02B)

Added:
- `agents/02b_data_migration_strategist.md`
- `schemas/data_migration_plan.schema.json`

### Where it fits
Run after Ticket Reader (and after Integration Planner if applicable):

1) 01 Ticket Reader → `TicketContext`  
2) 02A Integration Planner → `IntegrationPlan` (optional)  
3) 02B Data Migration Strategist → `DataMigrationPlan` (optional but recommended for migrations)  
4) 02 Product Analyst → backlog includes migration tasks + dependencies  
5) Architects → specs align to phased migration plan  

Generated: 2025-12-26


## Additional SDLC agents

### 02C — Domain Modeler
Clarifies entities, invariants, and domain rules before design.

### 02D — Risk & Rollout Planner
Defines feature flags, rollout phases, metrics, and rollback triggers.

### 03D — Contract Validator
Normalizes API/event contracts for BE/FE and integrations.

These agents are **conditional** and only used when the ticket complexity warrants them.

Generated: 2025-12-26


## Migration Modernization Auditor (02E)

Added:
- `agents/02e_migration_modernization_auditor.md`

### Why this exists
When extracting/migrating from a monolith, the danger is doing a *lift-and-shift* of legacy coupling and anti-patterns.
02E forces a **target-state design** and framework best practices (Rails/Laravel) so the new service improves quality rather than preserving debt.

### Where it fits
1) 01 Ticket Reader  
2) 02A Integration Planner (optional)  
3) 02B Data Migration Strategist (migration/backfill/cutover)  
4) **02E Modernization Auditor (avoid legacy anti-patterns)**  
5) Architects (03A/03B/03C) finalize specs  
6) QA + Implement + Review + Release  

Generated: 2025-12-26


## Domain Expert (suggested) — Option A

Added: `templates/domain_expert_agent_prompt.md`

Use when ticket requirements are ambiguous or written by someone without deep domain knowledge (Payroll, Recruitment, Employee Admin, etc.).
Run it **after** Ticket Reader and **before** Product Analyst so backlog and specs reflect correct domain rules.

Generated: 2025-12-26


## DomainKnowledgePack (formal schema)

Added:
- `schemas/domain_knowledge_pack.schema.json`
- `templates/domain_expert_payroll_split.md`

Agent 02 (Product Analyst) now explicitly accepts one or multiple `DomainKnowledgePack` inputs and must weave rules/edge cases into backlog acceptance criteria.

Generated: 2025-12-26


## How it works (high-level)

You run this inside **Cursor** using the **Orchestrator** plus specialized agents.  
The Orchestrator decides which agents to run based on the ticket and your `stack` + `commit_type`.

### Modes
- **interactive (default):** Orchestrator returns a `PipelinePlan`; you run agents step-by-step.
- **one_message:** Orchestrator returns a single JSON bundle (`ticket_context`, optional `backlog`, `spec/specs`, `test_suite/test_suites`, and optional integration/migration artifacts).

### Typical sequence (Mermaid)

```mermaid
sequenceDiagram
  autonumber
  actor Dev as You (Cursor)
  participant Orch as 00 Orchestrator
  participant TR as 01 Ticket Reader
  participant DE as Domain Expert (suggested)
  participant IP as 02A Integration Planner
  participant DM as 02B Data Migration Strategist
  participant MA as 02E Modernization Auditor
  participant PA as 02 Product Analyst
  participant RA as 03A/03B BE Architect
  participant FE as 03C FE Architect
  participant Sec as 05 Security
  participant Perf as 06 Perf/Obs
  participant QA as 04 QA Designer
  participant ImplBE as 07A/07B BE Implementer
  participant ImplFE as 07C FE Implementer
  participant Rev as 08 Code Reviewer
  participant Ops as 09 Release/Ops

  Dev->>Orch: Paste ticket + stack + commit_type (+ mode)
  Orch->>TR: Run Ticket Reader
  TR-->>Orch: TicketContext JSON

  alt Ticket is thin / domain-heavy
    Orch->>DE: Suggest DomainKnowledgePack (1..N experts)
    DE-->>Orch: DomainKnowledgePack(s) JSON
  end

  alt Integrations / new service involved
    Orch->>IP: Run Integration Planner
    IP-->>Orch: IntegrationPlan JSON
  end

  alt Migration / service extraction / data movement
    Orch->>DM: Run Data Migration Strategist
    DM-->>Orch: DataMigrationPlan JSON
    Orch->>MA: Run Modernization Auditor (avoid legacy patterns)
    MA-->>Orch: ModernizationPlan JSON
  end

  Orch->>PA: Build Backlog (stories + AC + deps)
  PA-->>Orch: Backlog JSON

  Orch->>RA: Produce BE DeveloperReadySpec
  RA-->>Orch: Spec JSON

  opt UI impacted
    Orch->>FE: Produce FE Spec (aligned to contracts)
    FE-->>Orch: Spec JSON (FE tasks)
  end

  opt Security sensitive
    Orch->>Sec: Threat model + privacy checks
    Sec-->>Orch: Updated Spec JSON
  end

  opt Performance sensitive
    Orch->>Perf: Perf + observability plan
    Perf-->>Orch: Updated Spec JSON
  end

  Orch->>QA: Produce TestSuite
  QA-->>Orch: TestSuite JSON

  opt Implement now
    Orch->>ImplBE: Apply Spec to repo (BE)
    ImplBE-->>Orch: Updated Spec JSON
    opt FE implementation
      Orch->>ImplFE: Apply FE spec to repo
      ImplFE-->>Orch: Updated Spec JSON
    end
    Orch->>Rev: Review diff + tests
    Rev-->>Orch: Review notes / updated TestSuite
  end

  opt Release required
    Orch->>Ops: Deploy + migration + rollout runbook
    Ops-->>Orch: Release notes / runbook
  end

  Orch-->>Dev: (interactive) Next agent to run OR (one_message) Full JSON bundle
```

### What you paste in Cursor (quick templates)

**Interactive (default):**
```
stack=rails
commit_type=fix
mode=interactive

Here is the ticket. Build a PipelinePlan and tell me the next agent to run.

TICKET:
<paste Jira/Linear ticket>
```

**One-message (no handoff):**
```
stack=laravel
commit_type=feat
mode=one_message

Run the pipeline end-to-end and return ONE JSON bundle with:
- ticket_context
- backlog (only if needed)
- spec (include BE + FE if UI impacted)
- test_suite
- integration_plan / data_migration_plan / modernization_plan if applicable

TICKET:
<paste Jira/Linear ticket>
```


---

## XML-Structured Prompting (recommended)

Added: `templates/xml_prompting_guide.md`

If you saw the Anthropic XML-tags idea: yes, it's useful here.
It reduces “blob prompt” ambiguity by separating **instructions vs context vs schemas**.

Start here:
- `templates/xml_prompting_guide.md`
Examples:
- `examples/xml_vs_blob/` (blob vs tagged)

Generated: 2025-12-26


---

## 07W — Code Writer (actually edits files)

If your pipeline ends with an **ImplementationPlan** but no code was written, that’s expected:
- Implementer agents plan.
- **07W writes**.

Added:
- `agents/07w_code_writer.md`

How to use:
1) Run Architect + QA + Implementer(s) until you have ImplementationPlan JSON(s).
2) Run **07W** with those JSONs pasted in.
3) Then run 08 (review) and 09 (release).

Generated: 2025-12-28


---

## Domain templates (scalable structure)

We group domain-specific experts under:

- `templates/domains/<domain>/`
- `templates/domains/<domain>/examples/`

Payroll specialists added:
- `templates/domains/payroll/domain_expert_payroll_mx_imss.md`
- `templates/domains/payroll/domain_expert_payroll_mx_infonavit.md`

To propose new domain specialists:
- `agents/01x_domain_agent_scout.md`

Generated: 2025-12-28


---

## Estructura por dominio (simple y plana)

Para evitar redundancia, usamos una estructura **plana por dominio**:

- `sdlc/templates/domains/<domain>/*.md` → agentes/prompts de dominio
- `sdlc/templates/domains/<domain>/examples/*.json` → ejemplos DomainKnowledgePack
- `sdlc/templates/domains/_shared/*.md` → prompts compartidos

Ejemplo Payroll:
- `sdlc/templates/domains/payroll/domain_expert_payroll_mx_imss.md`
- `sdlc/templates/domains/payroll/examples/domain_knowledge_pack_payroll_mx_imss.json`

Generated:
 2025-12-28


---

## 01X “materialize” (crear nuevos agentes de dominio automáticamente)

El Domain Agent Scout (01X) ahora puede **proponer y materializar** nuevos agentes de dominio, entregando:
- el **template .md** del agente (prompt listo para copiar)
- un **example DomainKnowledgePack .json** (forma esperada del output)

Estructura:
- `sdlc/templates/domains/<domain>/*.md`
- `sdlc/templates/domains/<domain>/examples/*.json`

### Aplicar el materialize con script (opcional)

1) Guarda el output JSON de 01X en un archivo (ej. `runs/<ticket>/suggested_domain_agents.json`)
2) Ejecuta:

```bash
python3 scripts/apply_materialize.py runs/<ticket>/suggested_domain_agents.json
```

Esto crea/escribe los archivos listados en `materialize.files[]`.

Generated: 2025-12-28

Tip: `chmod +x scripts/apply_materialize.py` if you want to run it directly.
