# SDLC Agents Reference

Complete reference guide for all agents in the SDLC pipeline. Each agent is a specialized AI prompt designed to work within Cursor IDE.

## Table of Contents

- [Core Pipeline Agents](#core-pipeline-agents)
- [Analysis & Planning Agents](#analysis--planning-agents)
- [Architecture Agents](#architecture-agents)
- [Implementation Agents](#implementation-agents)
- [Quality & Validation Agents](#quality--validation-agents)
- [Domain & Specialized Agents](#domain--specialized-agents)

---

## Core Pipeline Agents

### Agent 00 — Orchestrator
**File:** `agents/00_orchestrator.md`  
**Role:** Central controller that decides which agents to run and in what order based on ticket content.  
**Input:** Ticket text, stack (rails/laravel), commit_type (feat/fix/etc - **required**), mode (interactive/one_message), fast_track (optional override)  
**Output:** `PipelinePlan` JSON or combined JSON bundle  
**When to use:** Always start here. First agent in every workflow.

**Required Input:**
- `commit_type` is **mandatory** - if missing, orchestrator will ask with conventional commit options:
  - `feat`, `fix`, `refactor`, `perf`, `style`, `test`, `docs`, `chore`, `ci`, `build`

**Modes:**
- **Interactive (default):** Returns PipelinePlan, you run agents step-by-step
- **One-message:** Returns complete JSON bundle with all artifacts

**Fast-Track Mode:**
- **Automatic:** Enabled for `commit_type` = `fix`, `refactor`, `style`, `test`, `docs`
- **Manual:** Set `fast_track=true` or `fast_track=false` to override
- **Skips:** Product Analyst, Integration Planner, Migration Strategist, Spec Compliance Validator, Test Coverage Validator
- **Uses:** Lightweight Architect mode for simplified specs

---

### Agent 01 — Ticket Reader
**File:** `agents/01_ticket_reader.md`  
**Role:** Extracts structured context from Jira/Linear tickets or plain text.  
**Input:** Raw ticket text (title + description + comments)  
**Output:** `TicketContext` JSON (`schemas/ticket_context.schema.json`)  
**When to use:** First step after orchestrator (or included in one-message mode)

**Output includes:**
- Ticket metadata (id, title, source, priority)
- Domain context (entities, integrations, constraints)
- Acceptance criteria (atomic, testable)
- Non-functionals (performance, security, reliability)
- Assumptions, risks, glossary

---

### Agent 02 — Product Analyst
**File:** `agents/02_product_analyst.md`  
**Role:** Converts ticket context into INVEST-compliant user stories and prioritized backlog.  
**Input:** `TicketContext` JSON (from Agent 01)  
**Output:** `Backlog` JSON (`schemas/backlog.schema.json`)  
**When to use:** When ticket scope is unclear or contains multiple stories

**Output includes:**
- Epic definition
- User stories with INVEST criteria
- Acceptance criteria (observable, testable)
- Priorities (P0-P3)
- Dependencies
- Out-of-scope items (for future prioritization)

---

## Analysis & Planning Agents

### Agent 00A — Codebase Analyzer
**File:** `agents/00a_codebase_analyzer.md`  
**Role:** Analyzes existing codebase to understand architecture, tech stack, patterns, and conventions.  
**Input:** Codebase structure, config files, key source files, documentation  
**Output:** `CodebaseArchitecture` JSON (`schemas/codebase_architecture.schema.json`)  
**When to use:** Before creating specs on a new codebase or unfamiliar area

**Output includes:**
- Tech stack (framework, language, dependencies, database, infrastructure)
- Architecture patterns (MVC, Service Layer, DDD, etc.)
- System design (components, API style, authentication)
- Code organization and naming conventions
- Database design and ORM patterns
- Testing strategy and frameworks
- Recommendations for alignment

---

### Agent 02A — Integration & Platform Planner
**File:** `agents/02a_integration_planner.md`  
**Role:** Identifies service boundaries, contracts, and integration risks for multi-service work.  
**Input:** `TicketContext` or `Backlog` JSON  
**Output:** `IntegrationPlan` JSON (`schemas/integration_plan.schema.json`)  
**When to use:** When ticket involves:
- Integrating with another service
- Creating a new service
- Webhooks, queues, SSO, external APIs
- Cross-team dependencies

**Output includes:**
- Service boundaries and ownership
- API contracts and event schemas
- Integration patterns (sync/async, pub/sub, etc.)
- Authentication and authorization approach
- Error handling and retry strategies
- Testing strategy for integrations

---

### Agent 02B — Data Migration Strategist
**File:** `agents/02b_data_migration_strategist.md`  
**Role:** Plans data migration, service extraction, and data movement strategies.  
**Input:** `TicketContext` or `Backlog` JSON  
**Output:** `DataMigrationPlan` JSON (`schemas/data_migration_plan.schema.json`)  
**When to use:** When ticket involves:
- Data migration
- Service extraction
- Backfill operations
- Dual-write patterns
- Cutover strategies

**Output includes:**
- Migration phases and timeline
- Data mapping and transformation rules
- Dual-write strategy
- Rollback plan
- Validation and verification steps
- Performance considerations

---

### Agent 02C — Domain Modeler
**File:** `agents/02c_domain_modeler.md`  
**Role:** Clarifies entities, invariants, and domain rules before design.  
**Input:** `TicketContext` or `Backlog` JSON  
**Output:** `DomainModel` JSON (embedded)  
**When to use:** When domain rules are complex or ambiguous

---

### Agent 02D — Risk & Rollout Planner
**File:** `agents/02d_risk_rollout_planner.md`  
**Role:** Defines feature flags, rollout phases, metrics, and rollback triggers.  
**Input:** `TicketContext` or `Backlog` JSON  
**Output:** `RolloutPlan` JSON (embedded)  
**When to use:** For high-risk features requiring phased rollout

---

### Agent 02E — Migration Modernization Auditor
**File:** `agents/02e_migration_modernization_auditor.md`  
**Role:** Ensures extracted/migrated services follow framework best practices (Rails/Laravel) and avoid legacy anti-patterns.  
**Input:** `TicketContext`, `DataMigrationPlan`  
**Output:** `ModernizationPlan` JSON (embedded)  
**When to use:** When extracting services from monolith to avoid lift-and-shift of legacy patterns

---

## Architecture Agents

### Agent 03 — Technical Architect (Generic)
**File:** `agents/03_technical_architect_generic.md`  
**Role:** Creates detailed technical specifications for generic/unknown stacks.  
**Input:** `Backlog` JSON, optional `CodebaseArchitecture` JSON  
**Output:** `DeveloperReadySpec` JSON (`schemas/spec.schema.json`)  
**When to use:** When stack is unknown or not Rails/Laravel

---

### Agent 03A — Rails Architect
**File:** `agents/03a_architect_rails.md`  
**Role:** Creates Rails-specific technical specifications.  
**Input:** `Backlog` JSON, optional `CodebaseArchitecture` JSON, optional `lightweight=true` flag  
**Output:** `DeveloperReadySpec` JSON (`schemas/spec.schema.json`)  
**When to use:** For Rails projects

**Lightweight Mode (fast-track):**
- When `lightweight=true` (set automatically for bug fixes/small refactors):
  - Minimal domain model (only what's changing)
  - Focused API contracts (only affected endpoints)
  - Simplified flows (just the fix/change)
  - Skip extensive edge cases and non-functionals (unless critical)
  - Sets `lightweight: true` flag in spec JSON

**Full Spec Mode (default):**
- Domain model (ActiveRecord models, associations, validations)
- API contracts (routes, controllers, request/response formats)
- Data contracts (JSON schemas, serializers)
- Flows (user journeys, business logic)
- Edge cases and error handling
- Non-functionals (performance, security, observability)
- Implementation plan (files to create/modify)

---

### Agent 03B — Laravel Architect
**File:** `agents/03b_architect_laravel.md`  
**Role:** Creates Laravel-specific technical specifications.  
**Input:** `Backlog` JSON, optional `CodebaseArchitecture` JSON, optional `lightweight=true` flag  
**Output:** `DeveloperReadySpec` JSON (`schemas/spec.schema.json`)  
**When to use:** For Laravel projects

**Lightweight Mode (fast-track):**
- When `lightweight=true` (set automatically for bug fixes/small refactors):
  - Minimal domain model (only what's changing)
  - Focused API contracts (only affected endpoints)
  - Simplified flows (just the fix/change)
  - Skip extensive edge cases and non-functionals (unless critical)
  - Sets `lightweight: true` flag in spec JSON

**Full Spec Mode (default):**
- Domain model (Eloquent models, relationships, migrations)
- API contracts (routes, controllers, FormRequests, Resources)
- Data contracts (JSON schemas, API Resources)
- Flows (user journeys, business logic)
- Edge cases and error handling
- Non-functionals (performance, security, observability)
- Implementation plan (files to create/modify)

---

### Agent 03C — Frontend Architect
**File:** `agents/03c_architect_frontend.md`  
**Role:** Creates frontend specifications aligned with backend contracts.  
**Input:** `Backlog` JSON, `DeveloperReadySpec` JSON (from BE architect)  
**Output:** `DeveloperReadySpec` JSON (`schemas/spec.schema.json`)  
**When to use:** When UI is impacted or frontend changes are needed

---

### Agent 03D — Contract Validator
**File:** `agents/03d_contract_validator.md`  
**Role:** Normalizes API/event contracts for BE/FE and integrations.  
**Input:** `DeveloperReadySpec` JSON  
**Output:** `ContractSpec` JSON (embedded)  
**When to use:** When contracts need validation across services

---

## Implementation Agents

### Agent 04 — QA Designer
**File:** `agents/04_qa_designer.md`  
**Role:** Builds test cases and traceability matrix from spec.  
**Input:** `DeveloperReadySpec` JSON  
**Output:** `TestSuite` JSON (`schemas/test_suite.schema.json`)  
**When to use:** Always, after spec creation

**Output includes:**
- Traceability matrix (AC → tests)
- Test cases (unit, integration, e2e, contract, security, performance)
- Automation notes (how to implement in chosen stack)
- Warnings (missing observability, flaky risks, dependencies)

---

### Agent 05 — Security & Privacy Reviewer
**File:** `agents/05_security_privacy.md`  
**Role:** Threat modeling and privacy checks for security-sensitive features.  
**Input:** `DeveloperReadySpec` JSON  
**Output:** Updated `DeveloperReadySpec` JSON with security enhancements  
**When to use:** When ticket touches:
- Authentication/authorization
- PII (personally identifiable information)
- Payments
- Webhooks
- Multi-tenant data
- File uploads

---

### Agent 06 — Performance & Observability Engineer
**File:** `agents/06_perf_observability.md`  
**Role:** Performance planning and observability requirements.  
**Input:** `DeveloperReadySpec` JSON  
**Output:** Updated `DeveloperReadySpec` JSON with performance/observability enhancements  
**When to use:** When ticket is performance-sensitive:
- Lists/search/reports
- Hot paths
- High-traffic endpoints
- Read-heavy operations

---

### Agent 07A — Implementer (Rails)
**File:** `agents/07a_implementer_rails.md`  
**Role:** Creates implementation plan for Rails code.  
**Input:** `DeveloperReadySpec` JSON (Rails), repository context  
**Output:** Updated `DeveloperReadySpec` JSON with detailed implementation plan  
**When to use:** For Rails implementation (before Agent 07W)

**Process:**
- Confirms routes/controller/service boundaries
- Plans migrations and model validations
- Writes request specs first (when feasible)
- Implements code, then adds unit/service specs
- Adds logs/instrumentation

**TDD Mode:** If Agent 07T has created tests, implements code to make them pass.

---

### Agent 07B — Implementer (Laravel)
**File:** `agents/07b_implementer_laravel.md`  
**Role:** Creates implementation plan for Laravel code.  
**Input:** `DeveloperReadySpec` JSON (Laravel), repository context  
**Output:** Updated `DeveloperReadySpec` JSON with detailed implementation plan  
**When to use:** For Laravel implementation (before Agent 07W)

**Process:**
- Confirms routes, controller, request validation
- Plans migrations, Eloquent relationships, constraints
- Writes feature tests first (when feasible)
- Implements code, then unit tests for business rules
- Adds logging/metrics hooks

**TDD Mode:** If Agent 07T has created tests, implements code to make them pass.

---

### Agent 07C — Implementer (Frontend)
**File:** `agents/07c_implementer_frontend.md`  
**Role:** Creates implementation plan for frontend code.  
**Input:** `DeveloperReadySpec` JSON (Frontend), repository context  
**Output:** Updated `DeveloperReadySpec` JSON with detailed implementation plan  
**When to use:** For frontend implementation (before Agent 07W)

---

### Agent 07T — Test Writer (TDD)
**File:** `agents/07t_test_writer.md`  
**Role:** Writes actual test code (RSpec/PHPUnit/Pest) from TestSuite before implementation. Enables Test-Driven Development.  
**Input:** `TestSuite` JSON, `DeveloperReadySpec` JSON, stack info  
**Output:** `TestCodeSet` JSON (`schemas/test_code_set.schema.json`)  
**When to use:** For TDD workflow, after Agent 04 (QA Designer)

**Output includes:**
- Complete test files with runnable code
- Test organization (RSpec: spec/requests/, spec/models/, etc.; PHPUnit: tests/Feature/, tests/Unit/)
- Dependencies (factories, fixtures, helpers)
- Expected initial failures (TDD approach)
- Traceability (tests → spec elements)

**TDD Workflow:**
1. Agent 07T writes tests (they should fail initially)
2. Agent 08C validates test coverage
3. Agent 07A/07B implements code to make tests pass
4. Agent 07W applies code changes
5. Agent 08C validates final coverage

---

### Agent 07W — Code Writer
**File:** `agents/07w_code_writer.md`  
**Role:** Actually applies implementation plan to the repository (writes code files).  
**Input:** `DeveloperReadySpec` JSON with implementation plan, repository context  
**Output:** `CodeChangeSet` JSON (`schemas/code_change_set.schema.json`)  
**When to use:** After implementer agents (07A/07B/07C) have created implementation plan

**Features:**
- Enforces spec compliance
- Generates traceability links (spec → code)
- Rejects non-compliant code
- Updates spec with code references

---

## Quality & Validation Agents

### Agent 08 — Code Reviewer
**File:** `agents/08_code_reviewer.md`  
**Role:** Reviews code changes against spec, correctness, security, performance, and maintainability.  
**Input:** `DeveloperReadySpec` JSON, code diff/changed files, test results  
**Output:** `TestSuite` JSON (repurposed for review findings)  
**When to use:** After Agent 07W applies code changes

**Review checks:**
- Correctness vs acceptance criteria and edge cases
- AuthZ/tenant scoping, input validation, error handling
- Performance (queries, indexes, pagination, N+1)
- Test coverage, determinism, meaningful assertions
- Merge/no-merge decision and punch list

---

### Agent 08A — Spec Compliance Validator
**File:** `agents/08a_spec_compliance_validator.md`  
**Role:** Validates that implemented code strictly adheres to DeveloperReadySpec.  
**Input:** `DeveloperReadySpec` JSON, `CodeChangeSet` JSON, optional `TestSuite` JSON  
**Output:** `SpecComplianceReport` JSON (`schemas/spec_compliance_report.schema.json`)  
**When to use:** After Agent 07W, before Agent 08 (Code Reviewer)

**Validates:**
- API contracts implementation
- Data contracts matching
- Flows implementation
- Edge case handling
- Non-functionals (logging, metrics, etc.)
- Spec-to-code traceability

**Compliance threshold:** Default 80% (configurable)

---

### Agent 08B — Spec Diff Analyzer
**File:** `agents/08b_spec_diff_analyzer.md`  
**Role:** Identifies changes between spec versions and their impact on codebase.  
**Input:** Old `DeveloperReadySpec` JSON, new `DeveloperReadySpec` JSON  
**Output:** `SpecDiffReport` JSON (`schemas/spec_diff_report.schema.json`)  
**When to use:** When spec is updated or changed

**Output includes:**
- Added, removed, modified spec elements
- Affected code locations (using code_references)
- Migration plan for breaking changes
- Recommended actions

---

### Agent 08C — Test Coverage Validator
**File:** `agents/08c_test_coverage_validator.md`  
**Role:** Validates that all spec elements have corresponding tests.  
**Input:** `DeveloperReadySpec` JSON, `TestSuite` JSON, test code (files or `TestCodeSet` JSON)  
**Output:** `TestCoverageReport` JSON (`schemas/test_coverage_report.schema.json`)  
**When to use:** 
- After Agent 07T (Test Writer) to validate all tests were written
- After Agent 07W (Code Writer) to validate final test coverage
- Before code review

**Validates:**
- API contracts coverage
- Data contracts coverage
- Flows coverage
- Edge cases coverage
- Acceptance criteria coverage
- Test quality (completeness, isolation, maintainability)

---

### Agent 09 — Release & Ops
**File:** `agents/09_release_ops.md`  
**Role:** Creates deployment, migration, and rollout runbook.  
**Input:** `DeveloperReadySpec` JSON, environment info (staging/prod), deploy method  
**Output:** Updated `DeveloperReadySpec` JSON with release plan  
**When to use:** When release risk is medium/high

**Output includes:**
- Deployment steps
- Migration procedures
- Feature flag strategy
- Rollback plan
- Monitoring and alerting
- Post-deployment verification

---

### Agent 10 — BE/FE Gap Auditor
**File:** `agents/10_be_fe_gap_auditor.md`  
**Role:** Audits integration gaps between backend APIs and frontend usage (routes, payloads, response shapes, auth, error handling).  
**Input:** `TicketContext` JSON, optional `CodebaseArchitecture` JSON, relevant backend and frontend code  
**Output:** `BeFeGapReport` JSON (`schemas/be_fe_gap_report.schema.json`)  
**When to use:** When BE/FE mismatches or integration issues are suspected or during cross-team alignment.

**Output includes:**
- Gap list with severity and evidence
- Suggested fixes for alignment
- Open questions to resolve

---

## Domain & Specialized Agents

### Agent 01X — Domain Agent Scout
**File:** `agents/01x_domain_agent_scout.md`  
**Role:** Creates domain expert agent scaffolds when domain expertise is needed.  
**Input:** Ticket text, product context, existing domain templates  
**Output:** `DomainScaffold` JSON (`schemas/domain_scaffold.schema.json`)  
**When to use:** When ticket requires domain-specific knowledge (Payroll, LMS, etc.)

**Output includes:**
- Domain expert agent prompt templates
- Example DomainKnowledgePack JSONs
- Domain README documentation
- Orchestrator integration suggestions

**Materialization:** Orchestrator MUST automatically create all files in `materialize.files[]`

---

## Agent Workflows

### Standard Feature Workflow (Rails)
```
Orchestrator → Ticket Reader → Product Analyst → Rails Architect → QA → 
Implementer → Code Writer → Spec Compliance → Test Coverage → Code Reviewer
```

### Bug Fix / Small Refactor - Fast-Track Workflow
```
Orchestrator → Ticket Reader → Architect (light) → QA (regression focus) → 
Implementer → Code Writer → Code Reviewer
```

**Fast-track automatically enabled for:** `commit_type` = `fix`, `refactor`, `style`, `test`, `docs`

### TDD Workflow (Rails)
```
Orchestrator → Ticket Reader → Product Analyst → Rails Architect → QA → 
Test Writer → Test Coverage Validator → Implementer → Code Writer → 
Test Coverage Validator → Spec Compliance → Code Reviewer
```

### Integration Workflow
```
Orchestrator → Ticket Reader → Integration Planner → Architect → QA → 
Test Writer → Test Coverage → Implementer → Code Writer → 
Test Coverage → Code Reviewer
```

### Migration/Extraction Workflow
```
Orchestrator → Ticket Reader → Integration Planner → Data Migration Strategist → 
Modernization Auditor → Architect → QA → Implementer → Code Writer → 
Code Reviewer → Release Ops
```

---

## Schema Reference

All agent outputs validate against schemas in `/schemas/`:

- `ticket_context.schema.json` - Agent 01
- `backlog.schema.json` - Agent 02
- `codebase_architecture.schema.json` - Agent 00A
- `integration_plan.schema.json` - Agent 02A
- `data_migration_plan.schema.json` - Agent 02B
- `spec.schema.json` - Agents 03, 03A, 03B, 03C
- `test_suite.schema.json` - Agent 04
- `test_code_set.schema.json` - Agent 07T
- `code_change_set.schema.json` - Agent 07W
- `spec_compliance_report.schema.json` - Agent 08A
- `spec_diff_report.schema.json` - Agent 08B
- `test_coverage_report.schema.json` - Agent 08C
- `pipeline_plan.schema.json` - Agent 00
- `be_fe_gap_report.schema.json` - Agent 10
- `domain_scaffold.schema.json` - Agent 01X
- `domain_knowledge_pack.schema.json` - Domain experts
- `features.schema.json` - Multi-session tracking
- `bundle.schema.json` - Bundle outputs for triage/test updates

---

## Validation

After each agent, validate output:

```bash
python3 scripts/validate_json_schema.py schemas/<schema>.schema.json <output.json>
```

Or validate entire run folder:

```bash
python3 scripts/validate_run.py runs/<TICKET>_<slug>_<timestamp>
```

---

## See Also

- [README.md](README.md) - Quick start and usage guide
- [docs/how-to-use-in-cursor.md](docs/how-to-use-in-cursor.md) - Detailed Cursor setup
- [docs/command-workflow.md](docs/command-workflow.md) - Command workflow guide
- [docs/sdlc-sequence-diagram.md](docs/sdlc-sequence-diagram.md) - Sequence diagrams
- [.cursor/rules/sdlc_pipeline.md](.cursor/rules/sdlc_pipeline.md) - Team-wide rules

---

Generated: 2026-01-31
