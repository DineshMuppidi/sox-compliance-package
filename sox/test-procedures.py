#!/usr/bin/env python3
"""
SOX ITGC Test Procedures Manual
=====================================
Generates the complete audit test-procedure set for every control in the
ITGC catalog (see itgc_catalog.py): test objective, test type, sample-size
approach, numbered test steps, expected results, and testing frequency —
written in auditor language suitable for a control-testing workpaper.

Output
------
  outputs/test-procedures.md

Run:  python3 sox/test-procedures.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from itgc_catalog import CATALOG_BY_ID  # noqa: E402

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

# control_id -> dict(objective, test_type, sample_approach, steps[], expected_results, frequency)
PROCEDURES = {
    "SOX-ITGC-001": dict(
        objective="Determine whether new user access to in-scope financial systems is "
                   "requested, approved by the appropriate system/data owner, and provisioned "
                   "consistent with the approved request.",
        test_type="Design & Operating Effectiveness",
        sample_approach="Obtain the population of new user access requests processed during "
                         "the period; select 25 items via attribute sampling (or 100% if the "
                         "population is <25).",
        steps=[
            "Obtain the population of new user access requests to in-scope systems for the "
            "period from the ticketing system and agree the population count to a "
            "system-generated report.",
            "Select a sample per the sampling approach above.",
            "For each sample item, obtain the access request and identify the requestor, "
            "the system/data owner approver, and the requested access/role.",
            "Verify the request was approved by an authorized system/data owner prior to "
            "the provisioning date/timestamp.",
            "Verify the access ultimately provisioned in the target system matches the "
            "access approved on the request, with no unapproved scope.",
            "Document any exceptions (missing approval, approval after provisioning, access "
            "broader than approved) for evaluation.",
        ],
        expected_results="100% of sampled access requests are approved by an authorized "
                          "system/data owner prior to provisioning, and provisioned access "
                          "matches the approved request with no unapproved scope.",
        frequency="Quarterly interim testing with a year-end roll-forward covering the "
                   "remaining period.",
    ),
    "SOX-ITGC-002": dict(
        objective="Determine whether access for terminated employees/contractors is disabled "
                   "within the defined SLA, and role-change access no longer required is "
                   "removed.",
        test_type="Design & Operating Effectiveness",
        sample_approach="Obtain the population of terminations during the period from HR/HRIS; "
                         "select 25 items via attribute sampling (or 100% if the population "
                         "is <25).",
        steps=[
            "Obtain the HR termination report for the period and agree population "
            "completeness to the HRIS extract.",
            "Select a sample of terminated users per the sampling approach above.",
            "For each sample item, identify the termination date per HR records.",
            "Obtain the account status/audit log for each in-scope system and identify the "
            "date access was disabled.",
            "Calculate elapsed time between termination date and access-disablement date; "
            "compare to the defined SLA (same business day).",
            "For a sample of role-change users, confirm access no longer required under "
            "the new role was removed.",
            "Document any exceptions exceeding the SLA for evaluation.",
        ],
        expected_results="Access is disabled within the defined SLA for 100% of sampled "
                          "terminations, and role-change access no longer required is removed.",
        frequency="Quarterly interim testing with a year-end roll-forward.",
    ),
    "SOX-ITGC-003": dict(
        objective="Determine whether privileged/administrative access is restricted to "
                   "authorized personnel with documented justification and approval, and is "
                   "subject to enhanced monitoring (MFA, session logging).",
        test_type="Design & Operating Effectiveness",
        sample_approach="Test 100% of the privileged-account population as of a point in "
                         "time, plus a sample of privileged-access grants made during the "
                         "period.",
        steps=[
            "Obtain a system-generated listing of all privileged/admin accounts on each "
            "in-scope system as of a point in time.",
            "Compare the listing to an independently maintained list of personnel "
            "authorized for privileged access and identify any accounts not on the "
            "authorized list.",
            "For a sample of privileged-access grants made during the period, obtain the "
            "request/approval documentation and verify business justification and "
            "system-owner approval predate the grant.",
            "Confirm MFA is enforced for privileged accounts by reviewing IAM/MFA "
            "configuration.",
            "Confirm privileged-session activity is logged by reviewing SIEM/logging "
            "configuration for the relevant systems.",
            "Document any unauthorized or unapproved privileged accounts as exceptions.",
        ],
        expected_results="All privileged accounts are held by authorized personnel with "
                          "documented approval; MFA and session logging are enforced for 100% "
                          "of privileged accounts.",
        frequency="Quarterly.",
    ),
    "SOX-ITGC-004": dict(
        objective="Determine whether user access within in-scope financial systems is free "
                   "of unmitigated segregation-of-duties conflicts.",
        test_type="Design & Operating Effectiveness",
        sample_approach="Run the SoD rule set against the full population of active users in "
                         "each in-scope system (100% population testing via automated rule "
                         "engine); re-perform for a sub-sample to validate rule-engine accuracy.",
        steps=[
            "Obtain the current SoD conflict rule set/matrix and confirm it was reviewed/"
            "approved by the Controller's Office within the last 12 months.",
            "Obtain evidence that the automated SoD conflict analysis was run against the "
            "full population of active users in each in-scope system for the period.",
            "Obtain the resulting conflict report and identify all users flagged with an "
            "unmitigated conflict.",
            "For each flagged conflict, determine whether a documented, monitored "
            "mitigating/compensating control exists and obtain evidence that control "
            "operated.",
            "For conflicts without a documented mitigating control, document as an "
            "exception.",
            "Re-perform the conflict analysis for a sub-sample of users to independently "
            "validate the rule engine's accuracy.",
        ],
        expected_results="All identified SoD conflicts either do not exist or are covered by "
                          "an evidenced, operating mitigating control.",
        frequency="Quarterly.",
    ),
    "SOX-ITGC-005": dict(
        objective="Determine whether periodic user access reviews are performed by the "
                   "appropriate system/data owner, inappropriate access is identified, and "
                   "remediation occurs timely.",
        test_type="Design & Operating Effectiveness",
        sample_approach="Test 100% of in-scope systems' UAR cycles performed during the "
                         "period (typically a small population).",
        steps=[
            "Obtain evidence a UAR was performed for each in-scope system during the "
            "testing period (signed-off access listing or UAR tool export).",
            "Confirm the review was performed by the appropriate system/data owner, not a "
            "peer or subordinate of the reviewed users.",
            "Confirm the reviewed population reconciles to the full user listing for that "
            "system as of the review date.",
            "Identify any access flagged 'remove' during the review and trace to evidence "
            "the access was removed within the defined SLA.",
            "Confirm the completed review is retained with a dated sign-off.",
            "Document any missed reviews, incomplete populations, or untimely remediation "
            "as exceptions.",
        ],
        expected_results="A UAR is completed each quarter for every in-scope system by the "
                          "appropriate owner, and 100% of flagged access is removed within SLA.",
        frequency="Quarterly.",
    ),
    "SOX-ITGC-006": dict(
        objective="Determine whether changes to in-scope financial applications are "
                   "documented, tested in a non-production environment, approved prior to "
                   "migration, and deployed by personnel independent of development.",
        test_type="Design & Operating Effectiveness",
        sample_approach="Obtain the population of production changes to in-scope systems for "
                         "the period; select 25 items via attribute sampling (or 100% if the "
                         "population is <25).",
        steps=[
            "Obtain the change management system's population of production changes to "
            "in-scope financial applications for the period; agree completeness to a "
            "system-generated report.",
            "Select a sample of changes per the sampling approach above.",
            "For each sample item, obtain the change ticket and confirm documented "
            "business/technical justification.",
            "Verify evidence of testing in a non-production environment prior to "
            "deployment.",
            "Verify documented approval from a designated change approver was obtained "
            "prior to the production migration date.",
            "Verify the individual who migrated the change to production is independent "
            "of (did not also author) the change, or that a compensating review occurred.",
            "Document any changes lacking testing evidence, approval, or independent "
            "deployment as exceptions.",
        ],
        expected_results="100% of sampled changes are documented, tested, and approved prior "
                          "to deployment, and deployed with appropriate segregation from "
                          "development.",
        frequency="Quarterly interim testing with a year-end roll-forward.",
    ),
    "SOX-ITGC-007": dict(
        objective="Determine whether emergency changes receive timely retroactive approval "
                   "and are reconciled to the standard change register.",
        test_type="Design & Operating Effectiveness",
        sample_approach="Test 100% of emergency changes during the period given typically low "
                         "volume; apply attribute sampling if volume is high.",
        steps=[
            "Obtain the population of changes flagged 'emergency' in the change management "
            "system for the period.",
            "For each item (or sample), obtain the post-implementation documentation and "
            "identify the retroactive approver and approval timestamp.",
            "Calculate elapsed time from implementation to retroactive approval; compare "
            "to the defined SLA (2 business days).",
            "Confirm the emergency change is logged and reconciled in the standard change "
            "register.",
            "Document any emergency changes lacking retroactive approval, exceeding the "
            "SLA, or missing from the register as exceptions.",
        ],
        expected_results="100% of emergency changes receive retroactive approval within the "
                          "defined SLA and are reconciled to the standard change register.",
        frequency="Quarterly.",
    ),
    "SOX-ITGC-008": dict(
        objective="Determine whether security configurations conform to the approved "
                   "baseline and security event logs are centrally collected and reviewed/"
                   "alerted on a defined cadence.",
        test_type="Design & Operating Effectiveness",
        sample_approach="Test 100% of in-scope systems' current configuration against the "
                         "approved baseline; select a sample of monitoring periods (e.g., 3 "
                         "months) for the log-review component.",
        steps=[
            "Obtain the approved security configuration baseline (password policy, MFA, "
            "session timeout) for in-scope systems.",
            "Obtain the current configuration export for each in-scope system and compare "
            "to the approved baseline; document deviations.",
            "Obtain evidence of the monthly baseline validation for a sample of months "
            "during the period.",
            "Obtain evidence that security event logs (failed logins, privileged activity, "
            "configuration changes) are centrally collected (e.g., SIEM ingestion report).",
            "For a sample of months, obtain evidence that log review/alerting occurred per "
            "the defined cadence and that alerts were triaged/resolved.",
            "Document configuration deviations or missed log reviews as exceptions.",
        ],
        expected_results="Security configurations conform to the approved baseline with no "
                          "unremediated deviations, and log review/alerting occurred each "
                          "period per the defined cadence.",
        frequency="Continuous automated monitoring; sample-based testing performed quarterly.",
    ),
    "SOX-ITGC-009": dict(
        objective="Determine whether scheduled batch jobs supporting in-scope financial "
                   "systems are monitored for completion with failures resolved, and backups "
                   "are executed per schedule and periodically test-restored.",
        test_type="Design & Operating Effectiveness",
        sample_approach="Select a sample of batch job run dates (e.g., 25 across the period) "
                         "and a sample of backup dates; test 100% of periodic restore tests "
                         "performed during the period.",
        steps=[
            "Obtain the population of scheduled batch jobs supporting in-scope financial "
            "systems and the job-monitoring tool's completion log for the period.",
            "Select a sample of run dates and confirm each sampled job completed "
            "successfully or, where it failed, was investigated and resolved with "
            "evidence retained.",
            "Obtain the backup schedule and backup completion logs for in-scope systems; "
            "select a sample of backup dates and confirm successful completion.",
            "Obtain evidence of the quarterly restore test(s) performed during the period "
            "and confirm the restore was successful.",
            "Document any unresolved job failures, missed backups, or failed/skipped "
            "restore tests as exceptions.",
        ],
        expected_results="Sampled batch jobs completed successfully or failures were "
                          "investigated/resolved; backups completed per schedule and the "
                          "periodic restore test was successful.",
        frequency="Daily automated monitoring; sample-based testing performed quarterly; "
                   "restore test performed quarterly.",
    ),
}


def write_markdown(path: str):
    lines = [
        "# SOX ITGC Test Procedures Manual",
        "",
        "*SOX Compliance Package | Confidential - Internal Use*",
        "",
        f"Complete test procedures for all {len(PROCEDURES)} IT General Controls in scope "
        "(see `sox/itgc_catalog.py` for control design detail). Each procedure documents the "
        "test objective, test type, sample-size approach, numbered test steps, expected "
        "results, and testing frequency for use as an audit workpaper template.",
        "",
        "| Control ID | Test Type | Frequency |",
        "|---|---|---|",
    ]
    for cid, proc in PROCEDURES.items():
        lines.append(f"| {cid} | {proc['test_type']} | {proc['frequency']} |")

    lines += ["", "---", ""]
    for cid, proc in PROCEDURES.items():
        ctl = CATALOG_BY_ID[cid]
        lines.append(f"## {cid}: {ctl.title}")
        lines.append("")
        lines.append(f"**Control:** {ctl.description}")
        lines.append("")
        lines.append(f"**Test Objective:** {proc['objective']}")
        lines.append("")
        lines.append(f"**Test Type:** {proc['test_type']}")
        lines.append("")
        lines.append(f"**Sample Size Approach:** {proc['sample_approach']}")
        lines.append("")
        lines.append("**Test Steps:**")
        lines.append("")
        for i, step in enumerate(proc["steps"], start=1):
            lines.append(f"{i}. {step}")
        lines.append("")
        lines.append(f"**Expected Results:** {proc['expected_results']}")
        lines.append("")
        lines.append(f"**Testing Frequency:** {proc['frequency']}")
        lines.append("")
        lines.append("---")
        lines.append("")

    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    md_path = os.path.join(OUT_DIR, "test-procedures.md")
    write_markdown(md_path)
    print(f"Wrote {md_path}")
    print(f"{len(PROCEDURES)} test procedures generated")


if __name__ == "__main__":
    main()
