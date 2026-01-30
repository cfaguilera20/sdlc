# How to Use the SDLC Pipeline in Cursor

This guide shows you **exactly** how to use the orchestrator and agents in Cursor.

## Option 1: Quick Start (Just Paste - No Setup)

**The simplest way** - works immediately:

1. **Open the orchestrator file:**
   - Open `agents/00_orchestrator.md` in Cursor

2. **Copy the entire content** (Cmd+A, Cmd+C / Ctrl+A, Ctrl+C)

3. **Start a new Cursor chat** and paste it, then add your ticket:

```
[Paste entire orchestrator.md content here]

---

stack=rails
commit_type=feat
mode=interactive

TICKET:
[Paste your Jira/Linear ticket here]
```

4. **Cursor will run the orchestrator** and return a `PipelinePlan` JSON

5. **For each agent in the plan:**
   - Open the corresponding `agents/XX_agent_name.md` file
   - Copy its content
   - Paste into a new chat with the previous agent's JSON output

**Pros:** Works immediately, no setup  
**Cons:** You copy/paste agent prompts each time

---

## Option 2: Using Custom Commands (Optional)

If your Cursor version supports Custom Commands, you can create reusable command templates:

1. **Check if Custom Commands are available:**
   - Open Cursor Settings (`Cmd+,` / `Ctrl+,`)
   - Search for "commands" or "custom commands"
   - If available, you can create reusable command templates

2. **Create a Custom Command for the Orchestrator:**
   - Open Settings → Commands (or Custom Commands)
   - Click "Create Command" or "+"
   - **Name:** `SDLC Orchestrator`
   - **Command/Prompt:** Copy the entire content from `agents/00_orchestrator.md`
   - Save the command

3. **Use the command:**
   - In Cursor chat, you may be able to invoke the command
   - Or use it as a template to paste into chat

**Note:** If Custom Commands aren't available in your Cursor version, use **Option 1** (paste directly) instead.

---

## Option 3: Use the Sync Script (Team Standardization)

**For teams that want everyone to have the same setup:**

1. **Run the sync script:**

```bash
make cursor-sync
# or
./scripts/sync_cursor_assets.sh
```

This copies all agents + rules + schemas to `~/.cursor/sdlc/`

2. **Use the synced files:**
   - Copy prompts from `~/.cursor/sdlc/agents/00_orchestrator.md` when needed
   - Everyone on the team has identical prompts in the same location
   - Easy to update by re-running the sync script

**Pros:** Everyone has identical prompts, easy updates  
**Cons:** Still requires copy/paste (since Custom Agents are removed)

---

## Option 4: SDLC One-Step Commands

If you want a one-step flow instead of manual copy/paste, use the SDLC commands:

- `/run-orchestrator` — start the pipeline and return a PipelinePlan JSON
- `/create-sdlc-config` — create `sdlc-config.md` from prompts
- `/update-test-cases` — update acceptance criteria and test cases for a ticket
- `/update-from-main` — safe repo update with backups and conflict guidance
- `/new-run` — create a run folder with placeholders
- `/validate-run` — validate all JSON outputs in a run folder
- `/split-bundle` — split one-message bundle into artifacts
- `/triage-ticket` — clarify scope fast (Ticket Reader / Domain Scout)
- `/update-spec` — update an existing spec after requirement changes
- `/release-plan` — generate release/runbook steps for risky changes
- `/update-mcp` — generate `.cursor/mcp.json` from `.tool-versions`
- `/feature-implementation-methodology` — full feature planning methodology prompt

These commands live in `.cursor/commands/` and can be used directly in Cursor.

---

## How Cursor Rules Work

The `.cursor/rules/sdlc_pipeline.md` file is **automatically loaded** by Cursor if:
- Your repo has a `.cursor/rules/` folder
- Cursor is configured to read rules from the repo

**You don't need to do anything** - Cursor will use these rules to guide behavior.

If rules aren't loading automatically:
- Check Cursor Settings → Rules
- Or manually reference the rules file in your chat: "Follow the rules in `.cursor/rules/sdlc_pipeline.md`"

---

## Complete Workflow Example

### 1. Create Run Folder (Prevents Data Loss)

```bash
make run-init TICKET=PROJ-123 TITLE="Add user authentication"
# Creates: runs/PROJ-123_add-user-authentication_20260115_120000/
```

