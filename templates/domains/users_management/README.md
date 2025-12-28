# Users Management Domain

This domain covers all aspects of user management, profiles, permissions, and account administration.

## Domain Overview

The Users Management domain manages the complete user lifecycle, including:
- User account creation and management
- User profiles and personal information
- Permissions and role management
- User configuration and settings
- Bulk user operations
- Privacy and data management

## Domain Expert Agents

1. **Domain Expert — Users Management (Accounts & Profiles)**
   - Focus: User accounts, profiles, personal information, configuration, bulk operations
   - Template: `domain_expert_users_accounts_profiles.md`

2. **Domain Expert — Users Management (Permissions & Roles)**
   - Focus: Permissions, roles, access control, authorization rules
   - Template: `domain_expert_users_permissions_roles.md`

## Usage

When working on user management-related tickets:

1. Identify which subdomain(s) the ticket touches
2. Run the appropriate Domain Expert agent(s) using the template files
3. Collect the `DomainKnowledgePack` JSON output(s)
4. Use the pack(s) as input to Agent 02 (Product Analyst) for backlog generation

