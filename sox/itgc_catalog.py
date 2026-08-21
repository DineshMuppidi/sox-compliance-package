"""
IT General Controls (ITGC) Catalog — SOX Compliance Package
================================================================
Single source of truth for this organization's SOX-scoped IT General
Controls (prefix ``SOX-ITGC-###``). Every other script in this package
(COSO mapping, test procedures, evidence matrix, control-design workbook)
imports from here rather than redefining control IDs locally, so a single
control stays traceable across the whole package.

Domains covered map to the four ITGC areas most relevant to a SOX ICFR
(Internal Control over Financial Reporting) scope: Access Management /
Authorization, Segregation of Duties, Access Reviews, Change Management,
and Monitoring (Computer Operations).
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ITGC:
    control_id: str
    title: str
    domain: str              # Access Management / Segregation of Duties / Access Reviews / Change Management / Monitoring
    description: str
    control_owner: str
    control_type: str        # Preventive / Detective / Corrective (may be combined, e.g. "Detective/Corrective")
    frequency: str            # Continuous / Daily / Monthly / Quarterly / Annual
    automation: str           # Automated / IT-Dependent Manual / Manual
    risk_rating: str          # Low / Medium / High / Critical
    coso_principles: list = field(default_factory=list)   # COSO 2013 principle IDs, e.g. ["P3", "P5"]
    itgc_domain_tag: str = "Authorization"                 # Authorization / Change Management / Access Reviews / Monitoring


CATALOG: list[ITGC] = [
    ITGC(
        "SOX-ITGC-001", "User Access Provisioning (New Hire / Role Change)",
        "Access Management",
        "New user access to in-scope financial systems (ERP, general ledger, sub-ledgers) is "
        "requested via a documented access request, approved by the system or data owner prior "
        "to provisioning, and provisioned by IT strictly in accordance with the approved request.",
        "IT Security / IAM Team", "Preventive", "Continuous (event-driven)", "IT-Dependent Manual",
        "High", ["P3", "P5", "P10", "P11"], "Authorization",
    ),
    ITGC(
        "SOX-ITGC-002", "User Access Deprovisioning (Termination / Role Change)",
        "Access Management",
        "Access for terminated employees and contractors is disabled within a defined SLA (same "
        "business day) of the termination date received from HR, and access for employees "
        "changing roles is adjusted to remove entitlements no longer required.",
        "IT Security / IAM Team", "Preventive", "Continuous (event-driven)", "IT-Dependent Manual",
        "Critical", ["P3", "P5", "P10", "P11"], "Authorization",
    ),
    ITGC(
        "SOX-ITGC-003", "Privileged / Administrative Access Management",
        "Access Management",
        "Access to privileged accounts (admin, DBA, superuser) on in-scope systems is restricted "
        "to authorized personnel, requires documented business justification and system-owner "
        "approval, and is subject to enhanced monitoring including MFA and session logging.",
        "IT Security", "Preventive", "Continuous", "Manual",
        "Critical", ["P3", "P5", "P10", "P11"], "Authorization",
    ),
    ITGC(
        "SOX-ITGC-004", "Segregation of Duties (SoD) — Financial Systems",
        "Segregation of Duties",
        "Access rights within in-scope financial applications are configured and periodically "
        "analyzed to prevent an individual user from holding conflicting access (e.g., create and "
        "approve a vendor, or post and approve a journal entry) without a documented, monitored "
        "mitigating control.",
        "IT Security / Controller's Office", "Preventive/Detective", "Quarterly", "IT-Dependent Manual",
        "High", ["P3", "P8", "P10", "P11"], "Authorization",
    ),
    ITGC(
        "SOX-ITGC-005", "Periodic User Access Review (UAR)",
        "Access Reviews",
        "System and data owners formally review the population of users with access to in-scope "
        "financial systems on a quarterly basis, confirm continued business need, and any "
        "inappropriate access identified is revoked within a defined SLA; the review and any "
        "remediation are evidenced and signed off.",
        "Business System Owners / IT Security", "Detective", "Quarterly", "Manual",
        "High", ["P5", "P16", "P17"], "Access Reviews",
    ),
    ITGC(
        "SOX-ITGC-006", "Program / Application Change Management",
        "Change Management",
        "Changes to in-scope financial applications and supporting infrastructure (code, "
        "configuration, interfaces) are documented, tested in a non-production environment, "
        "approved by a designated change approver, and migrated to production only by personnel "
        "without conflicting development access.",
        "IT Change Management / Application Development", "Preventive", "Continuous (per release)",
        "IT-Dependent Manual", "High", ["P7", "P9", "P10", "P11", "P12"], "Change Management",
    ),
    ITGC(
        "SOX-ITGC-007", "Emergency Change Management",
        "Change Management",
        "Emergency changes that bypass the standard change process require post-implementation "
        "documentation and retroactive approval by a designated approver within a defined SLA "
        "(2 business days), and are logged and reconciled against the standard change register.",
        "IT Change Management", "Detective/Corrective", "Continuous (event-driven)", "Manual",
        "Medium", ["P9", "P10", "P16"], "Change Management",
    ),
    ITGC(
        "SOX-ITGC-008", "Security Configuration & Log Monitoring",
        "Monitoring",
        "Security configurations (password policy, MFA, session timeout) on in-scope systems are "
        "set per an approved baseline and periodically validated; security event logs (failed "
        "logins, privileged activity, configuration changes) are centrally collected and "
        "reviewed/alerted on a defined cadence.",
        "IT Security / SOC", "Detective", "Continuous monitoring / Monthly baseline validation",
        "Automated", "Medium", ["P11", "P16", "P17"], "Monitoring",
    ),
    ITGC(
        "SOX-ITGC-009", "Batch Job & Backup Monitoring (Computer Operations)",
        "Monitoring",
        "Scheduled batch jobs (interfaces, financial close processes) supporting in-scope "
        "financial systems are monitored for successful completion, with failures investigated, "
        "resolved, and logged; backups are executed per schedule and periodically test-restored "
        "to confirm recoverability.",
        "IT Operations", "Detective", "Daily (job monitoring) / Quarterly (restore test)",
        "Automated / IT-Dependent Manual", "Medium", ["P11", "P16"], "Monitoring",
    ),
]

CATALOG_BY_ID: dict[str, ITGC] = {c.control_id: c for c in CATALOG}

DOMAINS = ["Access Management", "Segregation of Duties", "Access Reviews", "Change Management", "Monitoring"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
RISK_SCORE = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}
IMPLEMENTATION_STATUSES = ["Not Started", "Planned", "In Progress", "Implemented", "Not Applicable"]


def controls(*ids: str) -> list[ITGC]:
    """Look up catalog controls by ID, preserving the order given."""
    return [CATALOG_BY_ID[i] for i in ids]


def control_titles(*ids: str) -> str:
    return "; ".join(f"{i} — {CATALOG_BY_ID[i].title}" for i in ids)


if __name__ == "__main__":
    print(f"{len(CATALOG)} IT General Controls in catalog")
    for d in DOMAINS:
        n = sum(1 for c in CATALOG if c.domain == d)
        print(f"  {d}: {n}")
