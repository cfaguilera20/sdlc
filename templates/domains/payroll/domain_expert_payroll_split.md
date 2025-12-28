# Payroll Domain Experts — Split Template (IMSS/Legal vs Calculations)

Use this when payroll tickets are complex and risk-heavy.

## Expert A — Payroll Legal / Compliance (IMSS/INFONAVIT/SAT/ISN)
Goal: interpret regulations and compliance constraints.

Return: DomainKnowledgePack JSON (domain="Payroll MX - Legal/Compliance")

Focus on:
- compliance requirements, edge cases, effective dates
- employer/employee contributions rules
- risk flags and audit evidence required

## Expert B — Payroll Calculations / Engine
Goal: define calculation logic, formulas, rounding, proration, calendars.

Return: DomainKnowledgePack JSON (domain="Payroll MX - Calculations")

Focus on:
- formulas, inputs/outputs, rounding rules
- pay periods (weekly/biweekly/catorcenal), time zones, DST
- retroactive changes, prorations, caps/floors
- characterization tests vs legacy behavior

## How Product Analyst should use them
- Merge both packs.
- Produce backlog stories:
  - compliance validations (Legal)
  - engine implementation + tests (Calculations)
  - traceability (explainable payroll)
