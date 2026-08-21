# SOX ITGC Test Procedures Manual

*SOX Compliance Package | Confidential - Internal Use*

Complete test procedures for all 9 IT General Controls in scope (see `sox/itgc_catalog.py` for control design detail). Each procedure documents the test objective, test type, sample-size approach, numbered test steps, expected results, and testing frequency for use as an audit workpaper template.

| Control ID | Test Type | Frequency |
|---|---|---|
| SOX-ITGC-001 | Design & Operating Effectiveness | Quarterly interim testing with a year-end roll-forward covering the remaining period. |
| SOX-ITGC-002 | Design & Operating Effectiveness | Quarterly interim testing with a year-end roll-forward. |
| SOX-ITGC-003 | Design & Operating Effectiveness | Quarterly. |
| SOX-ITGC-004 | Design & Operating Effectiveness | Quarterly. |
| SOX-ITGC-005 | Design & Operating Effectiveness | Quarterly. |
| SOX-ITGC-006 | Design & Operating Effectiveness | Quarterly interim testing with a year-end roll-forward. |
| SOX-ITGC-007 | Design & Operating Effectiveness | Quarterly. |
| SOX-ITGC-008 | Design & Operating Effectiveness | Continuous automated monitoring; sample-based testing performed quarterly. |
| SOX-ITGC-009 | Design & Operating Effectiveness | Daily automated monitoring; sample-based testing performed quarterly; restore test performed quarterly. |

---

## SOX-ITGC-001: User Access Provisioning (New Hire / Role Change)

**Control:** New user access to in-scope financial systems (ERP, general ledger, sub-ledgers) is requested via a documented access request, approved by the system or data owner prior to provisioning, and provisioned by IT strictly in accordance with the approved request.

**Test Objective:** Determine whether new user access to in-scope financial systems is requested, approved by the appropriate system/data owner, and provisioned consistent with the approved request.

**Test Type:** Design & Operating Effectiveness

**Sample Size Approach:** Obtain the population of new user access requests processed during the period; select 25 items via attribute sampling (or 100% if the population is <25).

**Test Steps:**

1. Obtain the population of new user access requests to in-scope systems for the period from the ticketing system and agree the population count to a system-generated report.
2. Select a sample per the sampling approach above.
3. For each sample item, obtain the access request and identify the requestor, the system/data owner approver, and the requested access/role.
4. Verify the request was approved by an authorized system/data owner prior to the provisioning date/timestamp.
5. Verify the access ultimately provisioned in the target system matches the access approved on the request, with no unapproved scope.
6. Document any exceptions (missing approval, approval after provisioning, access broader than approved) for evaluation.

**Expected Results:** 100% of sampled access requests are approved by an authorized system/data owner prior to provisioning, and provisioned access matches the approved request with no unapproved scope.

**Testing Frequency:** Quarterly interim testing with a year-end roll-forward covering the remaining period.

---

## SOX-ITGC-002: User Access Deprovisioning (Termination / Role Change)

**Control:** Access for terminated employees and contractors is disabled within a defined SLA (same business day) of the termination date received from HR, and access for employees changing roles is adjusted to remove entitlements no longer required.

**Test Objective:** Determine whether access for terminated employees/contractors is disabled within the defined SLA, and role-change access no longer required is removed.

**Test Type:** Design & Operating Effectiveness

**Sample Size Approach:** Obtain the population of terminations during the period from HR/HRIS; select 25 items via attribute sampling (or 100% if the population is <25).

**Test Steps:**

1. Obtain the HR termination report for the period and agree population completeness to the HRIS extract.
2. Select a sample of terminated users per the sampling approach above.
3. For each sample item, identify the termination date per HR records.
4. Obtain the account status/audit log for each in-scope system and identify the date access was disabled.
5. Calculate elapsed time between termination date and access-disablement date; compare to the defined SLA (same business day).
6. For a sample of role-change users, confirm access no longer required under the new role was removed.
7. Document any exceptions exceeding the SLA for evaluation.

**Expected Results:** Access is disabled within the defined SLA for 100% of sampled terminations, and role-change access no longer required is removed.

**Testing Frequency:** Quarterly interim testing with a year-end roll-forward.

---

## SOX-ITGC-003: Privileged / Administrative Access Management

**Control:** Access to privileged accounts (admin, DBA, superuser) on in-scope systems is restricted to authorized personnel, requires documented business justification and system-owner approval, and is subject to enhanced monitoring including MFA and session logging.

**Test Objective:** Determine whether privileged/administrative access is restricted to authorized personnel with documented justification and approval, and is subject to enhanced monitoring (MFA, session logging).

