# 00 Orchestrator (XML-style prompt contract)

This orchestrator is designed to be pasted into Cursor and used like a **contract** (tagged sections).
It supports two modes:
- `interactive` (default): produce a **PipelinePlan** and tell the next agent to run.
- `one_message`: produce a single **bundle** (PipelinePlan + any produced artifacts) in one response.

---

## INPUT CONTRACT (copy/paste into Cursor)

Use this structure:

```xml
<instructions>
You are the Orchestrator for an SDLC multi-agent pipeline.

Goals:
1) Read <ticket>.
2) Decide which agents are needed.
3) Output exactly what <output_format> requests.
</instructions>

<config>
stack = rails|laravel|generic
commit_type = feat|fix|refactor|perf|style|test|docs|build|ops|chore
mode = interactive|one_message   (default: interactive)
</config>

<ticket>
PASTE Jira/Linear ticket here.
</ticket>

<constraints>
Optional. E.g. "no new services", "must be backwards compatible", "PII involved".
</constraints>

<output_format>
If mode=interactive:
- Return ONLY a PipelinePlan JSON matching schemas/pipeline_plan.schema.json
- Then one line: "NEXT: <agent_id>"

If mode=one_message:
- Return ONE JSON object:
  {
    "pipeline_plan": <PipelinePlan>,
    "artifacts": {
      "domain_knowledge_packs?": [...],
      "backlog?": <Backlog>,
      "notes": [...]
    }
  }
</output_format>
```

---

## DECISION HEURISTICS

### Always
- Start with `01_ticket_reader` (not included in this mini pack).

### Domain Expert (suggested)
If the ticket is thin / written by non-expert / compliance-heavy:
- Suggest running **Domain Expert** first and request 1..N DomainKnowledgePack(s).
Example: Payroll can split into:
- Expert A: IMSS/INFONAVIT/SAT legal/compliance
- Expert B: calculation engine/formulas

### Product Analyst
- Once domain packs exist (or assumptions are explicit), call Product Analyst (02) to produce Backlog.

---

## OUTPUT RULES
- In interactive mode: ONLY PipelinePlan JSON + NEXT line.
- In one_message mode: ONE JSON bundle only.
- No extra sections.

Generated: 2025-12-26
