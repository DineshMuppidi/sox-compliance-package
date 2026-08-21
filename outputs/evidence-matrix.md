# SOX ITGC — Evidence Collection Matrix

*SOX Compliance Package | Confidential - Internal Use*

20 evidence artifacts mapped across 9 IT General Controls. Standard retention period: **7 years (SOX Section 802 / SEC Rule 17a-4 alignment)**.

| Evidence ID | Control | Description | How to Collect | Owner | Storage |
|---|---|---|---|---|---|
| EV-001 | SOX-ITGC-001: User Access Provisioning (New Hire / Role Change) | New-access request tickets with system/data-owner approval | Export from ITSM ticketing system (e.g., ServiceNow), filtered by request type = New Access, for the testing period. | IT Security / IAM Team | ITSM archive / GRC evidence repository |
| EV-002 | SOX-ITGC-001: User Access Provisioning (New Hire / Role Change) | Provisioning confirmation showing access granted matches request | Export from IAM platform or target-system provisioning/audit log. | IT Security / IAM Team | IAM platform export / GRC evidence repository |
| EV-003 | SOX-ITGC-002: User Access Deprovisioning (Termination / Role Change) | HR termination report for the period | Export from HRIS (e.g., Workday) termination module. | HR / People Operations | HRIS export / GRC evidence repository |
| EV-004 | SOX-ITGC-002: User Access Deprovisioning (Termination / Role Change) | Access deactivation timestamps per terminated user | Export from IAM deprovisioning workflow or target-system audit log. | IT Security / IAM Team | IAM platform export / GRC evidence repository |
| EV-005 | SOX-ITGC-003: Privileged / Administrative Access Management | Point-in-time privileged/admin account listing per system | System-generated report from each in-scope system or PAM tool. | IT Security | PAM tool export / GRC evidence repository |
| EV-006 | SOX-ITGC-003: Privileged / Administrative Access Management | Privileged-access request & approval documentation | Export from ITSM ticketing system, filtered by request type = Privileged Access. | IT Security | ITSM archive / GRC evidence repository |
| EV-007 | SOX-ITGC-003: Privileged / Administrative Access Management | MFA enforcement and privileged-session logging configuration | Configuration export/screenshot from IAM and SIEM platforms. | IT Security | GRC evidence repository |
| EV-008 | SOX-ITGC-004: Segregation of Duties (SoD) — Financial Systems | Approved SoD conflict rule set / matrix | Signed-off document maintained jointly by IT Security and the Controller's Office. | IT Security / Controller's Office | GRC / policy repository |
| EV-009 | SOX-ITGC-004: Segregation of Duties (SoD) — Financial Systems | SoD conflict analysis report for the period | Automated output from the GRC/SoD analysis tool run against active user population. | IT Security | GRC evidence repository |
| EV-010 | SOX-ITGC-004: Segregation of Duties (SoD) — Financial Systems | Mitigating/compensating control evidence for flagged conflicts | Management review reports and sign-offs for each flagged conflict. | Controller's Office | GRC evidence repository |
| EV-011 | SOX-ITGC-005: Periodic User Access Review (UAR) | UAR access listing with reviewer sign-off | Export from UAR tool, or system access listing plus documented email/e-signature approval. | Business System Owner | GRC evidence repository |
| EV-012 | SOX-ITGC-005: Periodic User Access Review (UAR) | Remediation evidence for access flagged for removal | IAM deprovisioning log filtered to users flagged during the UAR. | IT Security / IAM Team | IAM platform export / GRC evidence repository |
| EV-013 | SOX-ITGC-006: Program / Application Change Management | Change tickets with justification, test evidence, and approval | Export from the change management system (e.g., Jira, ServiceNow) for the period. | IT Change Management | Change management system archive |
| EV-014 | SOX-ITGC-006: Program / Application Change Management | Deployment logs identifying the individual who deployed | Export from the CI/CD or deployment tool. | Application Development / DevOps | CI/CD system export |
| EV-015 | SOX-ITGC-007: Emergency Change Management | Emergency change tickets with retroactive approval timestamp | Export from the change management system, filtered by change type = Emergency. | IT Change Management | Change management system archive |
| EV-016 | SOX-ITGC-007: Emergency Change Management | Reconciliation of emergency changes to the standard change register | Reconciliation report/spreadsheet prepared by IT Change Management. | IT Change Management | GRC evidence repository |
| EV-017 | SOX-ITGC-008: Security Configuration & Log Monitoring | Approved security configuration baseline and current-state export | Approved baseline document plus configuration export from each in-scope system. | IT Security | GRC / policy repository |
| EV-018 | SOX-ITGC-008: Security Configuration & Log Monitoring | SIEM log ingestion and alert review/triage evidence | SIEM dashboard export and tickets for reviewed/triaged alerts. | IT Security / SOC | SIEM export / GRC evidence repository |
| EV-019 | SOX-ITGC-009: Batch Job & Backup Monitoring (Computer Operations) | Batch job completion and failure-investigation logs | Export from the job scheduler (e.g., Control-M, Autosys) completion report. | IT Operations | Job scheduler export / GRC evidence repository |
| EV-020 | SOX-ITGC-009: Batch Job & Backup Monitoring (Computer Operations) | Backup completion logs and quarterly restore-test results | Backup platform completion report plus restore-test evidence/screenshots. | IT Operations | Backup platform export / GRC evidence repository |
