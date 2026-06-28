"""
Exports framework reports to JSON.
"""

import json
from pathlib import Path


class Exporter:

    REPORT_FOLDER = Path("validation_reports")

    @classmethod
    def _ensure_folder(cls):

        cls.REPORT_FOLDER.mkdir(
            exist_ok=True
        )

    # -------------------------------------------------

    @classmethod
    def export_report(cls, report: dict, file_name: str):

        cls._ensure_folder()

        output_path = (cls.REPORT_FOLDER / file_name)

        with open(output_path, "w", encoding = "utf-8") as file:

            json.dump(report, file, indent=4)

        print(f" {file_name} exported.")