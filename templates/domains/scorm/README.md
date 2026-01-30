# SCORM Domain

This domain covers **SCORM** interoperability for LMS platforms, including importing SCORM packages, launching SCOs, tracking runtime data (cmi.*), and mapping SCORM completion/score back into LMS progress.

## Domain Overview

SCORM capability typically requires:
- Package ingestion (`.zip`) and manifest parsing (`imsmanifest.xml`)
- Launch + runtime API implementation (SCORM 1.2 and/or SCORM 2004)
- Persisting runtime state (`cmi.*`) per learner attempt
- Translating SCORM outcomes into LMS completion rules, grades, and certificates
- Secure content delivery (signed URLs) and tenant isolation

## Domain Expert Agents

1. **Domain Expert — SCORM**
   - Focus: SCORM standards, runtime behavior, data model, edge cases, security, and how to map SCORM outcomes to LMS concepts
   - Template: `domain_expert_scorm.md`
   - **Use when:** Defining SCORM support scope (1.2 vs 2004), ingestion pipeline, runtime tracking, reporting, and interoperability constraints

## Related Domains

- **LMS** (`../lms/`) - Course catalog, progress tracking, certificates
- **Surveys/Assessments** (`../surveys/`) - Evaluation/testing concepts that may overlap with SCORM results


