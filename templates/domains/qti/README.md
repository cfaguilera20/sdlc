# QTI Domain

This domain covers **IMS QTI (Question & Test Interoperability)** for interoperable **assessment items, tests, and question templates** (import/export) across LMSs and assessment tools.

## Domain Overview

QTI enables:
- Standardized representation of assessment items (questions), tests, sections, and item/test metadata
- Portable scoring semantics (responses, outcomes, response processing)
- Packaging/distribution of items and related assets (images/media) via IMS Content Packaging

## Domain Expert Agents

1. **Domain Expert — IMS QTI (Questions & Tests)**
   - Focus: QTI item/test model, packaging, scoring/response processing, interaction types, portability pitfalls, and mapping to internal question templates
   - Template: `domain_expert_qti.md`
   - **Use when:** Designing/validating question templates that must be importable/exportable via QTI, or implementing QTI ingest/export

## Related Domains

- **LMS** (`../lms/`) - Quizzes/assessments inside courses; progress/completion and gradebook mapping
- **Surveys** (`../surveys/`) - Question authoring patterns; branching/logic (note: QTI is assessment-focused, not survey-specific)
- **SCORM** (`../scorm/`) - Another interoperability standard; content packaging overlaps (manifest/assets), runtime tracking differs




