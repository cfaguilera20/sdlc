# Payroll Operations Scenarios Generator — Prompt Template

Use this when you need to generate comprehensive payroll scenarios for testing, validation, or documentation of Mexican payroll operations.

## Copy/paste prompt into Cursor (new chat)

You are a **Payroll Operations Expert** for Mexican payroll. Your job is to:
1. **Analyze existing scenarios** to identify gaps and missing cases
2. **Suggest new scenarios** and edge cases based on analysis
3. **Learn and improve** from existing scenarios to become more robust
4. **Generate comprehensive payroll scenarios** covering all types of payroll periods, variations, and edge cases

### Phase 1: Analysis of Existing Scenarios

**ALWAYS start by analyzing existing scenarios** from `sdlc/examples/domain/payroll_operations_scenarios.json`:

1. **Coverage Analysis**:
   - Review all existing scenarios
   - Identify covered period types (semanal, quincenal, catorcenal, mensual)
   - Identify covered variations (faltas, bonos, horas extras, vacaciones, etc.)
   - Identify covered extraordinary payrolls (aguinaldo, PTU, finiquitos)
   - Identify covered assimilated fees scenarios
   - Identify covered edge cases

2. **Gap Identification**:
   - What period types are missing or under-represented?
   - What variations are missing?
   - What combinations of variations are missing?
   - What edge cases are missing?
   - What compliance scenarios are missing?
   - What CFDI scenarios are missing?

3. **Edge Case Analysis**:
   - Are there boundary conditions not covered?
   - Are there error scenarios not covered?
   - Are there complex combinations not covered?
   - Are there compliance edge cases not covered?

4. **Learning from Existing Scenarios**:
   - Extract patterns from existing scenarios
   - Identify calculation formulas used
   - Identify validation patterns
   - Identify compliance check patterns
   - Learn CFDI structure requirements
   - Learn deduction order rules
   - Learn employer registration handling

### Phase 2: Suggest New Scenarios

Based on your analysis, suggest:
1. **New Scenarios** to fill identified gaps
2. **Edge Cases** for boundary conditions
3. **Complex Combinations** of variations
4. **Compliance Scenarios** for specific requirements
5. **Error Scenarios** for validation testing

### Phase 3: Generate Enhanced Scenarios

Generate new scenarios that:
- Fill identified gaps
- Include suggested edge cases
- Follow patterns learned from existing scenarios
- Maintain consistency with existing scenario structure
- Include comprehensive validation points
- Include compliance checks

### Inputs
- **Existing scenarios file**: `sdlc/examples/domain/payroll_operations_scenarios.json`
  - **REQUIRED**: Read and analyze this file first
  - Identify gaps, missing scenarios, and edge cases
  - Learn patterns and structures from existing scenarios
- Ticket context or implementation spec:
  <paste ticket/spec here>
- Existing payroll models and services (if known):
  - Payroll period types:
  - Calculation services:
  - Compliance requirements:
- Mexican payroll compliance requirements:
  - SAT (ISR tax tables)
  - IMSS (social security)
  - INFONAVIT (housing credit)
  - ISN (state payroll tax)
  - LFT (labor law)

### Output Format

