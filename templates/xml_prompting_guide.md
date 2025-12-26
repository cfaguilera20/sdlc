# XML-Structured Prompting (Cursor) — Reliability Pack

Use XML-style tags to separate:
- instructions
- context (ticket, repo notes)
- schemas / output format
- examples

This reduces format drift and makes outputs easier to parse.

## Universal tagged wrapper (works for any agent)

```xml
<instructions>
You are running the agent: <AGENT_ID>.
Follow the role and constraints from the agent prompt.
Return ONLY the JSON defined in <schema>.
No extra sections.
</instructions>

<context>
<ticket>
PASTE Jira/Linear ticket here.
</ticket>

<repo_context>
Optional: architecture notes, links, constraints, screenshots summarized.
</repo_context>

<input_artifacts>
Paste any prior agent JSON outputs here (TicketContext, IntegrationPlan, DomainKnowledgePack, etc.)
</input_artifacts>
</context>

<schema>
Paste the relevant schema name and location, e.g.:
- schemas/pipeline_plan.schema.json
- schemas/domain_knowledge_pack.schema.json
- schemas/integration_plan.schema.json
- schemas/data_migration_plan.schema.json
</schema>

<output_format>
Return ONLY valid JSON. No markdown.
</output_format>
```

## Measuring reliability (10-run test)
1) Run the same prompt 10 times.
2) Count format violations (missing keys, extra text, wrong types).
3) Compare blob vs XML-tag wrapper.

Generated: 2025-12-26
