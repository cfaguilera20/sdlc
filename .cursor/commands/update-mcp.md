# Update MCP Config From Tool Versions

This command generates `.cursor/mcp.json` using `.tool-versions`.

<purpose>
Create a concrete `.cursor/mcp.json` by resolving local tool paths (e.g., npx)
from `.tool-versions` and the example template.
</purpose>

<critical>
- Do not modify global `~/.cursor/mcp.json`.
- Run the local script in repo root.
- Output only the generated file path.
</critical>

<execution_flow>

<phase name="Execute">
Provide the exact command:
`python3 scripts/update_mcp_from_tool_versions.py`
</phase>

</execution_flow>
