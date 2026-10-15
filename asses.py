
import json
from pathlib import Path
from datetime import datetime, timezone

CONFIG_FILE = Path("security_config.json")
REPORT_FILE = Path("assessment_report.json")


def check_config(config):
    findings = []

    checks = [
        (
            "DEBUG_MODE",
            config.get("debug_mode") is True,
            "Disable debug mode in production."
        ),
        (
            "HTTPS_DISABLED",
            config.get("https_enabled") is False,
            "Enable HTTPS for network traffic."
        ),
        (
            "WEAK_PASSWORD_POLICY",
            config.get("minimum_password_length", 0) < 12,
            "Set a minimum password length of at least 12 characters."
        ),
        (
            "SECURITY_LOGGING_DISABLED",
            config.get("security_logging") is False,
            "Enable security event logging."
        ),
        (
            "DEPENDENCIES_UNREVIEWED",
            config.get("dependencies_reviewed") is False,
            "Review and update dependencies using trusted sources."
        )
    ]

    for rule, failed, remediation in checks:
        findings.append({
            "rule": rule,
            "status": "FINDING" if failed else "PASS",
            "severity": "Medium" if failed else "Informational",
            "evidence": (
                "The supplied configuration does not meet the check."
                if failed else
                "The supplied configuration meets the check."
            ),
            "remediation": remediation if failed else "No action required."
        })

    return findings


def main():
    if not CONFIG_FILE.exists():
        print("Missing security_config.json")
        print("Create the configuration file using the README example.")
        return

    try:
        config = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        print(f"Unable to read configuration: {error}")
        return

    findings = check_config(config)

    report = {
        "assessment": "Ethical Security Configuration Review",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "scope": "Supplied configuration only; no external system tested.",
        "summary": {
            "checks": len(findings),
            "findings": sum(
                item["status"] == "FINDING" for item in findings
            ),
            "passes": sum(
                item["status"] == "PASS" for item in findings
            )
        },
        "results": findings
    }

    REPORT_FILE.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8"
    )

    print(json.dumps(report["summary"], indent=2))
    print(f"Report saved to {REPORT_FILE}")


if __name__ == "__main__":
    main()