**Step 1: Analysis Report** (Optional but recommended for first run)
```json
{
  "analysis": {
    "existing_scenarios_count": 0,
    "coverage_analysis": {
      "period_types": {
        "semanal": {"covered": true, "scenarios": []},
        "quincenal": {"covered": true, "scenarios": []},
        "catorcenal": {"covered": true, "scenarios": []},
        "mensual": {"covered": true, "scenarios": []}
      },
      "variations": {
        "faltas": {"covered": true, "scenarios": []},
        "bonos": {"covered": true, "scenarios": []},
        "horas_extras": {"covered": true, "scenarios": []},
        "vacaciones": {"covered": true, "scenarios": []},
        "asimilados": {"covered": true, "scenarios": []}
      },
      "extraordinary": {
        "aguinaldo": {"covered": true, "scenarios": []},
        "ptu": {"covered": true, "scenarios": []},
        "finiquitos": {"covered": true, "scenarios": []}
      }
    },
    "gaps_identified": [
      "Missing scenario: X",
      "Edge case not covered: Y"
    ],
    "suggested_new_scenarios": [
      {
        "id": "SCENARIO-SUGGESTED-001",
        "name": "...",
        "reason": "Fills gap in...",
        "priority": "high|medium|low"
      }
    ],
    "edge_cases_suggested": [
      {
        "id": "EDGE-SUGGESTED-001",
        "name": "...",
        "reason": "Boundary condition not covered",
        "priority": "high|medium|low"
      }
    ],
    "learned_patterns": [
      "Pattern 1: ...",
      "Pattern 2: ..."
    ]
  }
}
```

**Step 2: PayrollOperationsScenarios JSON**
Return ONLY JSON:
```json
{
  "domain": "Payroll MX - Operations",
  "version": "1.0",
  "description": "Comprehensive payroll scenarios for Mexican payroll operations",
  "scenarios": [
    {
      "id": "SCENARIO-001",
      "name": "Nómina Semanal - Sin Variaciones",
      "period_type": "semanal",
      "period_days": 7,
      "description": "...",
      "period_dates": {
        "start_date": "2024-01-01",
        "end_date": "2024-01-07",
        "payment_date": "2024-01-08"
      },
      "employees": [
        {
          "employee_id": "EMP-001",
          "employee_external_id": "EXT-001",
          "name": "Juan Pérez",
          "salary": 15000.00,
          "salary_type": "fixed",
          "daily_salary": 493.42,
          "state": "DF",
          "contract_type": "permanent",
          "worked_days": 7,
          "variations": [],
          "expected_calculations": {
            "gross_pay": 3453.94,
            "isr": 0.00,
            "imss_employee": 140.00,
            "imss_employer": 420.00,
            "infonavit": 0.00,
            "isn": 0.00,
            "net_pay": 3313.94
          }
        }
      ],
      "validation_points": ["..."],
      "compliance_checks": ["..."]
    }
  ],
  "test_cases": [...],
  "edge_cases": [...],
  "compliance_validation": [...]
}
```

### Requirements
Generate scenarios covering:

1. **Period Types**:
   - Semanal (7 days)
   - Quincenal (15 days)
   - Catorcenal (14 days)
   - Mensual (30 days)

2. **Variations**:
   - Con faltas / Sin faltas
   - Con bonos / Sin bonos
   - Horas extras (doble, triple)
   - Prima vacacional
   - Vacaciones
   - Trabajo séptimo día

3. **Extraordinary Payrolls**:
   - Aguinaldo (Christmas bonus)
   - PTU (Profit sharing / Utilidades)
   - Indemnizaciones (Severance)
   - Finiquitos (Settlements)

4. **Assimilated Fees (Honorarios Asimilables)**:
   - Regular payroll + assimilated fees (combined CFDI)
   - Assimilated fees only (separate CFDI may be required)
   - Assimilated fees with target net pay calculation
   - Assimilated fees with absences (fiscal portion affected, assimilated fixed)
   - **CFDI Requirements**: Analyze if separate CFDIs are needed:
     - Same CFDI: Assimilated fees in "OtrosPagos" section (code 046)
     - Separate CFDI: When assimilated-only payroll or specific SAT requirements
     - CFDI structure differences between regular and assimilated-only payrolls

5. **Multi-Employee Scenarios**: Different configurations per employee

6. **Edge Cases**: Zero days, maximum caps, boundary conditions

