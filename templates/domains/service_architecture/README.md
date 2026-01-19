# Service Architecture Domain

This domain covers service architecture decisions including naming conventions, bounded context boundaries, system of record (SoR) decisions, and microservice split strategies.

## Domain Overview

The Service Architecture domain helps make architectural decisions about:
- Service/module naming (customer-facing vs internal microservice names)
- Bounded context boundaries (what belongs in which service)
- System of Record (SoR) decisions (which service owns which data)
- Microservice split strategies (when to separate vs keep together)
- Integration boundaries and contracts

## Domain Expert Agents

1. **Domain Expert — Service Architecture (Naming & Boundaries)**
   - Focus: Service naming conventions, bounded context boundaries, SoR decisions, microservice splits
   - Template: `domain_expert_service_architecture_naming_boundaries.md`
   - **Use when:** Deciding how to name services/modules, what belongs in which service, and which service is the system of record for different data

## Usage

When working on architecture decisions:

1. First, run domain experts to understand domain knowledge (e.g., LMS, L&D Planning)
2. Then, run Service Architecture expert to make naming and boundary decisions
3. Collect the `DomainKnowledgePack` JSON output
4. Use the pack as input to architecture planning and implementation

## Related Domains

- **LMS** (`../lms/`) - LMS domain knowledge (what an LMS does)
- **Learning & Development** (`../learning_development/`) - L&D Planning domain knowledge
- **Training** (`../training/`) - Legacy training module analysis

## Note

This domain is for **architectural decisions**, not domain knowledge. Domain experts (LMS, L&D, etc.) focus on "what the domain does", while Service Architecture focuses on "how to structure services and name them".

