import json
from pathlib import Path

from validation.validation_engine import ValidationEngine
from validation.quality_engine import QualityEngine


class Search:
    OUTPUT_FOLDER = Path("outputs")

    @classmethod
    def search_reports(cls):
        keyword = input("\nEnter file name keyword : ").strip().lower()

        files = sorted(
            cls.OUTPUT_FOLDER.glob("*.json")
        )

        found = False

        for file in files:
            if keyword not in file.name.lower():
                continue

            found = True

            with open(file, "r", encoding = "utf-8") as f:
                package = json.load(f)

            validation = (ValidationEngine().validate(package))

            quality = (QualityEngine().generate(validation))

            print("\n" + "=" * 50)

            print(f"File : {file.name}")

            print(f"Status : {quality['validation_status']}")

            print(f"Quality : {quality['quality_score']}")

        if not found:
            print("\nNo matching reports found.")