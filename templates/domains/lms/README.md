# LMS Domain Experts

This directory contains domain expert agents for Learning Management System (LMS) functionality.

## Domain Experts

### Core LMS
- `domain_expert_lms_saas.md` - Core LMS SaaS functionality (course catalog, content delivery, assessments, certificates)

### Integration & Access Control
- `domain_expert_lms_peoplecloud_integration.md` - PeopleCloud SSO and data sync integration
- `domain_expert_lms_rbac.md` - Role-based access control and permissions
- `domain_expert_lms_progress_tracking.md` - Progress tracking, completion logic, analytics
- `domain_expert_lms_reporting.md` - Reporting and analytics for admins, managers, and learners

### Technical Features
- `domain_expert_lms_video_management.md` - Video upload, processing, Cloudflare Stream integration, video player
- `domain_expert_lms_course_creation_wizard.md` - Course creation wizard workflow, phases, validation, publishing
- `domain_expert_lms_course_navigation.md` - Course navigation, sidebar, progress tracking, lesson sequencing
- `domain_expert_lms_course_import_export.md` - Moodle/SCORM import/export, course package format, content migration
- `domain_expert_lms_enrollment_access.md` - Enrollment types, access control, enrollment management
- `domain_expert_lms_time_limits.md` - Course completion deadlines, time limit enforcement, deadline notifications
- `domain_expert_lms_certificate_generation.md` - Certificate templates, PDF generation, verification, sharing
- `domain_expert_lms_content_management.md` - Content upload, organization, preview, editing, delivery

## Usage

Run these domain experts when working on:
- PeopleCloud integration tickets
- RBAC implementation
- Progress tracking features
- Reporting and analytics features
- Video management and upload
- Course creation and wizard
- Course navigation and structure
- Course import/export (Moodle, SCORM)
- Enrollment and access control
- Time limits and deadlines
- Certificate generation
- Content management
- Multi-tenant access control

## Examples

See `examples/` directory for example DomainKnowledgePack JSONs.
