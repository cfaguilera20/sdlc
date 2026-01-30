# Create Run Folder

This command creates a new run folder with standard placeholders.

<purpose>
Create a unique run folder for a ticket and ensure required artifacts exist
(ticket.txt, pipeline_plan.json, spec.json, test_suite.json, notes.md, decision.md).
</purpose>

<critical>
- Require `ticket` and `title` inputs.
- Instruct user to run `scripts/new_run.py` from repo root.
- Output only the created run folder path if known.
</critical>

<execution_flow>

<phase name="Inputs">
Ask for:
1) Ticket ID (e.g., PROJ-123)
2) Short title
</phase>

<phase name="Execute">
Provide the exact command:
`python3 scripts/new_run.py --ticket <ID> --title "<short title>"`
</phase>

<phase name="Next Step">
Tell the user to paste the ticket into `runs/.../ticket.txt`.
</phase>

</execution_flow>
