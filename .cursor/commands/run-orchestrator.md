# Run SDLC Orchestrator (One Step)

This command runs the orchestrator using a ticket and returns a PipelinePlan JSON.

<purpose>
Reduce manual steps by guiding the user through a single orchestrator run:
create a run folder, load the ticket, run Agent 00, and save the PipelinePlan.
This does not run the full pipeline; it starts it correctly and consistently.
</purpose>

<critical>
- Require `stack` and `commit_type`. If missing, ask before proceeding.
- If no run folder exists, instruct the user to create one with `scripts/new_run.py`.
- Output ONLY the PipelinePlan JSON (no prose) once inputs are ready.
</critical>

<execution_flow>

<phase name="Setup">
1) Ask for `stack` (rails/laravel/other) and `commit_type` if not provided.
2) Ask for ticket text or a file reference to `runs/.../ticket.txt`.
3) If run folder missing, instruct to create it and paste ticket there.
</phase>

<phase name="Orchestrate">
Run the orchestrator prompt (Agent 00) using the provided ticket and inputs.
</phase>

<phase name="Output">
Return ONLY the PipelinePlan JSON so it can be saved to `runs/.../pipeline_plan.json`.
</phase>

</execution_flow>
