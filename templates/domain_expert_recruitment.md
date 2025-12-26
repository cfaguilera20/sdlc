# Recruitment Domain Expert — Template

Use this when recruitment/talent acquisition tickets are complex, workflow-heavy, or compliance-sensitive.

## Domain: Recruitment & Talent Acquisition

Goal: Capture business rules, workflows, compliance requirements, and edge cases for recruitment processes.

Return: DomainKnowledgePack JSON (domain="Recruitment & Talent Acquisition")

## Key Areas to Cover

### Core Entities
- **Candidates**: Profiles, applications, status tracking
- **Job Postings**: Published positions with requirements and metadata
- **Applications**: Candidate submissions linked to job postings
- **Interviews**: Scheduled meetings with types, participants, feedback
- **Offers**: Formal job offers with terms and acceptance tracking
- **Workflows**: Configurable pipeline stages from application to hire

### Business Rules Focus
- Application status transitions and workflow enforcement
- Multi-application handling (one active per job posting)
- Interview scheduling constraints and timezone handling
- Offer management (single acceptance, expiration)
- Job posting lifecycle (draft → published → closed)
- Tenant isolation and data scoping

### Compliance Requirements
- **GDPR/Data Privacy**: Right to access, export, deletion
- **PII Protection**: Encryption at rest and in transit
- **Audit Trails**: All data access and modifications logged
- **Data Retention**: Minimum retention periods (2-7 years)
- **Consent Management**: Explicit consent for data processing
- **Multi-tenant Isolation**: Strict data boundaries
- **Background Checks**: FCRA compliance if applicable
- **EEO Reporting**: Equal opportunity data collection

### Edge Cases to Document
- Duplicate applications to same job posting
- Job posting closed with pending interviews
- Interview cancellations and rescheduling
- Multiple offers to same candidate
- Application withdrawal after offer sent
- Bulk imports with duplicates/errors
- Recruiter/hiring manager reassignment
- Timezone handling across participants
- Data migration scenarios (past dates, missing data)

### Calculations/Formulas
- Time-to-fill metrics
- Application conversion rates
- Offer acceptance rates
- Interview scheduling with timezone conversion
- Application scoring (if applicable)

### User Journeys
1. **Candidate**: Apply → Track status → Interview → Offer → Accept/Decline
2. **Recruiter**: Manage pipeline → Screen → Schedule → Collect feedback → Extend offer
3. **Hiring Manager**: Review applications → Provide feedback → Approve offers
4. **HR Admin**: Configure workflows → Manage permissions → Generate reports

### Data Requirements
**Inputs:**
- Candidate: email, name, phone, resume, cover letter, answers
- Job posting: title, description, requirements, dates, status
- Interview: application_id, interviewer(s), type, scheduled_at, timezone
- Offer: application_id, salary, start_date, benefits, expiration
- Status changes: application_id, new_status, user_id, reason

**Outputs:**
- Candidate profiles with application history
- Application details with timeline
- Job posting metrics and pipeline status
- Interview schedules (timezone-adjusted)
- Offer details and acceptance status
- Recruitment metrics and analytics
- Audit logs

### Open Questions to Clarify
- Exact workflow stage sequence and configurability
- Interview feedback rating structure
- Integration with external job boards
- Referral system requirements
- Background check workflows
- Offer negotiation handling
- Automated screening rules
- Data retention policies
- Bulk import formats and validation
- Candidate portal vs email-only communication
- ATS integrations (Greenhouse, Lever, etc.)
- Expected volume and scale

### Assumptions (Default)
- Standard pipeline: Applied → Screening → Interview → Offer → Hired
- Multi-tenant isolation via tenant_id scoping
- Shared authentication service (not within recruitment service)
- File storage via shared service (S3, etc.) with tenant-scoped paths
- Email-based notifications (optional SMS/push)
- Business hours for interview scheduling (configurable)
- Soft deletes for audit trail preservation
- Candidate profiles persist after application closure

## How Product Analyst Should Use This

When consuming the DomainKnowledgePack:
1. **Merge with TicketContext** to understand full scope
2. **Identify workflow complexity** - may need separate stories for workflow configuration
3. **Break down into stories:**
   - Core entities (candidates, applications, job postings)
   - Workflow engine (status transitions, rules)
   - Interview scheduling system
   - Offer management
   - Integration points (auth, storage, notifications)
   - Compliance features (audit, data export, retention)
   - Analytics and reporting
4. **Flag open questions** as blockers or assumptions
5. **Prioritize compliance** requirements early in backlog

## Example Use Cases

- Extracting recruitment module from monolith
- Adding new recruitment features (referrals, assessments)
- Migrating recruitment data
- Implementing compliance features (GDPR, audit trails)
- Building recruitment analytics
- Integrating with external ATS systems

