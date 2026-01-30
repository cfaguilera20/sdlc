# Triage Ticket (Fast)

This command clarifies scope quickly without running the full pipeline.

<purpose>
Run Ticket Reader (and Domain Scout if needed) to clarify scope, risks, and
acceptance criteria before full planning.
</purpose>

<critical>
- Require raw ticket text or a `ticket.txt` file.
- Output a single JSON bundle only.
- Bundle must validate against `schemas/bundle.schema.json`.
</critical>

<execution_flow>

<phase name="Inputs">
Ask for the ticket text or a file reference to `runs/.../ticket.txt`.
</phase>

<phase name="Ticket Reader">
Run Agent 01 to produce `TicketContext`.
</phase>

<phase name="Domain Scout (Optional)">
If domain is ambiguous or specialized, run Agent 01X to produce `DomainScaffold`.
</phase>

<phase name="Output">
Return ONE JSON object:
{
  "ticket_context": { ... },
  "domain_scaffold": { ... } // optional
}
</phase>

</execution_flow>
