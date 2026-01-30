# Update From Main (Safe)

This command runs the safe update script for the SDLC repo.

<purpose>
Update local branches from `main` safely with backups and conflict guidance.
This reduces accidental data loss during repo updates.
</purpose>

<critical>
- Do not run any git commands until the user confirms.
- Instruct the user to run `scripts/update-from-main.sh` from repo root.
- If conflicts occur, instruct the user to paste the error output.
</critical>

<execution_flow>

<phase name="Confirm">
Ask the user to confirm they want to update from `main`.
</phase>

<phase name="Execute">
Provide the exact command:
`./scripts/update-from-main.sh`
</phase>

<phase name="Handle Issues">
If conflicts occur, ask for the output and offer guidance.
</phase>

</execution_flow>
