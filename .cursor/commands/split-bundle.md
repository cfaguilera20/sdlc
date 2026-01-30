# Split One-Message Bundle

This command splits a one-message JSON bundle into run artifacts.

<purpose>
When the orchestrator returns a single JSON bundle, this command splits it into
individual files in the run folder for persistence and validation.
</purpose>

<critical>
- Require the bundle file path and target run folder.
- Instruct user to run `scripts/split_one_message_bundle.py`.
</critical>

<execution_flow>

<phase name="Inputs">
Ask for:
1) Bundle file path (e.g., `runs/.../bundle.json`)
2) Run folder path (e.g., `runs/PROJ-123_slug_YYYYMMDD_HHMMSS`)
</phase>

<phase name="Execute">
Provide the exact command:
`python3 scripts/split_one_message_bundle.py <bundle.json> <run_folder>`
</phase>

</execution_flow>
