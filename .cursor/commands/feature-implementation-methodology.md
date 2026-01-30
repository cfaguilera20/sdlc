# Feature Implementation Methodology (SDLC‑Aligned)

Use this command when you want a single prompt that guides a full feature workflow
without duplicating SDLC agents. It is concise, consistent, and avoids repetition.

<purpose>
Provide a structured, phase‑based methodology that aligns with the SDLC agent
pipeline (00 → 09) while remaining usable as a single prompt. It replaces the
old monolithic prompt with a clearer, DRY version.
</purpose>

<critical>
- Be consistent with SDLC terminology (TicketContext, Backlog, Spec, TestSuite).
- Prefer reusing SDLC agents rather than re‑stating their full checklists.
- Avoid duplicating content across phases; reference earlier decisions instead.
- Ask for the ticket first; do not start without it.
- Keep outputs actionable and scoped to the ticket.
</critical>

<execution_flow>

<phase name="0) Inputs & Classification">
Ask for:
1) Ticket text (or `runs/.../ticket.txt`)
2) `stack` (rails/laravel/other)
3) `commit_type` (feat/fix/refactor/perf/style/test/docs/chore/ci/build)

Classify complexity:
- **Simple:** small fix/refactor → fast‑track
- **Medium:** single story with limited surface area
- **Complex:** multi‑story, integrations, migrations, or security‑sensitive
</phase>

<phase name="1) Discovery & Scope (Agent 01)">
Run Ticket Reader to produce `TicketContext`:
- Clarify scope, risks, constraints
- Extract acceptance criteria
- Identify unknowns/assumptions to resolve
</phase>

<phase name="2) Planning (Agent 02 / optional)">
If scope > 1 story or ambiguous:
- Run Product Analyst to produce `Backlog`
Otherwise skip and continue.
</phase>

<phase name="3) Architecture & Spec (Agent 03A/03B/03C)">
Create a `DeveloperReadySpec`:
- Contracts, flows, data model, edge cases
- Implementation plan at file level (lightweight if fast‑track)
</phase>

<phase name="4) QA & Tests (Agent 04, optional 07T)">
Generate `TestSuite` aligned to acceptance criteria and spec.
If TDD requested, run Test Writer (07T) before implementation.
</phase>

<phase name="5) Implementation (Agent 07A/07B/07C → 07W)">
Use Implementer to plan, then Code Writer to apply changes.
Keep changes scoped to the spec; update spec if scope changes.
</phase>

<phase name="6) Validation & Review (Agent 08A/08C/08)">
Validate spec compliance, test coverage, and code review.
Capture findings; do not proceed if schemas fail validation.
</phase>

<phase name="7) Release (Agent 09, conditional)">
If risk is medium/high or includes migrations:
- Generate release/runbook plan
</phase>

</execution_flow>

<output_format>
Return a short, phase‑by‑phase checklist tailored to the ticket, indicating which
agents to run and which artifacts to produce (JSON only when schema is required).
</output_format>
