# Update Spec (Focused)

This command updates an existing DeveloperReadySpec after requirement changes.

<purpose>
Modify `spec.json` to reflect new/changed requirements without re-running
the full pipeline. Keeps scope tight and changes traceable.
</purpose>

<critical>
- Require existing `spec.json` and the updated ticket context.
- Do not add new scope beyond updated requirements.
- Output only the updated `spec.json` (JSON only).
</critical>

<execution_flow>

<phase name="Inputs">
Ask for:
1) Updated ticket text or `ticket_context.json`
2) Existing `spec.json`
</phase>

<phase name="Update">
Revise spec sections impacted by the change (flows, contracts, edge cases,
non-functionals, implementation plan if present).
</phase>

<phase name="Output">
Return updated `spec.json` only.
</phase>

</execution_flow>
