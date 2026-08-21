# IT General Controls — Design Workbook

*SOX Compliance Package | Confidential - Internal Use*

**9 ITGCs.** 5/9 implemented, 4/9 operating-effectiveness tested. Audit readiness: **44%**.

| Control ID | Title | Domain | Owner | Type | Frequency | Risk | Status | Design Tested | Operating Tested |
|---|---|---|---|---|---|---|---|---|---|
| SOX-ITGC-001 | User Access Provisioning (New Hire / Role Change) | Access Management | IT Security / IAM Team | Preventive | Continuous (event-driven) | **High** | Implemented | Yes | Yes |
| SOX-ITGC-002 | User Access Deprovisioning (Termination / Role Change) | Access Management | IT Security / IAM Team | Preventive | Continuous (event-driven) | **Critical** | Implemented | Yes | No |
| SOX-ITGC-003 | Privileged / Administrative Access Management | Access Management | IT Security | Preventive | Continuous | **Critical** | In Progress | Yes | No |
| SOX-ITGC-004 | Segregation of Duties (SoD) — Financial Systems | Segregation of Duties | IT Security / Controller's Office | Preventive/Detective | Quarterly | **High** | In Progress | No | No |
| SOX-ITGC-005 | Periodic User Access Review (UAR) | Access Reviews | Business System Owners / IT Security | Detective | Quarterly | **High** | Implemented | Yes | Yes |
| SOX-ITGC-006 | Program / Application Change Management | Change Management | IT Change Management / Application Development | Preventive | Continuous (per release) | **High** | Implemented | Yes | Yes |
| SOX-ITGC-007 | Emergency Change Management | Change Management | IT Change Management | Detective/Corrective | Continuous (event-driven) | **Medium** | In Progress | Yes | No |
| SOX-ITGC-008 | Security Configuration & Log Monitoring | Monitoring | IT Security / SOC | Detective | Continuous monitoring / Monthly baseline validation | **Medium** | In Progress | No | No |
| SOX-ITGC-009 | Batch Job & Backup Monitoring (Computer Operations) | Monitoring | IT Operations | Detective | Daily (job monitoring) / Quarterly (restore test) | **Medium** | Implemented | Yes | Yes |

## Control Detail

### SOX-ITGC-001: User Access Provisioning (New Hire / Role Change)
- **Domain:** Access Management (Authorization)
- **Description:** New user access to in-scope financial systems (ERP, general ledger, sub-ledgers) is requested via a documented access request, approved by the system or data owner prior to provisioning, and provisioned by IT strictly in accordance with the approved request.
- **Owner:** IT Security / IAM Team | **Type:** Preventive | **Frequency:** Continuous (event-driven) | **Automation:** IT-Dependent Manual
- **Risk Rating:** High | **COSO Principles:** P3, P5, P10, P11
- **Implementation Status:** Implemented | **Design Tested:** Yes | **Operating Tested:** Yes | **Last Reviewed:** 2026-07-15

### SOX-ITGC-002: User Access Deprovisioning (Termination / Role Change)
- **Domain:** Access Management (Authorization)
- **Description:** Access for terminated employees and contractors is disabled within a defined SLA (same business day) of the termination date received from HR, and access for employees changing roles is adjusted to remove entitlements no longer required.
- **Owner:** IT Security / IAM Team | **Type:** Preventive | **Frequency:** Continuous (event-driven) | **Automation:** IT-Dependent Manual
- **Risk Rating:** Critical | **COSO Principles:** P3, P5, P10, P11
- **Implementation Status:** Implemented | **Design Tested:** Yes | **Operating Tested:** No | **Last Reviewed:** 2026-07-15

### SOX-ITGC-003: Privileged / Administrative Access Management
- **Domain:** Access Management (Authorization)
- **Description:** Access to privileged accounts (admin, DBA, superuser) on in-scope systems is restricted to authorized personnel, requires documented business justification and system-owner approval, and is subject to enhanced monitoring including MFA and session logging.
- **Owner:** IT Security | **Type:** Preventive | **Frequency:** Continuous | **Automation:** Manual
- **Risk Rating:** Critical | **COSO Principles:** P3, P5, P10, P11
- **Implementation Status:** In Progress | **Design Tested:** Yes | **Operating Tested:** No | **Last Reviewed:** 2026-06-20

