"""
consistency_validator.py

Validates logical consistency of an
Intelligence Package.
"""

from validation.report_builder import ReportBuilder

from validation.utils import (safe_get,count_entities,has_duplicates)


class ConsistencyValidator:
    def validate(self, package: dict) -> dict:

        results = []

        results.extend(self._validate_duplicate_entities(package))
        results.extend(self._validate_entity_consistency(package))
        results.extend(self._validate_classification(package))
        results.extend(self._validate_confidence(package))
        results.extend(self._validate_evidence(package))
        results.extend(self._validate_processing_trace(package))

        passed = sum(
            1
            for item in results
            if item["status"] == "PASS"
        )

        failed = sum(
            1
            for item in results
            if item["status"] == "FAIL"
        )

        warnings = sum(
            1
            for item in results
            if item["status"] == "WARNING"
        )

        return {
            "validator": "Consistency Validator",
            "total_checks": len(results),
            "passed_checks": passed,
            "failed_checks": failed,
            "warning_checks": warnings,
            "results": results
        }

    # -----------------------------------------------------

    def _validate_duplicate_entities(self,package: dict):
        results = []

        entities = safe_get(package,"entities",{})

        for entity_type, values in entities.items():
            if has_duplicates(values):
                results.append(
                    ReportBuilder.build_result(
                        rule="Duplicate Entity Check",
                        status="FAIL",
                        target=entity_type,
                        message="Duplicate entities detected.",
                        severity="ERROR"
                    )
                )

            else:
                results.append(ReportBuilder.build_result(
                        rule="Duplicate Entity Check",
                        status="PASS",
                        target=entity_type,
                        message="No duplicate entities.",
                        severity="INFO"
                    )
                )

        return results

    # -----------------------------------------------------

    def _validate_entity_consistency(self,package: dict):
        results = []

        entities = safe_get(package,"entities",{})

        entity_count = count_entities(entities)

        if entity_count == 0:
            results.append(
                ReportBuilder.build_result(
                    rule="Entity Consistency",
                    status="FAIL",
                    target="entities",
                    message="No entities found.",
                    severity="ERROR"
                )
            )

        else:
            results.append(ReportBuilder.build_result(
                    rule="Entity Consistency",
                    status="PASS",
                    target="entities",
                    message=f"{entity_count} entities found.",
                    severity="INFO"
                )
            )

        return results

    # -----------------------------------------------------

    def _validate_classification(self,package: dict):
        results = []

        primary = safe_get(package,"classification.primary_category")

        if primary:
            results.append(ReportBuilder.build_result(
                    rule="Classification Consistency",
                    status="PASS",
                    target="classification.primary_category",
                    message=f"Primary category: {primary}",
                    severity="INFO"
                )
            )

        else:
            results.append(ReportBuilder.build_result(
                    rule="Classification Consistency",
                    status="FAIL",
                    target="classification.primary_category",
                    message="Primary category missing.",
                    severity="ERROR"
                )
            )

        return results

    # -----------------------------------------------------

    def _validate_confidence(self,package: dict):
        results = []

        score = safe_get(package,"confidence.score")

        if score is None:
            results.append(ReportBuilder.build_result(
                    rule="Confidence Check",
                    status="FAIL",
                    target="confidence.score",
                    message="Confidence score missing.",
                    severity="ERROR"
                )
            )

            return results

        if 0 <= score <= 100:
            results.append(ReportBuilder.build_result(
                    rule="Confidence Check",
                    status="PASS",
                    target="confidence.score",
                    message=f"Confidence score: {score}",
                    severity="INFO"
                )
            )
        else:
            results.append(ReportBuilder.build_result(
                    rule="Confidence Check",
                    status="FAIL",
                    target="confidence.score",
                    message="Confidence score out of range.",
                    severity="ERROR"
                )
            )

        return results

    # -----------------------------------------------------

    def _validate_evidence(self,package: dict):

        results = []

        evidence = safe_get(package,"evidence_report",{})

        if evidence:

            results.append(
                ReportBuilder.build_result(
                    rule="Evidence Check",
                    status="PASS",
                    target="evidence_report",
                    message=f"{len(evidence)} evidence records found.",
                    severity="INFO"
                )
            )

        else:
            results.append(ReportBuilder.build_result(
                    rule="Evidence Check",
                    status="WARNING",
                    target="evidence_report",
                    message="Evidence report is empty.",
                    severity="WARNING"
                )
            )

        return results

    # -----------------------------------------------------

    def _validate_processing_trace(self,package: dict):

        results = []

        trace = safe_get(package,"processing_trace.processing_trace",[])

        if len(trace) >= 5:

            results.append(ReportBuilder.build_result(
                    rule="Processing Trace",
                    status="PASS",
                    target="processing_trace",
                    message=f"{len(trace)} processing steps found.",
                    severity="INFO"
                )
            )

        else:
            results.append(ReportBuilder.build_result(
                    rule="Processing Trace",
                    status="WARNING",
                    target="processing_trace",
                    message="Processing trace seems incomplete.",
                    severity="WARNING"
                )
            )

        return results