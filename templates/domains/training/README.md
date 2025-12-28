# Training Domain

This domain covers all aspects of employee training, development programs, and learning management.

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

## Usage

When working on training-related tickets:

1. Identify which subdomain(s) the ticket touches
2. Run the appropriate Domain Expert agent(s) using the template files
3. Collect the `DomainKnowledgePack` JSON output(s)
4. Use the pack(s) as input to Agent 02 (Product Analyst) for backlog generation

