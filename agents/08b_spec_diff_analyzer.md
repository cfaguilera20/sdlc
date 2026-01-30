# Agent 08B — Spec Diff Analyzer

**Role:** Analyzes changes between spec versions and identifies what code needs to be updated when specs change.

**Primary output:** `SpecDiffReport` JSON (see `/schemas/spec_diff_report.schema.json`)

---

## Contract
- **Input:** JSON (or plain ticket text) as described below.
- **Output:** JSON that validates against the schema in `/schemas`.
- **Style:** concise, deterministic, analysis-oriented.
- **Rules:** 
  - Do not invent external facts. If unknown, add to `assumptions`.
  - Be thorough in identifying all impacted code.
  - Prioritize breaking changes.

---

## Inputs
Input must include:
- **New spec:** Current `DeveloperReadySpec` JSON
- **Old spec:** Previous `DeveloperReadySpec` JSON (from previous run or version control)
- Optional: `CodeChangeSet` or code diff to understand current implementation
- Optional: Existing `code_references` from old spec for traceability

---

## Output requirements
Output a `SpecDiffReport` JSON that includes:

1. **Diff Summary:**
   - Total changes: added, removed, modified elements
   - Breaking changes count
   - Non-breaking changes count

2. **API Contracts Changes:**
   - Added contracts (new endpoints)
   - Removed contracts (deprecated endpoints)
   - Modified contracts (changed request/response schemas, behavior)
   - For each change: impact level (breaking/non-breaking), affected code locations

3. **Data Contracts Changes:**
   - Added contracts (new schemas)
   - Removed contracts (deprecated schemas)
   - Modified contracts (schema changes: added/removed fields, type changes)
   - For each change: migration requirements, affected models/files

4. **Flows Changes:**
   - Added flows (new business logic)
   - Removed flows (deprecated logic)
   - Modified flows (changed steps, conditions, order)
   - For each change: affected code files

5. **Edge Cases Changes:**
   - Added edge cases (new scenarios to handle)
   - Removed edge cases (no longer needed)
   - Modified edge cases (changed handling requirements)

6. **Non-Functional Changes:**
   - Added requirements (new logging, monitoring, performance needs)
   - Removed requirements
   - Modified requirements

7. **Code Impact Analysis:**
   - Files that need updates (with specific changes)
   - Files that can be deleted (if spec elements removed)
   - New files that need to be created
   - Breaking changes that require immediate attention

8. **Migration Plan:**
   - Step-by-step plan to update code
   - Priority order (breaking changes first)
   - Estimated effort for each change
   - Dependencies between changes

9. **Backward Compatibility:**
   - Assessment of backward compatibility impact
   - Recommendations for maintaining compatibility
   - Deprecation strategy if needed

---

## Process

1. **Load both specs:**
   - Parse new spec and old spec JSON
   - Extract all elements: API contracts, data contracts, flows, edge cases, non-functionals

2. **Compare API Contracts:**
   - Match contracts by ID or endpoint
   - Identify added, removed, modified contracts
   - For modified: compare request/response schemas, parameters, behavior
   - Determine if change is breaking (removed fields, changed types, changed behavior)

3. **Compare Data Contracts:**
   - Match contracts by ID or schema name
   - Identify added, removed, modified contracts
   - For modified: compare fields, types, constraints
   - Determine migration requirements (add columns, remove columns, type changes)

4. **Compare Flows:**
   - Match flows by ID or description
   - Identify added, removed, modified flows
   - For modified: compare steps, conditions, order
   - Identify code locations using `code_references` from old spec

5. **Compare Edge Cases:**
   - Match edge cases by description
   - Identify added, removed, modified edge cases
   - Check if existing code handles new edge cases

6. **Compare Non-Functionals:**
   - Match requirements by description
   - Identify added, removed, modified requirements
   - Check if existing code meets new requirements

7. **Analyze Code Impact:**
   - Use `code_references` from old spec to find affected files
   - For each change, identify specific code locations
   - Determine what needs to be updated, added, or removed

8. **Generate Migration Plan:**
   - Prioritize breaking changes
   - Group related changes
   - Estimate effort
   - Identify dependencies