**Test Type:** Design & Operating Effectiveness

**Sample Size Approach:** Test 100% of the privileged-account population as of a point in time, plus a sample of privileged-access grants made during the period.

**Test Steps:**

1. Obtain a system-generated listing of all privileged/admin accounts on each in-scope system as of a point in time.
2. Compare the listing to an independently maintained list of personnel authorized for privileged access and identify any accounts not on the authorized list.
3. For a sample of privileged-access grants made during the period, obtain the request/approval documentation and verify business justification and system-owner approval predate the grant.
4. Confirm MFA is enforced for privileged accounts by reviewing IAM/MFA configuration.
5. Confirm privileged-session activity is logged by reviewing SIEM/logging configuration for the relevant systems.
6. Document any unauthorized or unapproved privileged accounts as exceptions.

**Expected Results:** All privileged accounts are held by authorized personnel with documented approval; MFA and session logging are enforced for 100% of privileged accounts.

**Testing Frequency:** Quarterly.

---

## SOX-ITGC-004: Segregation of Duties (SoD) — Financial Systems

**Control:** Access rights within in-scope financial applications are configured and periodically analyzed to prevent an individual user from holding conflicting access (e.g., create and approve a vendor, or post and approve a journal entry) without a documented, monitored mitigating control.

**Test Objective:** Determine whether user access within in-scope financial systems is free of unmitigated segregation-of-duties conflicts.

**Test Type:** Design & Operating Effectiveness

**Sample Size Approach:** Run the SoD rule set against the full population of active users in each in-scope system (100% population testing via automated rule engine); re-perform for a sub-sample to validate rule-engine accuracy.

**Test Steps:**

1. Obtain the current SoD conflict rule set/matrix and confirm it was reviewed/approved by the Controller's Office within the last 12 months.
2. Obtain evidence that the automated SoD conflict analysis was run against the full population of active users in each in-scope system for the period.
3. Obtain the resulting conflict report and identify all users flagged with an unmitigated conflict.
4. For each flagged conflict, determine whether a documented, monitored mitigating/compensating control exists and obtain evidence that control operated.
5. For conflicts without a documented mitigating control, document as an exception.
6. Re-perform the conflict analysis for a sub-sample of users to independently validate the rule engine's accuracy.

**Expected Results:** All identified SoD conflicts either do not exist or are covered by an evidenced, operating mitigating control.

**Testing Frequency:** Quarterly.

---

## SOX-ITGC-005: Periodic User Access Review (UAR)

**Control:** System and data owners formally review the population of users with access to in-scope financial systems on a quarterly basis, confirm continued business need, and any inappropriate access identified is revoked within a defined SLA; the review and any remediation are evidenced and signed off.

**Test Objective:** Determine whether periodic user access reviews are performed by the appropriate system/data owner, inappropriate access is identified, and remediation occurs timely.

**Test Type:** Design & Operating Effectiveness

**Sample Size Approach:** Test 100% of in-scope systems' UAR cycles performed during the period (typically a small population).

**Test Steps:**

1. Obtain evidence a UAR was performed for each in-scope system during the testing period (signed-off access listing or UAR tool export).
2. Confirm the review was performed by the appropriate system/data owner, not a peer or subordinate of the reviewed users.
3. Confirm the reviewed population reconciles to the full user listing for that system as of the review date.
4. Identify any access flagged 'remove' during the review and trace to evidence the access was removed within the defined SLA.
5. Confirm the completed review is retained with a dated sign-off.
6. Document any missed reviews, incomplete populations, or untimely remediation as exceptions.

**Expected Results:** A UAR is completed each quarter for every in-scope system by the appropriate owner, and 100% of flagged access is removed within SLA.

**Testing Frequency:** Quarterly.

---

## SOX-ITGC-006: Program / Application Change Management

**Control:** Changes to in-scope financial applications and supporting infrastructure (code, configuration, interfaces) are documented, tested in a non-production environment, approved by a designated change approver, and migrated to production only by personnel without conflicting development access.

**Test Objective:** Determine whether changes to in-scope financial applications are documented, tested in a non-production environment, approved prior to migration, and deployed by personnel independent of development.

**Test Type:** Design & Operating Effectiveness

**Sample Size Approach:** Obtain the population of production changes to in-scope systems for the period; select 25 items via attribute sampling (or 100% if the population is <25).

**Test Steps:**

1. Obtain the change management system's population of production changes to in-scope financial applications for the period; agree completeness to a system-generated report.
2. Select a sample of changes per the sampling approach above.
3. For each sample item, obtain the change ticket and confirm documented business/technical justification.
4. Verify evidence of testing in a non-production environment prior to deployment.
5. Verify documented approval from a designated change approver was obtained prior to the production migration date.
6. Verify the individual who migrated the change to production is independent of (did not also author) the change, or that a compensating review occurred.
7. Document any changes lacking testing evidence, approval, or independent deployment as exceptions.

