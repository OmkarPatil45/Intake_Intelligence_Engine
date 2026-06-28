"""
Generates deterministic quality assessment
from validation results.
"""

from validation.validation_rules import (QUALITY_THRESHOLDS, SUGGESTION_RULES)


class QualityEngine:
    def generate(self, validation_report: dict) -> dict:
        summary = validation_report["validation_summary"]
        passed = summary["passed_checks"]
        failed = summary["failed_checks"]
        warnings = summary["warning_checks"]
        total = summary["total_checks"]
        score = round((passed / max(total, 1)) * 100)
        status = self._determine_status(score)
        errors = []
        warning_list = []
        suggestions = set()

        for validator in validation_report["validator_reports"]:
            for result in validator["results"]:

                if result["status"] == "FAIL":
                    errors.append(result)

                    suggestion = (SUGGESTION_RULES.get(result["rule"]))

                    if suggestion:
                        suggestions.add(suggestion)

                elif result["status"] == "WARNING":
                    warning_list.append(result)
                    suggestion = (SUGGESTION_RULES.get(result["rule"]))

                    if suggestion:
                        suggestions.add(suggestion)

        explanation = (
            f"The package passed "
            f"{passed} of {total} "
            f"validation checks. "
            f"{failed} failed and "
            f"{warnings} produced warnings."
        )

        return {
            "quality_score": score,
            "validation_status": status,
            "errors": errors,
            "warnings": warning_list,
            "improvement_suggestions": sorted(list(suggestions)),
            "explanation": explanation
        }

    # -----------------------------------------------------

    def _determine_status(self,score: int):
        if score >= QUALITY_THRESHOLDS["PASS"]:
            return "PASS"

        if score >= QUALITY_THRESHOLDS["WARNING"]:
            return "WARNING"

        return "FAIL"