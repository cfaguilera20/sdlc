# Create Release Plan

This command generates a release/runbook plan for risky changes.

<purpose>
Run Agent 09 (Release & Ops) to produce deployment steps, rollback strategy,
and verification checklist for medium/high-risk releases.
</purpose>

<critical>
- Require the latest `spec.json`.
- Only use when risk is medium/high or includes migrations/flags.
- Output JSON only (updated spec with release plan).
</critical>

<execution_flow>

<phase name="Inputs">
Ask for the latest `spec.json` and any environment constraints (staging/prod).
</phase>

<phase name="Release Plan">
Run Agent 09 to append a release plan to the spec.
</phase>

<phase name="Output">
Return the updated spec JSON only.
</phase>

</execution_flow>
