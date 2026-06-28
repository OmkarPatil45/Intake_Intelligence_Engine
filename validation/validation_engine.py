"""
Central orchestrator for the
Universal Intelligence Validation Framework
Does NOT contain validation logic.
"""

from validation.schema_validator import SchemaValidator
from validation.consistency_validator import ConsistencyValidator


class ValidationEngine:

    def __init__(self):
# Registered Validators
        self.validators = [SchemaValidator(),ConsistencyValidator()]

    # -----------------------------------------------------

    def validate(self,package: dict) -> dict:

        validator_reports = []

        total_checks = 0

        passed_checks = 0

        failed_checks = 0

        warning_checks = 0

        for validator in self.validators:

            report = validator.validate(package)

            validator_reports.append(report)

            total_checks += report.get("total_checks",0)

            passed_checks += report.get("passed_checks",0)

            failed_checks += report.get("failed_checks",0)

            warning_checks += report.get("warning_checks",0)

        return {
            "validation_summary": {
                "total_checks": total_checks,
                "passed_checks": passed_checks,
                "failed_checks": failed_checks,
                "warning_checks": warning_checks
            },

            "validator_reports": validator_reports

        }