**Expected Results:** 100% of sampled changes are documented, tested, and approved prior to deployment, and deployed with appropriate segregation from development.

**Testing Frequency:** Quarterly interim testing with a year-end roll-forward.

---

## SOX-ITGC-007: Emergency Change Management

**Control:** Emergency changes that bypass the standard change process require post-implementation documentation and retroactive approval by a designated approver within a defined SLA (2 business days), and are logged and reconciled against the standard change register.

**Test Objective:** Determine whether emergency changes receive timely retroactive approval and are reconciled to the standard change register.

**Test Type:** Design & Operating Effectiveness

**Sample Size Approach:** Test 100% of emergency changes during the period given typically low volume; apply attribute sampling if volume is high.

**Test Steps:**

1. Obtain the population of changes flagged 'emergency' in the change management system for the period.
2. For each item (or sample), obtain the post-implementation documentation and identify the retroactive approver and approval timestamp.
3. Calculate elapsed time from implementation to retroactive approval; compare to the defined SLA (2 business days).
4. Confirm the emergency change is logged and reconciled in the standard change register.
5. Document any emergency changes lacking retroactive approval, exceeding the SLA, or missing from the register as exceptions.

**Expected Results:** 100% of emergency changes receive retroactive approval within the defined SLA and are reconciled to the standard change register.

**Testing Frequency:** Quarterly.

---

## SOX-ITGC-008: Security Configuration & Log Monitoring

**Control:** Security configurations (password policy, MFA, session timeout) on in-scope systems are set per an approved baseline and periodically validated; security event logs (failed logins, privileged activity, configuration changes) are centrally collected and reviewed/alerted on a defined cadence.

**Test Objective:** Determine whether security configurations conform to the approved baseline and security event logs are centrally collected and reviewed/alerted on a defined cadence.

**Test Type:** Design & Operating Effectiveness

**Sample Size Approach:** Test 100% of in-scope systems' current configuration against the approved baseline; select a sample of monitoring periods (e.g., 3 months) for the log-review component.

**Test Steps:**

1. Obtain the approved security configuration baseline (password policy, MFA, session timeout) for in-scope systems.
2. Obtain the current configuration export for each in-scope system and compare to the approved baseline; document deviations.
3. Obtain evidence of the monthly baseline validation for a sample of months during the period.
4. Obtain evidence that security event logs (failed logins, privileged activity, configuration changes) are centrally collected (e.g., SIEM ingestion report).
5. For a sample of months, obtain evidence that log review/alerting occurred per the defined cadence and that alerts were triaged/resolved.
6. Document configuration deviations or missed log reviews as exceptions.

**Expected Results:** Security configurations conform to the approved baseline with no unremediated deviations, and log review/alerting occurred each period per the defined cadence.

**Testing Frequency:** Continuous automated monitoring; sample-based testing performed quarterly.

---

## SOX-ITGC-009: Batch Job & Backup Monitoring (Computer Operations)

**Control:** Scheduled batch jobs (interfaces, financial close processes) supporting in-scope financial systems are monitored for successful completion, with failures investigated, resolved, and logged; backups are executed per schedule and periodically test-restored to confirm recoverability.

**Test Objective:** Determine whether scheduled batch jobs supporting in-scope financial systems are monitored for completion with failures resolved, and backups are executed per schedule and periodically test-restored.

**Test Type:** Design & Operating Effectiveness

**Sample Size Approach:** Select a sample of batch job run dates (e.g., 25 across the period) and a sample of backup dates; test 100% of periodic restore tests performed during the period.

**Test Steps:**

1. Obtain the population of scheduled batch jobs supporting in-scope financial systems and the job-monitoring tool's completion log for the period.
2. Select a sample of run dates and confirm each sampled job completed successfully or, where it failed, was investigated and resolved with evidence retained.
3. Obtain the backup schedule and backup completion logs for in-scope systems; select a sample of backup dates and confirm successful completion.
4. Obtain evidence of the quarterly restore test(s) performed during the period and confirm the restore was successful.
5. Document any unresolved job failures, missed backups, or failed/skipped restore tests as exceptions.

**Expected Results:** Sampled batch jobs completed successfully or failures were investigated/resolved; backups completed per schedule and the periodic restore test was successful.

**Testing Frequency:** Daily automated monitoring; sample-based testing performed quarterly; restore test performed quarterly.

---

