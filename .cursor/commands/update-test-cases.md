# Update Test Cases and Acceptance Criteria

This command updates acceptance criteria and test cases for an existing ticket.

<purpose>
Given a ticket and current artifacts, update acceptance criteria and test cases
without re-running the full pipeline. This is used when requirements changed or
gaps were found during review.
</purpose>

<critical>
- Do not change scope beyond the ticket's intent.
- Require the latest `ticket_context.json` or raw ticket text.
- If a `spec.json` exists, align changes to it; otherwise, update AC and tests only.
- Output a single JSON bundle only.
- Bundle must validate against `schemas/bundle.schema.json`.
</critical>

<execution_flow>

<phase name="Inputs">
Ask for:
1) Ticket text or `runs/.../ticket_context.json`
2) Existing `runs/.../spec.json` (optional but preferred)
3) Existing `runs/.../test_suite.json` (if updating tests)
</phase>

<phase name="Update Acceptance Criteria">
If `ticket_context.json` is provided, update `acceptance_criteria` in-place and
return an updated TicketContext JSON.
</phase>

<phase name="Update Test Cases">
If `spec.json` and `test_suite.json` are provided, update the TestSuite to align
with the revised acceptance criteria and spec. Add or adjust tests; do not remove
coverage unless the requirement was explicitly removed.
</phase>

<phase name="Output">
Return ONE JSON object:
{
  "ticket_context": { ... }, // optional
  "test_suite": { ... }      // optional
}
</phase>

</execution_flow>
