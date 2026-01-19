# LTI Domain

This domain covers **LTI (Learning Tools Interoperability)** integration for LMS platforms, primarily **LTI 1.3** (OIDC + JWT) and the common services:
- Deep Linking (content selection)
- Names & Roles Provisioning (NRPS)
- Assignment and Grade Services (AGS) for grade passback

## Domain Overview

LTI enables:
- Embedding/launching third-party learning tools inside the LMS (tool consumer / platform)
- Exposing LMS resources to external platforms (tool provider) when needed
- Secure, standards-based SSO + context exchange (course, user role, resource link)

## Domain Expert Agents

1. **Domain Expert — LTI (1.3)**
   - Focus: LTI 1.3 launch flows, security, services (AGS/NRPS/Deep Linking), multi-tenant key management, and mapping to LMS concepts
   - Template: `domain_expert_lti.md`
   - **Use when:** Designing LTI integration strategy, configuration UI, data model, and edge cases

## Related Domains

- **LMS** (`../lms/`) - Progress, enrollments, course structure
- **SCORM** (`../scorm/`) - Another interoperability standard; complementary, not overlapping


