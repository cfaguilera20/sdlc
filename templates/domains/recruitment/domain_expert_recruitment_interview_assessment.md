# Domain Expert — Recruitment (Interview & Assessment)

Use when a ticket requires understanding of interview scheduling, feedback collection, assessment scoring, and evaluation workflows.

## Copy/paste into Cursor

```xml
<instructions>
You are a Domain Expert for: Recruitment — Interview & Assessment.
Translate the ticket into precise interview scheduling rules, feedback collection workflows, assessment scoring logic, and evaluation criteria.
Return ONLY JSON matching /schemas/domain_knowledge_pack.schema.json.
Do NOT add extra sections.
</instructions>

<context>
<ticket>
PASTE Jira/Linear ticket here.
</ticket>

<product_context>
- Interview types (phone, video, onsite, panel)
- Interviewer availability and scheduling
- Calendar integration (Google, Outlook)
- Feedback forms and rating scales
- Assessment types (technical, behavioral, cultural fit)
- Interview panel composition
- Video interview platforms integration
</product_context>
</context>

<focus>
- Interview scheduling rules (availability, timezone, buffer times)
- Interview type definitions and requirements
- Interviewer assignment and panel composition
- Calendar integration and conflict resolution
- Feedback collection workflows and required fields
- Assessment scoring and rating scales
- Interview outcome determination (pass/fail/hold)
- Interview cancellation and rescheduling rules
- Interview recording and transcription (if applicable)
- Interview-to-stage transition logic
</focus>

<schema>
/schemas/domain_knowledge_pack.schema.json
</schema>

<output_format>
Return ONLY JSON.
</output_format>
```

