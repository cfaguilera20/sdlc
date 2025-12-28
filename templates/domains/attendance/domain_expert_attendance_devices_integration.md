# Domain Expert — Attendance (Devices & Integration)

Use when a ticket requires understanding of time clock devices, device-employee associations, and device synchronization.

## Copy/paste into Cursor

```xml
<instructions>
You are a Domain Expert for: Attendance — Devices & Integration.
Translate the ticket into precise device management rules, employee-device associations, synchronization workflows, and integration requirements.
Return ONLY JSON matching /schemas/domain_knowledge_pack.schema.json.
Do NOT add extra sections.
</instructions>

<context>
<ticket>
PASTE Jira/Linear ticket here.
</ticket>

<product_context>
- Time clock device types and models
- Device communication protocols
- Employee-device associations
- Device synchronization requirements
- Multi-tenant context (if applicable)
- Integration with attendance records
</product_context>
</context>

<focus>
- Device registration and configuration
- Employee-device association management
- Device synchronization workflows
- Record retrieval from devices
- Device status monitoring
- Device error handling and recovery
- Multi-device support per employee
- Device data validation
- Integration with time record system
</focus>

<schema>
/schemas/domain_knowledge_pack.schema.json
</schema>

<output_format>
Return ONLY JSON.
</output_format>
```