### 2. Paste Ticket into Run Folder

```bash
# Copy your ticket text into:
runs/PROJ-123_add-user-authentication_20260115_120000/ticket.txt
```

### 3. Run Orchestrator in Cursor

**In Cursor chat (paste the orchestrator prompt + reference the ticket file):**

```
stack=rails
commit_type=feat
mode=interactive

<context>
@runs/PROJ-123_add-user-authentication_20260115_120000/ticket.txt
</context>
```

**Save the output:**
- Copy the `PipelinePlan` JSON
- Save to `runs/.../pipeline_plan.json`

### 4. Run Each Agent from the Plan

**Agent 01 (Ticket Reader):**
- Copy content from `agents/01_ticket_reader.md`
- Paste into new chat + reference the ticket file (avoid pasting chat history)
- Get `TicketContext` JSON
- Save to `runs/.../ticket_context.json`

**Agent 02 (Product Analyst) - if needed:**
- Copy content from `agents/02_product_analyst.md`
- Paste into new chat + reference `runs/.../ticket_context.json`
- Get `Backlog` JSON
- Save to `runs/.../backlog.json`

**Agent 03a (Architect Rails):**
- Copy content from `agents/03a_architect_rails.md`
- Paste into new chat + reference `runs/.../ticket_context.json` (and selected story from `runs/.../backlog.json` if present)
- Get `DeveloperReadySpec` JSON
- Save to `runs/.../spec.json`

**Agent 04 (QA Designer):**
- Copy content from `agents/04_qa_designer.md`
- Paste into new chat + reference `runs/.../spec.json`
- Get `TestSuite` JSON
- Save to `runs/.../test_suite.json`

### 5. Validate Everything

```bash
make validate-run RUN=runs/PROJ-123_add-user-authentication_20260115_120000
```

### 6. (Optional) Implement

**Agent 07a (Implementer Rails):**
- Copy content from `agents/07a_implementer_rails.md`
- Paste into new chat + paste `DeveloperReadySpec` + `TestSuite`
- Get updated spec with `implementation_plan`
- Apply changes in Cursor editor

**Agent 08 (Code Reviewer):**
- Copy content from `agents/08_code_reviewer.md`
- Paste into new chat + paste spec + diff/changed files
- Get review notes

---

## One-Message Mode (Faster, But Riskier)

If you want everything in one response:

```
stack=rails
commit_type=feat
mode=one_message

Run the pipeline end-to-end and return ONE JSON bundle with:
- ticket_context
- backlog (only if needed)
- spec
- test_suite

TICKET:
[Paste ticket]
```

**Then split the bundle:**

```bash
# Save the bundle JSON to a file first, then:
make split-bundle-new-run BUNDLE=runs/.../bundle.json TICKET=PROJ-123 TITLE="Add auth"
```

**Important:** The orchestrator will save files incrementally, but splitting the final bundle ensures everything is in the right place.

---

## Troubleshooting

### "Agent not found" or "Can't find orchestrator"
- **Solution:** Use Option 1 (paste directly) - just copy the content from `agents/00_orchestrator.md` and paste into chat
- The paste method works exactly the same way

### "Can't find Agents in Settings"
- **Solution:** Use Option 1 (paste directly)
- Copy the agent prompt from `agents/00_orchestrator.md` and paste into your Cursor chat

### "Schema validation failed"
- Run: `make validate-run RUN=runs/...`
- Fix the JSON errors shown
- Re-run the agent if needed

### "Rules not working"
- Check that `.cursor/rules/sdlc_pipeline.md` exists
- Cursor should auto-load it, but you can reference it manually in chat

### "Domain materialize files not created"
- After `01x_domain_agent_scout` runs, apply materialize:
  ```bash
  make materialize FILE=runs/.../01x_output.json
  ```

### "File contents showing in chat"
- **This is Cursor's default behavior** - it shows file contents when tools read/write files
- **This is intentional and helpful** - you can see exactly what was written
- You can scroll past or collapse file content sections if needed
- The orchestrator and agents will write files directly to preserve your work incrementally

---

## Next Steps

- See `docs/command-workflow.md` for the command-style workflow (`/prime`, `/plan`, `/execute`, `/commit`)
- See `README.md` for full pipeline documentation
- See `schemas/features.schema.json` for multi-session backlog tracking
