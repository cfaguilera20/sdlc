# PeopleCloud Monolith - Domains Inventory

This document lists all business domains identified in the PeopleCloud monolith and their scaffold status.

## Domains Status

### ✅ Completed Domain Scaffolds

1. **Payroll** - `templates/domains/payroll/`
   - Status: Complete with multiple sub-agents
   - Sub-agents: IMSS, INFONAVIT, Operations, Split

2. **Recruitment** - `templates/domains/recruitment/`
   - Status: Complete with 5 sub-agents
   - Sub-agents: Pipeline & Stages, Candidate Management, Interview & Assessment, Offer & Onboarding, Analytics & Compliance

3. **Attendance** - `templates/domains/attendance/`
   - Status: Complete with 4 sub-agents
   - Sub-agents: Time Records & Registrations, Shifts & Schedules, Policies & Rules, Devices & Integration
   - Files: README, 4 templates, 4 example JSONs

4. **Performance** - `templates/domains/performance/`
   - Status: Complete with 3 sub-agents
   - Sub-agents: Evaluations & Reviews, Objectives & KPIs, Workflows & Tasks
   - Files: README, 3 templates, 3 example JSONs

5. **Training** - `templates/domains/training/`
   - Status: Complete with 2 sub-agents
   - Sub-agents: Programs & Courses, Applications & Participants
   - Files: README, 2 templates, 2 example JSONs

6. **Structure & Organization** - `templates/domains/structure_organization/`
   - Status: Complete with 2 sub-agents
   - Sub-agents: Hierarchy & Units, Positions & Profiles
   - Files: README, 2 templates, 2 example JSONs

7. **Compensations** - `templates/domains/compensations/`
   - Status: Complete with 1 sub-agent
   - Sub-agents: Structure & Management
   - Files: README, 1 template, 1 example JSON

8. **Surveys** - `templates/domains/surveys/`
   - Status: Complete with 2 sub-agents
   - Sub-agents: Surveys & Assessments, Evaluations & Results
   - Files: README, 2 templates, 2 example JSONs

9. **Users Management** - `templates/domains/users_management/`
   - Status: Complete with 2 sub-agents
   - Sub-agents: Accounts & Profiles, Permissions & Roles
   - Files: README, 2 templates, 2 example JSONs

### 📋 Identified Domains (Not Yet Scaffolded)

10. **ThreeSixty** - 360-degree feedback and evaluations
    - Location: `core/ThreeSixty/`, `app/controller/ThreeSixty/`
    - Key features: Evaluations, evaluators, groups, competences, applications

11. **TalentManagement** - Talent management and nine-box grid
    - Location: `app/controller/TalentManagement/`
    - Key features: Nine-box, calibrations, evaluations, ranges, grid

12. **Budget** - Budget management and scenarios
    - Location: `core/Budget/`, `app/controller/Budget/`
    - Key features: Budget scenarios, budget planning

13. **Projects** - Project and task management
    - Location: `app/services/Projects/`
    - Key features: Projects, tasks, task status

14. **Kudos** - Recognition and rewards
    - Location: `app/transformers/Kudos/`
    - Key features: Applications, boxes, recognition

15. **Contracts** - Contract management
    - Location: `core/Contracts/`
    - Key features: Contract types, contract management

16. **Documents** - Document management
    - Location: `core/Documents/`
    - Key features: Document storage, management

17. **Notifications** - Notification system
    - Location: `core/Notificacion/`, `app/controller/Notifications/`
    - Key features: Notifications, broadcasts

18. **Reports** - Reporting system
    - Location: `core/Report/`, `core/Reports/`
    - Key features: Report generation, analytics

## Next Steps

To scaffold remaining domains:
   - Create domain README
   - Identify sub-domains (2-6 sub-agents)
   - Create domain expert templates
   - Create example JSONs
   - Generate domain scaffold JSON

3. Use the Domain Scaffolder agent (`agents/domain.md`) to generate complete scaffolds for each domain

## Usage

When working on tickets for any domain:

1. Check if domain scaffold exists in `templates/domains/<domain_name>/`
2. If exists, use the domain expert templates to generate DomainKnowledgePack
3. If not exists, run Domain Scaffolder agent to create the scaffold first
4. Use DomainKnowledgePack as input to Agent 02 (Product Analyst)

