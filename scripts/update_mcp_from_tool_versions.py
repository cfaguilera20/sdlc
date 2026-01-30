#!/usr/bin/env python3
"""
Update .cursor/mcp.json based on tools in .tool-versions.

- Uses .cursor/mcp.example.json as a base template.
- Resolves command paths for local MCP servers (e.g., npx) using asdf when available.
"""
import argparse
import json
import shutil
import subprocess
from pathlib import Path
from typing import Optional


def read_tool_versions(path: Path) -> dict:
    tools = {}
    if not path.exists():
        return tools
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            tools[parts[0]] = parts[1]
    return tools


def asdf_where(tool: str) -> Optional[str]:
    try:
        result = subprocess.run(
            ["asdf", "where", tool],
            check=True,
            capture_output=True,
            text=True,
        )
        path = result.stdout.strip()
        return path if path else None
    except Exception:
        return None


def resolve_command(cmd: str) -> str:
    # Try asdf for nodejs tools (npx/node)
    if cmd in {"npx", "node"}:
        asdf_path = asdf_where("nodejs")
        if asdf_path:
            candidate = Path(asdf_path) / "bin" / cmd
            if candidate.exists():
                return str(candidate)
    # Fallback to PATH
    which = shutil.which(cmd)
    return which if which else cmd


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", default=".cursor/mcp.example.json")
    ap.add_argument("--out", default=".cursor/mcp.json")
    ap.add_argument("--tool-versions", default=".tool-versions")
    args = ap.parse_args()

    template_path = Path(args.template)
    out_path = Path(args.out)
    tool_versions = read_tool_versions(Path(args.tool_versions))

    if not template_path.exists():
        print(f"Missing template: {template_path}")
        return 1

    data = json.loads(template_path.read_text(encoding="utf-8"))
    servers = data.get("mcpServers", {})

    # If nodejs is declared, resolve npx to a concrete path (optional).
    if "nodejs" in tool_versions:
        for name, server in servers.items():
            cmd = server.get("command")
            if isinstance(cmd, str):
                server["command"] = resolve_command(cmd)
                servers[name] = server

    out_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
