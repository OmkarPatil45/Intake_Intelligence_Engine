"""
Verifies deterministic behaviour of the
Universal Intelligence Validation Framework.
"""

import json

from validation.validation_engine import ValidationEngine
from validation.quality_engine import QualityEngine


class ReplayValidator:

    def __init__(self, replay_count=3):
        self.replay_count = replay_count
        self.validation_engine = ValidationEngine()
        self.quality_engine = QualityEngine()

    # ---------------------------------------------------------

    def verify(self, package: dict):
        validation_reports = []
        quality_reports = []

        for _ in range(self.replay_count):
            validation_report = (self.validation_engine.validate(package))

            quality_report = (self.quality_engine.generate(validation_report))

            validation_reports.append(validation_report)

            quality_reports.append(quality_report)

        return self._build_report(validation_reports,quality_reports)

    # ---------------------------------------------------------

    def _build_report(self,validation_reports,quality_reports):
        validation_stable = all(
            report == validation_reports[0]
            for report in validation_reports
        )

        quality_stable = all(
            report == quality_reports[0]
            for report in quality_reports
        )

        quality_scores = [
            report["quality_score"]
            for report in quality_reports
        ]

        status = (
            "PASS"
            if validation_stable
            and quality_stable

            else "FAIL"
        )

        explanation = (
            "Replay verification successful."
            if status == "PASS"
            else
            "Validation results changed across executions."
        )

        return {
            "replay_count": self.replay_count,
            "validation_reports_identical": validation_stable,
            "quality_reports_identical": quality_stable,
            "quality_scores": quality_scores,
            "overall_status": status,
            "explanation": explanation
        }