"""
Validates an entire directory of intelligence
packages and generates an aggregate report.
"""

from pathlib import Path
import json

from validation.validation_engine import ValidationEngine
from validation.quality_engine import QualityEngine


class BatchValidator:
    def __init__(self, output_folder="outputs"):
        self.output_folder = Path(output_folder)
        self.validation_engine = ValidationEngine()
        self.quality_engine = QualityEngine()

    # ---------------------------------------------------------

    def validate_folder(self):
        packages = self._load_packages()
        package_reports = []

        for package in packages:
            validation_report = (self.validation_engine.validate(package))

            quality_report = (self.quality_engine.generate(validation_report))

            package_reports.append({
                "file_name":
                    package.get("metadata",{}).get("file_name","Unknown"),

                "validation_status": quality_report["validation_status"],

                "quality_score": quality_report["quality_score"],

                "passed_checks": validation_report["validation_summary"]["passed_checks"],

                "failed_checks": validation_report["validation_summary"]["failed_checks"]
            })

        return {
            "batch_summary": self._build_summary(package_reports),

            "processing_statistics": self._build_statistics(package_reports),

            "package_reports": package_reports
        }

    # ---------------------------------------------------------

    def _load_packages(self):
        packages = []

        for file in self.output_folder.glob("*.json"):
            try:
                with open(file, "r", encoding = "utf-8") as f:
                    data = json.load(f)

                    if isinstance(data, dict):
                        packages.append(data)

            except Exception:
                pass

        return packages

    # ---------------------------------------------------------

    def _build_summary(self,package_reports):

        total_packages = len(package_reports)

        successful_packages = sum(
            1

            for report in package_reports

            if report["validation_status"] == "PASS")

        warning_packages = sum(
            1

            for report in package_reports

            if report["validation_status"] == "WARNING")

        failed_packages = sum(
            1

            for report in package_reports

            if report["validation_status"] == "FAIL")

        return {
            "total_packages": total_packages,
            "successful_packages":successful_packages,
            "warning_packages":warning_packages,
            "failed_packages":failed_packages
        }

    # ---------------------------------------------------------

    def _build_statistics(self,package_reports):
        if not package_reports:

            return {
                "average_quality_score": 0,
                "highest_quality_score": 0,
                "lowest_quality_score": 0,
                "average_passed_checks": 0
            }

        quality_scores = [
            report["quality_score"]
            for report in package_reports

        ]

        passed_checks = [
            report["passed_checks"]
            for report in package_reports
        ]

        return {
            "average_quality_score": round(sum(quality_scores) / len(quality_scores),2),

            "highest_quality_score":max(quality_scores),

            "lowest_quality_score":min(quality_scores),

            "average_passed_checks": round(sum(passed_checks)/ len(passed_checks),2)
        }