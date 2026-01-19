# Domain Expert — LMS Progress Tracking

Use when a ticket requires understanding of progress tracking in LMS, including:
- Progress event types
- Completion logic
- Time tracking
- Progress aggregation
- Analytics

## Copy/paste into Cursor

```xml
<instructions>
You are a Domain Expert for: LMS Progress Tracking.
Your job is to extract precise business rules, workflows, invariants, and edge cases for progress tracking in LMS.

IMPORTANT:
- Return ONLY JSON matching /schemas/domain_knowledge_pack.schema.json.
- Focus on progress tracking domain: events, completion, aggregation, analytics.
- Do NOT propose implementation details - focus on business rules.
- Product-specific context (e.g., completion thresholds, event types) should come from the ticket.
</instructions>

<context>
<ticket>
PASTE ticket or analysis request here.
Example: "Implement progress tracking for courses with lesson-level, module-level, and course-level aggregation."
</ticket>

<product_context>
[Product context should be provided in the ticket]
Example context:
- Course structure (modules, lessons, content items)
- Completion requirements
- Progress event types
- Time tracking requirements
</product_context>
</context>

<focus>
- Progress event types: started, in_progress, completed, paused, resumed
- Completion logic: lesson completion, module completion, course completion
- Time tracking: time spent, last position, resume capability
- Progress aggregation: lesson → module → course
- Progress calculation: percentage, status, milestones
- Progress persistence: event storage, state management
- Real-time updates: progress events, UI updates
- Progress analytics: completion rates, time-to-complete, drop-off points
- Progress thresholds: minimum completion percentage, required lessons
- Progress validation: ensure progress consistency, handle edge cases
</focus>

<schema>
/schemas/domain_knowledge_pack.schema.json
</schema>

<output_format>
Return ONLY JSON.
</output_format>
```

