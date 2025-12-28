# Attendance Domain

This domain covers all aspects of employee attendance, time tracking, schedules, and shift management.

## Domain Overview

The Attendance domain manages the complete time and attendance lifecycle, including:
- Time clock records and registrations
- Shift management and scheduling
- Attendance policies and rules
- Schedule assignments and rotations
- Device integration for time tracking
- Attendance reports and analytics

## Domain Expert Agents

This domain is broken down into specialized expert agents:

1. **Domain Expert — Attendance (Time Records & Registrations)**
   - Focus: Time clock records, check-in/check-out, mobile registrations, record validation
   - Template: `domain_expert_attendance_time_records.md`

2. **Domain Expert — Attendance (Shifts & Schedules)**
   - Focus: Shift definitions, schedule management, rotating shifts, schedule assignments
   - Template: `domain_expert_attendance_shifts_schedules.md`

3. **Domain Expert — Attendance (Policies & Rules)**
   - Focus: Attendance policies, policy groups, schedule policies, rule enforcement
   - Template: `domain_expert_attendance_policies_rules.md`

4. **Domain Expert — Attendance (Devices & Integration)**
   - Focus: Time clock devices, device-employee associations, device synchronization
   - Template: `domain_expert_attendance_devices_integration.md`

## Usage

When working on attendance-related tickets:

1. Identify which subdomain(s) the ticket touches
2. Run the appropriate Domain Expert agent(s) using the template files
3. Collect the `DomainKnowledgePack` JSON output(s)
4. Use the pack(s) as input to Agent 02 (Product Analyst) for backlog generation

## Example Files

See `examples/` directory for example `DomainKnowledgePack` JSONs that demonstrate the expected structure and content for each subdomain.

