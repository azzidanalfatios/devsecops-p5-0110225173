import json
import sys
from pathlib import Path


report_path = Path("bandit-report.json")

if not report_path.exists():
    print("QUALITY GATE FAILED: Laporan Bandit tidak ditemukan.")
    sys.exit(1)

report = json.loads(report_path.read_text(encoding="utf-8"))

high_findings = [
    finding
    for finding in report.get("results", [])
    if finding.get("issue_severity", "").upper() == "HIGH"
]

if high_findings:
    print(f"QUALITY GATE FAILED: {len(high_findings)} temuan HIGH.")

    for finding in high_findings:
        print(
            f"{finding.get('filename')}:{finding.get('line_number')} "
            f"- {finding.get('issue_text')}"
        )

    sys.exit(1)

print("QUALITY GATE PASSED: Tidak ditemukan temuan HIGH.")