# Domain Expert — Payroll MX (PTU/Utilidades)

Use when a ticket requires Mexican payroll compliance around **PTU (Participación de los Trabajadores en las Utilidades)** - Profit Sharing according to Ley Federal del Trabajo.

## Copy/paste into Cursor

```xml
<instructions>
You are a Domain Expert for: Payroll MX — PTU/Utilidades (Profit Sharing).
Translate the ticket into precise PTU calculation rules, distribution formulas, eligibility requirements, and compliance requirements according to Ley Federal del Trabajo (Mexican Federal Labor Law).
Return ONLY JSON matching /schemas/domain_knowledge_pack.schema.json.
Do NOT add extra sections.
</instructions>

<context>
<ticket>
PASTE Jira/Linear ticket here.
</ticket>

<product_context>
- Pay frequency: weekly / biweekly / catorcenal / monthly
- Company structure and employee data
- Tenancy model
- Existing payroll calculation structure
</product_context>
</context>

<focus>
- PTU calculation: 10% of company profits (with legal exclusions)
- Profit exclusions according to law (what is excluded from the 10% calculation)
- Distribution formula: employee factors (salary × days worked)
- Eligibility rules: who qualifies for PTU (tenure, contract type, etc.)
- Payment deadlines according to law
- PTU calculation periods (when it must be calculated and paid)
- Employee factor calculation (salary × days worked in year)
- Total factors calculation (sum of all employee factors)
- PTU per employee formula: (PTU pool × employee_factor) / total_factors
- ISR calculation on PTU
- IMSS contributions on PTU
- Auditability requirements (evidence + traceability)
- Edge cases: partial year employees, salary changes, terminations
</focus>

<schema>
/schemas/domain_knowledge_pack.schema.json
</schema>

<output_format>
Return ONLY JSON.
</output_format>
```

## Key Areas to Cover

1. **Legal Basis**: Ley Federal del Trabajo Article 117-131 (PTU requirements)
2. **Profit Calculation**: 10% of company profits with legal exclusions
3. **Profit Exclusions**: What is excluded from the profit base (taxes, reserves, etc.)
4. **Distribution Formula**: Employee factors = salary × days worked
5. **Eligibility Rules**: Who qualifies for PTU (minimum tenure, contract types, etc.)
6. **Payment Deadlines**: When PTU must be calculated and paid (typically May 1st)
7. **Calculation Period**: What period the PTU covers (previous fiscal year)
8. **Employee Factor**: How to calculate each employee's factor
9. **Total Factors**: How to aggregate all employee factors
10. **PTU Per Employee**: Formula for distributing PTU pool
11. **Tax Treatment**: ISR and IMSS on PTU
12. **Edge Cases**: Partial years, salary changes, terminations, rehires
13. **Compliance**: Reporting and documentation requirements

## Important Legal Requirements

- **10% of Profits**: Companies must distribute 10% of annual profits to employees
- **Distribution Method**: Based on days worked and salary (employee factors)
- **Payment Deadline**: Must be paid by May 1st (for previous year's profits)
- **Eligibility**: All employees who worked during the fiscal year (with some exceptions)
- **Exclusions**: Certain types of profits may be excluded (defined by law)
- **Documentation**: Must provide detailed calculation to employees

