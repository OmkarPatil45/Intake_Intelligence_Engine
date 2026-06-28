import json
from pathlib import Path

from validation.validation_engine import ValidationEngine
from validation.quality_engine import QualityEngine


class Filters:
    OUTPUT_FOLDER = Path("outputs")

    # ---------------------------------------------

    @classmethod
    def filter_quality(cls):
        try:
            score = int(input("\nMinimum Quality Score : "))

        except:
            print("\nInvalid score.")

            return

        files = sorted(cls.OUTPUT_FOLDER.glob("*.json"))

        print()

        for file in files:
            with open(file, "r", encoding = "utf-8") as f:

                package = json.load(f)

            validation = (ValidationEngine().validate(package))

            quality = (QualityEngine().generate(validation))

            if quality["quality_score"] >= score:

                print(
                    f"{file.name}"
                    f"  -> "
                    f"{quality['quality_score']}"
                )

    # ---------------------------------------------

    @classmethod
    def failed_reports(cls):
        files = sorted(cls.OUTPUT_FOLDER.glob("*.json"))

        print()

        found = False

        for file in files:
            with open(file, "r", encoding = "utf-8") as f:

                package = json.load(f)

            validation = (ValidationEngine().validate(package))

            quality = (QualityEngine().generate(validation))

            if quality["validation_status"] == "FAIL":

                found = True

                print(
                    f"{file.name}"
                    f"  -> "
                    f"{quality['quality_score']}"
                )

        if not found:
            print("No failed reports.")