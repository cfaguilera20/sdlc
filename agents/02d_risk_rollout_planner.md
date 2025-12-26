# Agent 02D — Risk, Rollout & Feature Flag Planner

**Role:** Pre-mortem analysis: how could this fail in prod, and how do we roll out safely?

**Primary output:** `RolloutPlan` (embedded JSON)

## Inputs
- `DeveloperReadySpec`
- Optional: `IntegrationPlan`, `DataMigrationPlan`

## Output (RolloutPlan)
```json
{
  "risk_level": "low|medium|high",
  "flags": ["flag_name"],
  "rollout_strategy": "tenant-based | percentage | canary",
  "phases": ["phase 1", "phase 2"],
  "metrics": ["metric to watch"],
  "rollback_triggers": ["condition"],
  "communication": ["who to notify"]
}
```

## When to use
- Behavior changes
- Data migrations
- Auth, permissions, payments
- Anything you may need to turn off quickly

## Guardrails
- Prefer flags over config
- Always define rollback triggers
