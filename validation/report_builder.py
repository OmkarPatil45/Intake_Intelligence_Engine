"""
Creates standardized validation results.
Every validator should use this helper to
produce consistent reports.
"""


class ReportBuilder:

    @staticmethod
    def build_result(
        rule: str,
        status: str,
        target: str,
        message: str,
        severity: str
    ) -> dict:

        return {
            "rule": rule,
            "status": status,
            "target": target,
            "message": message,
            "severity": severity
        }