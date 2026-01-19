# Training Domain

This domain covers all aspects of employee training, development programs, and learning management, specifically focused on legacy PeopleCloud Training module analysis.

## Domain Overview

The Training domain manages the complete training lifecycle, including:
- Training program creation and management
- Course and resource management
- Training plan applications
- Participant tracking and enrollment
- Training providers and instructors
- Training phases and progress tracking

## Domain Expert Agents

1. **Domain Expert — Training (Programs & Courses)**
   - Focus: Training programs, courses, resources, providers, instructors
   - Template: `domain_expert_training_programs_courses.md`

2. **Domain Expert — Training (Applications & Participants)**
   - Focus: Training plan applications, participant enrollment, progress tracking, completion
   - Template: `domain_expert_training_applications_participants.md`

3. **Domain Expert — Training (PeopleCloud Legacy: Phases, Applications, Schedules)**
   - Focus: **Legacy PeopleCloud Training module** - phases, plan applications, schedules, schedule details, participant slot allocation, invitation workflow
   - Template: `domain_expert_training_peoplecloud_legacy_phases_schedules.md`
   - **Use when:** Migrating or extracting the PeopleCloud Training module to understand existing business rules, workflows, and edge cases
   - **Analyzes:** training_plan → training_phase → training_program relationships, training_plan_application creation, training_schedule + training_schedule_detail recurrence, participant capacity management, PC_Action invitations

## Related Domains

- **LMS** (`../lms/`) - Modern LMS domain knowledge (course catalogs, content delivery, progress, assessments, certificates)
- **Learning & Development** (`../learning_development/`) - Annual planning and governance (Plan Anual de Capacitación y Desarrollo)

## Usage

When working on training-related tickets:

1. Identify which subdomain(s) the ticket touches
2. Run the appropriate Domain Expert agent(s) using the template files
3. Collect the `DomainKnowledgePack` JSON output(s)
4. Use the pack(s) as input to Agent 02 (Product Analyst) for backlog generation
