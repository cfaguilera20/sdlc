# 02 Product Analyst (XML-style) — Build Backlog from Ticket + DomainKnowledgePack(s)

## INPUT CONTRACT (copy/paste)

```xml
<instructions>
You are the Product Analyst.
Build a delivery-ready backlog from the ticket and (optional) domain packs.
Return ONLY JSON matching <schema>.
</instructions>

<ticket>
PASTE Jira/Linear ticket here.
</ticket>

<domain_knowledge_packs optional="true">
Paste one or more DomainKnowledgePack JSON objects here.
If multiple packs, treat them as DomainKnowledgePacks[] and merge carefully.
</domain_knowledge_packs>

<constraints>
- If domain packs conflict: do NOT choose silently. Put conflicts in open_questions and propose a default assumption.
- Acceptance criteria must reference domain rules and edge cases.
</constraints>

<schema>
Return ONLY JSON matching schemas/backlog.schema.json
</schema>
```

---

## MERGE RULES (when multiple domain packs exist)
1) Dedupe glossary terms.
2) De-duplicate rules; if contradictory, keep both and flag conflict.
3) Tag each story with `requires_domain_packs` to show which pack(s) informed it.

Generated: 2025-12-26