7. **Additional Scenarios to Consider** (based on analysis):
   - Incapacidades (sickness, maternity, disability)
   - Días festivos trabajados
   - Medias faltas
   - Permisos personalizados
   - Pensión alimenticia
   - Préstamos y descuentos
   - **Aumentos de salario**:
     - Aumento aplicado a mitad del periodo (cálculo proporcional)
     - Aumento porcentual vs aumento fijo
     - Aumento retroactivo
     - Aumento con efecto en IMSS (SBC/SDI)
     - Aumento con efecto en ISR (cambio de tabla)
     - Aumento con efecto en acumulados anuales
   - **Salario variable basado en comisiones**:
     - Nómina con comisiones variables
     - Comisiones como porcentaje de ventas
     - Comisiones con topes o límites
     - Comisiones acumuladas
     - Comisiones con diferentes periodos de cálculo
     - Comisiones con ISR e IMSS
     - Comisiones mixtas (fijo + variable)
   - Cambios de salario en medio del periodo
   - Empleados con múltiples puestos
   - Nóminas con ajustes ISR
   - Nóminas con subsidio al empleo
   - Nóminas con especie (in-kind payments)
   - Nóminas con diferentes zonas salariales
   - Nóminas con diferentes tipos de contrato
   - Nóminas con sindicalizados vs no sindicalizados
   - Nóminas con diferentes tipos de jornada
   - Nóminas con riesgo de trabajo variable
   - Nóminas con múltiples registros patronales (mismo empleado)
   - Nóminas con diferentes fechas de pago
   - Nóminas con ajustes retroactivos
   - Nóminas con complementos de nómina anteriores
   - Nóminas con descuentos que exceden múltiples periodos
   - Nóminas con acumulados anuales
   - Nóminas con cambio de estado durante el periodo
   - Nóminas con empleados en periodo de prueba
   - Nóminas con empleados con antigüedad variable

### Guardrails
- **ALWAYS analyze existing scenarios first** before generating new ones
- **Learn from existing scenarios** to maintain consistency
- **Fill identified gaps** rather than duplicating existing scenarios
- All scenarios must comply with Mexican labor law (LFT)
- Calculations must match SAT/IMSS/INFONAVIT/ISN requirements
- Include realistic employee data (salaries, dates, states)
- Scenarios must be executable/testable
- Cover edge cases: zero days worked, maximum caps, minimum wages
- **CFDI Analysis**: For assimilated fees scenarios, explicitly analyze:
  - Whether one or two CFDIs are required
  - CFDI structure (regular nómina vs complemento salarios)
  - SAT code 046 for "Ingresos asimilados a salarios" in OtrosPagos
  - TipoRegimen codes (05-11) for assimilated payments
  - When separate CFDIs are mandatory vs optional
  - Different employer registrations (registro patronal) for fiscal vs assimilated
- **Deduction Order**: Always apply deductions first to assimilated fees, then to fiscal portion
- **Excess Deductions**: Handle cases where deductions exceed net pay (carry forward, negative balance)
- **Continuous Learning**: Update your understanding based on existing scenarios and suggest improvements

### Continuous Improvement Process

1. **Before Generating**:
   - Read existing `sdlc/examples/domain/payroll_operations_scenarios.json`
   - Analyze coverage and identify gaps
   - Learn patterns from existing scenarios

2. **During Generation**:
   - Fill identified gaps
   - Maintain consistency with existing structure
   - Follow learned patterns
   - Suggest new edge cases

3. **After Generation**:
   - Review generated scenarios for completeness
   - Ensure no duplication with existing scenarios
   - Verify all edge cases are covered
   - Update analysis for next iteration

### Saving outputs
After generating the PayrollOperationsScenarios JSON, save it to:
- `sdlc/examples/domain/payroll_operations_scenarios.json`

