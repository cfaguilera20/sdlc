# Learning & Development Domain

This domain covers Learning & Development (L&D) Planning and governance, including annual planning, skills gap identification, initiative selection, and evaluation.

## Domain Overview

The Learning & Development domain manages the complete L&D planning lifecycle, including:
- Plan Anual de Capacitación y Desarrollo (annual training and development plan)
- Skills gap identification and analysis
- Initiative selection (programs, workshops, mentoring, e-learning)
- Calendar and resource management (budget, providers, instructors, hours, locations)
- Evaluation and impact measurement (Kirkpatrick model, ROI, performance, retention)

## Domain Expert Agents

1. **Domain Expert — L&D Planning**
   - Focus: Annual planning, skills gaps, initiatives, calendar/resources, evaluation/impact
   - Template: `domain_expert_ld_planning.md`
   - **Use when:** Analyzing L&D Planning domain requirements, understanding planning business rules, workflows, and edge cases
   - **Note:** This expert focuses on L&D Planning domain knowledge only. Service naming and architecture boundaries are handled separately by Service Architecture expert.

## Related Domains

- **LMS** (`../lms/`) - Learning delivery and execution (course catalogs, content delivery, progress, assessments, certificates)
- **Training** (`../training/`) - Legacy training module analysis (cohorts, schedules, participants)
- **Service Architecture** (`../service_architecture/`) - Service naming and boundary decisions

## Usage

When working on L&D Planning-related tickets:

1. Identify which L&D Planning subdomain(s) the ticket touches
2. Run the L&D Planning Domain Expert agent using the template file
3. Collect the `DomainKnowledgePack` JSON output
4. Use the pack as input to Agent 02 (Product Analyst) for backlog generation
5. Architecture/product team uses domain knowledge packs to make naming and service boundary decisions (via Service Architecture expert)
