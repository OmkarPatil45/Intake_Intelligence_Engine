"""
schema_validator.py

Validates the structural integrity of an
intelligence package.

Does NOT validate business logic.
"""

from validation.validation_rules import (REQUIRED_FIELDS,EXPECTED_TYPES)

from validation.report_builder import ReportBuilder


class SchemaValidator:
    def validate(self, package: dict) -> dict:
        """
        Perform schema validation.
        """

        results = []

        results.extend(self._validate_required_fields(package))

        results.extend(self._validate_data_types(package))

        results.extend(self._validate_empty_values(package))

        passed = sum(
            1 for item in results
            if item["status"] == "PASS"
        )

        failed = sum(
            1 for item in results
            if item["status"] == "FAIL"
        )

        return {
            "validator": "Schema Validator",
            "total_checks": len(results),
            "passed_checks": passed,
            "failed_checks": failed,
            "results": results
        }

    # -----------------------------------------------------

    def _validate_required_fields(self,package: dict):

        results = []

        for field in REQUIRED_FIELDS:
            if field in package:

                results.append(ReportBuilder.build_result(
                        rule="Required Field Check",
                        status="PASS",
                        target=field,
                        message="Required field present.",
                        severity="INFO"
                    )
                )

            else:
                results.append(ReportBuilder.build_result(
                        rule="Required Field Check",
                        status="FAIL",
                        target=field,
                        message="Required field missing.",
                        severity="ERROR"
                    )
                )

        return results

    # -----------------------------------------------------

    def _validate_data_types(self,package: dict):

        results = []

        for field, expected_type in EXPECTED_TYPES.items():

            if field not in package:
                continue

            actual_value = package[field]

            if isinstance(actual_value,expected_type):

                results.append(ReportBuilder.build_result(
                        rule="Data Type Check",
                        status="PASS",
                        target=field,
                        message=f"Correct type ({expected_type.__name__}).",
                        severity="INFO"
                    )
                )

            else:
                results.append(ReportBuilder.build_result(
                        rule="Data Type Check",
                        status="FAIL",
                        target=field,
                        message=(
                            f"Expected {expected_type.__name__}, "
                            f"received {type(actual_value).__name__}."
                        ),

                        severity="ERROR"
                    )
                )

        return results

    # -----------------------------------------------------

    def _validate_empty_values(self,package: dict):

        results = []
        for field in REQUIRED_FIELDS:
            if field not in package:
                continue
            value = package[field]
            is_empty = (
                value is None

                or value == ""

                or value == []

                or value == {}

            )

            if is_empty:
                results.append(ReportBuilder.build_result(
                        rule="Empty Value Check",
                        status="FAIL",
                        target=field,
                        message="Field is empty.",
                        severity="WARNING"
                    )
                )

            else:
                results.append(ReportBuilder.build_result(
                        rule="Empty Value Check",
                        status="PASS",
                        target=field,
                        message="Field contains data.",
                        severity="INFO"
                    )
                )

        return results