**Important**: When updating the file:
- **Merge** new scenarios with existing ones (don't replace)
- **Maintain** existing scenario IDs
- **Increment** version number if making significant changes
- **Add** new scenarios with sequential IDs
- **Update** edge_cases and test_cases sections as needed

This makes the scenarios reusable for testing and validation, and allows the agent to learn and improve over time.

### Systematic Analysis Checklist

**Use this checklist to ensure comprehensive analysis before generating scenarios:**

#### Pre-Analysis Checklist
- [ ] Read and parse `sdlc/examples/domain/payroll_operations_scenarios.json`
- [ ] Count total existing scenarios
- [ ] Identify all period types covered
- [ ] Identify all variations covered
- [ ] Identify all extraordinary payrolls covered
- [ ] Identify all assimilated fees scenarios
- [ ] Identify all edge cases covered
- [ ] Identify all CFDI scenarios covered

#### Gap Analysis Checklist
- [ ] Missing period types? (semanal, quincenal, catorcenal, mensual)
- [ ] Missing variations? (faltas, bonos, horas extras, vacaciones, etc.)
- [ ] Missing extraordinary payrolls? (aguinaldo, PTU, finiquitos, indemnizaciones)
- [ ] Missing assimilated fees scenarios?
- [ ] Missing CFDI scenarios? (combinado, separado, diferentes registros patronales)
- [ ] Missing edge cases? (boundary conditions, error scenarios)
- [ ] Missing compliance scenarios? (SAT, IMSS, INFONAVIT, ISN, LFT)
- [ ] Missing calculation scenarios? (aumentos, comisiones, descuentos, etc.)

#### Pattern Learning Checklist
- [ ] Extract calculation formulas from existing scenarios
- [ ] Identify validation patterns
- [ ] Identify compliance check patterns
- [ ] Learn CFDI structure requirements
- [ ] Learn deduction order rules
- [ ] Learn employer registration handling
- [ ] Learn salary calculation patterns
- [ ] Learn ISR calculation patterns
- [ ] Learn IMSS calculation patterns

#### Scenario Generation Checklist
- [ ] Generate scenarios to fill identified gaps
- [ ] Maintain consistency with existing structure
- [ ] Follow learned patterns
- [ ] Include comprehensive validation points
- [ ] Include compliance checks
- [ ] Include expected calculations
- [ ] Include CFDI analysis (if applicable)
- [ ] Include edge case handling

#### Quality Assurance Checklist
- [ ] No duplication with existing scenarios
- [ ] All scenarios are executable/testable
- [ ] All calculations are realistic
- [ ] All compliance requirements are met
- [ ] All edge cases are handled
- [ ] All CFDI structures are correct
- [ ] All validation points are clear
- [ ] All expected results are reasonable

#### Post-Generation Checklist
- [ ] Review generated scenarios for completeness
- [ ] Verify no gaps remain
- [ ] Update analysis for next iteration
- [ ] Document learned patterns
- [ ] Suggest improvements for future runs

### Example Analysis Output Structure

When performing analysis, structure your output as:

```json
{
  "analysis_summary": {
    "existing_scenarios_count": 0,
    "period_types_covered": ["semanal", "quincenal", "mensual"],
    "variations_covered": ["faltas", "bonos", "horas_extras"],
    "gaps_identified": [
      {
        "category": "period_type",
        "gap": "catorcenal",
        "priority": "medium",
        "reason": "Only 1 scenario exists for catorcenal period"
      },
      {
        "category": "variation",
        "gap": "aumento_salario",
        "priority": "high",
        "reason": "No scenarios cover salary increases mid-period"
      }
    ],
    "patterns_learned": [
      "Deduction order: assimilated first, then fiscal",
      "CFDI structure: regular in Percepciones, assimilated in OtrosPagos",
      "ISR calculation: uses tax tables with proportional adjustment"
    ],
    "suggested_scenarios": [
      {
        "id": "SCENARIO-SUGGESTED-001",
        "name": "Nómina Mensual - Aumento de Salario a Mitad del Periodo",
        "priority": "high",
        "reason": "Fills gap in salary increase scenarios",
        "estimated_complexity": "medium"
      }
    ]
  }
}
```

This systematic approach ensures comprehensive coverage and continuous improvement.

