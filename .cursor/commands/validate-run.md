# Validate Run Artifacts

This command validates all JSON outputs in a run folder.

<purpose>
Run schema validation across a run folder and summarize any failures.
This provides a quick quality gate before proceeding.
</purpose>

<critical>
- Require a run folder path under `runs/`.
- Instruct user to run `scripts/validate_run.py`.
- If validation fails, ask for the error output.
</critical>

<execution_flow>

<phase name="Inputs">
Ask for the run folder path (e.g., `runs/PROJ-123_slug_YYYYMMDD_HHMMSS`).
</phase>

<phase name="Execute">
Provide the exact command:
`python3 scripts/validate_run.py <RUN_FOLDER>`
</phase>

<phase name="Report">
If errors occur, ask the user to paste the output for help.
</phase>

</execution_flow>