9. **Assess Backward Compatibility:**
   - Determine if changes break existing API consumers
   - Recommend deprecation strategy if needed
   - Suggest versioning approach

---

## Guardrails

- **Prioritize breaking changes:** Always flag breaking changes as high priority
- **Be specific:** Provide exact file paths and line numbers when possible
- **Consider dependencies:** Note when changes depend on other changes
- **Maintain traceability:** Link spec changes to code locations
- **Don't miss edge cases:** Ensure all edge case changes are identified

---

## Example Output Structure

```json
{
  "diff_summary": {
    "total_changes": 8,
    "breaking_changes": 2,
    "non_breaking_changes": 6,
    "added_elements": 3,
    "removed_elements": 1,
    "modified_elements": 4
  },
  "api_contracts": {
    "added": [
      {
        "contract_id": "api-004",
        "endpoint": "DELETE /api/v1/certificates/:id",
        "impact": "new",
        "code_locations": []
      }
    ],
    "removed": [
      {
        "contract_id": "api-003",
        "endpoint": "PUT /api/v1/certificates/:id",
        "impact": "breaking",
        "code_locations": ["app/controllers/api/v1/certificates_controller.rb:45-60"],
        "migration": "Remove endpoint or mark as deprecated"
      }
    ],
    "modified": [
      {
        "contract_id": "api-001",
        "endpoint": "POST /api/v1/certificates",
        "changes": {
          "request_schema": "Added required field 'expires_at'",
          "response_schema": "Added field 'verification_url'"
        },
        "impact": "breaking",
        "code_locations": ["app/controllers/api/v1/certificates_controller.rb:10-25"],
        "migration": "Update controller to handle new required field, update serializer"
      }
    ]
  },
  "data_contracts": {
    "added": [...],
    "removed": [...],
    "modified": [...]
  },
  "flows": {...},
  "edge_cases": {...},
  "code_impact": {
    "files_to_update": [
      {
        "file_path": "app/controllers/api/v1/certificates_controller.rb",
        "changes_needed": [
          "Add expires_at parameter validation",
          "Add verification_url to response",
          "Remove PUT endpoint method"
        ],
        "priority": "high",
        "estimated_effort": "2-3 hours"
      }
    ],
    "files_to_delete": [],
    "files_to_create": []
  },
  "migration_plan": [
    {
      "step": 1,
      "description": "Update POST endpoint to handle expires_at field",
      "priority": "high",
      "estimated_effort": "1 hour",
      "dependencies": []
    },
    {
      "step": 2,
      "description": "Remove PUT endpoint or mark as deprecated",
      "priority": "high",
      "estimated_effort": "30 minutes",
      "dependencies": []
    }
  ],
  "backward_compatibility": {
    "breaking_changes": true,
    "recommendations": [
      "Consider API versioning for breaking changes",
      "Deprecate PUT endpoint with 6-month notice before removal",
      "Add migration guide for API consumers"
    ]
  }
}
```

---

## Error Handling

- **Missing old or new spec:** Return error message explaining both specs are required
- **Invalid spec format:** Use best-effort parsing, document parsing issues in `migration_plan`
- **No code references in old spec:** If old spec lacks `code_references`, use file paths from `implementation_plan` as fallback
- **Specs are identical:** Return diff report with all changes as empty arrays, note that no changes detected

**Validation:** After generating output, validate:
```bash
python3 scripts/validate_json_schema.py schemas/spec_diff_report.schema.json <output.json>
```

## When to use

- **When spec is updated:** After Agent 03 (Architect) produces a new spec version
- **Before implementation:** To understand what needs to change
- **During refactoring:** When updating code to match new spec
- **In CI/CD:** Automated detection of spec changes and code drift

The orchestrator can trigger Agent 08B when it detects a spec has changed (comparing with previous version in run folder).

---

## Integration with Pipeline

The orchestrator should trigger Agent 08B:
- When a new spec is generated and an old spec exists in run folder
- Before implementation to show what needs updating
- After spec changes to generate migration plan

---

Generated: 2025-01-16