### SOX-ITGC-004: Segregation of Duties (SoD) — Financial Systems
- **Domain:** Segregation of Duties (Authorization)
- **Description:** Access rights within in-scope financial applications are configured and periodically analyzed to prevent an individual user from holding conflicting access (e.g., create and approve a vendor, or post and approve a journal entry) without a documented, monitored mitigating control.
- **Owner:** IT Security / Controller's Office | **Type:** Preventive/Detective | **Frequency:** Quarterly | **Automation:** IT-Dependent Manual
- **Risk Rating:** High | **COSO Principles:** P3, P8, P10, P11
- **Implementation Status:** In Progress | **Design Tested:** No | **Operating Tested:** No | **Last Reviewed:** 2026-05-10

### SOX-ITGC-005: Periodic User Access Review (UAR)
- **Domain:** Access Reviews (Access Reviews)
- **Description:** System and data owners formally review the population of users with access to in-scope financial systems on a quarterly basis, confirm continued business need, and any inappropriate access identified is revoked within a defined SLA; the review and any remediation are evidenced and signed off.
- **Owner:** Business System Owners / IT Security | **Type:** Detective | **Frequency:** Quarterly | **Automation:** Manual
- **Risk Rating:** High | **COSO Principles:** P5, P16, P17
- **Implementation Status:** Implemented | **Design Tested:** Yes | **Operating Tested:** Yes | **Last Reviewed:** 2026-07-30

### SOX-ITGC-006: Program / Application Change Management
- **Domain:** Change Management (Change Management)
- **Description:** Changes to in-scope financial applications and supporting infrastructure (code, configuration, interfaces) are documented, tested in a non-production environment, approved by a designated change approver, and migrated to production only by personnel without conflicting development access.
- **Owner:** IT Change Management / Application Development | **Type:** Preventive | **Frequency:** Continuous (per release) | **Automation:** IT-Dependent Manual
- **Risk Rating:** High | **COSO Principles:** P7, P9, P10, P11, P12
- **Implementation Status:** Implemented | **Design Tested:** Yes | **Operating Tested:** Yes | **Last Reviewed:** 2026-07-01

### SOX-ITGC-007: Emergency Change Management
- **Domain:** Change Management (Change Management)
- **Description:** Emergency changes that bypass the standard change process require post-implementation documentation and retroactive approval by a designated approver within a defined SLA (2 business days), and are logged and reconciled against the standard change register.
- **Owner:** IT Change Management | **Type:** Detective/Corrective | **Frequency:** Continuous (event-driven) | **Automation:** Manual
- **Risk Rating:** Medium | **COSO Principles:** P9, P10, P16
- **Implementation Status:** In Progress | **Design Tested:** Yes | **Operating Tested:** No | **Last Reviewed:** 2026-06-15

### SOX-ITGC-008: Security Configuration & Log Monitoring
- **Domain:** Monitoring (Monitoring)
- **Description:** Security configurations (password policy, MFA, session timeout) on in-scope systems are set per an approved baseline and periodically validated; security event logs (failed logins, privileged activity, configuration changes) are centrally collected and reviewed/alerted on a defined cadence.
- **Owner:** IT Security / SOC | **Type:** Detective | **Frequency:** Continuous monitoring / Monthly baseline validation | **Automation:** Automated
- **Risk Rating:** Medium | **COSO Principles:** P11, P16, P17
- **Implementation Status:** In Progress | **Design Tested:** No | **Operating Tested:** No | **Last Reviewed:** 2026-05-01

### SOX-ITGC-009: Batch Job & Backup Monitoring (Computer Operations)
- **Domain:** Monitoring (Monitoring)
- **Description:** Scheduled batch jobs (interfaces, financial close processes) supporting in-scope financial systems are monitored for successful completion, with failures investigated, resolved, and logged; backups are executed per schedule and periodically test-restored to confirm recoverability.
- **Owner:** IT Operations | **Type:** Detective | **Frequency:** Daily (job monitoring) / Quarterly (restore test) | **Automation:** Automated / IT-Dependent Manual
- **Risk Rating:** Medium | **COSO Principles:** P11, P16
- **Implementation Status:** Implemented | **Design Tested:** Yes | **Operating Tested:** Yes | **Last Reviewed:** 2026-07-20

## Risk Rating Legend

- **Low**: Design and operating effectiveness confirmed; monitor via routine review cycle.
- **Medium**: Control operating; minor design or evidence gaps being closed this quarter.
- **High**: Control partially implemented or not yet operating-effectiveness tested.
- **Critical**: Control gap represents likely exposure to a material weakness if unremediated.
