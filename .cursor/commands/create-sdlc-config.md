# Create SDLC Config

This command creates a project-specific SDLC config file for consistent ticket planning.

<purpose>
Create a reusable SDLC configuration file for this repo so all agents have consistent
project context (ticketing system, stakeholders, repos, docs, naming conventions).
This is a one-time setup per project, with occasional updates as team info changes.
</purpose>

<critical>
- Ask questions one at a time; do not assume missing values.
- Load any existing config if present and confirm updates instead of overwriting silently.
- Output a complete, ready-to-save file named `sdlc-config.md` at repo root.
- Keep output strictly to the file contents (no extra prose) so it can be saved directly.
</critical>

<execution_flow>

<phase name="Discovery">
Collect the minimum project metadata needed for consistent planning:
1) Ticket system (Jira/Linear/Other) + project key/board
2) Default stakeholders (PM, Eng Lead, Design)
3) Primary repos (FE/BE/Other)
4) Naming conventions (labels, prefixes)
5) Reference docs (architecture, API, PRD template)
</phase>

<phase name="Draft Config">
Generate `sdlc-config.md` using the template in `templates/sdlc-config.example.md`.
Include only confirmed values; leave bracketed placeholders if unknown.
</phase>

<phase name="Validation">
Confirm the user wants to save it as `sdlc-config.md` in the repo root.
If yes, output the final file content only.
</phase>

</execution_flow>
