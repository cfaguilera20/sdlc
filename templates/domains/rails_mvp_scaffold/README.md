# Rails MVP Scaffold Domain

This domain covers the technical setup and configuration of new Rails projects with standard MVP-ready features.

## Domain Overview

The Rails MVP Scaffold domain manages the foundational setup for new Rails applications, including:
- Authentication with Devise
- Admin panel with Active Admin
- Multi-tenant architecture
- Database configuration and migrations
- MVP boilerplate and best practices

## Domain Expert Agents

This domain is broken down into specialized expert agents:

1. **Domain Expert — Rails MVP Scaffold (Authentication & Devise)**
   - Focus: Devise setup, user models, authentication flows, authorization
   - Template: `domain_expert_rails_mvp_scaffold_authentication.md`

2. **Domain Expert — Rails MVP Scaffold (Active Admin)**
   - Focus: Active Admin configuration, admin models, customizations
   - Template: `domain_expert_rails_mvp_scaffold_active_admin.md`

3. **Domain Expert — Rails MVP Scaffold (Multi-Tenant Architecture)**
   - Focus: Multi-tenancy strategies, tenant isolation, data scoping
   - Template: `domain_expert_rails_mvp_scaffold_multi_tenant.md`

4. **Domain Expert — Rails MVP Scaffold (Database & Migrations)**
   - Focus: Database setup, migration patterns, schema design, seeds
   - Template: `domain_expert_rails_mvp_scaffold_database.md`

5. **Domain Expert — Rails MVP Scaffold (MVP Foundation)**
   - Focus: Project structure, initial setup, boilerplate, best practices
   - Template: `domain_expert_rails_mvp_scaffold_foundation.md`

## Usage

When working on Rails project setup or MVP initialization tickets:

1. Identify which subdomain(s) the ticket touches
2. Run the appropriate Domain Expert agent(s) using the template files
3. Collect the `DomainKnowledgePack` JSON output(s)
4. Use the pack(s) as input to Agent 02 (Product Analyst) for backlog generation

## Example Files

See `examples/` directory for example `DomainKnowledgePack` JSONs that demonstrate the expected structure and content for each subdomain.

