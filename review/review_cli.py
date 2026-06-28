import json
from pathlib import Path

from review.menu import Menu
from review.display import Display
from review.search import Search
from review.filters import Filters
from review.exporter import Exporter

from validation.validation_engine import ValidationEngine
from validation.quality_engine import QualityEngine
from validation.batch_validator import BatchValidator
from validation.replay_validator import ReplayValidator


class ReviewCLI:

    def __init__(self):
        self.output_folder = Path("outputs")
        self.validation_engine = ValidationEngine()
        self.quality_engine = QualityEngine()
        self.batch_validator = BatchValidator()
        self.replay_validator = ReplayValidator()

    # ----------------------------------------------------

    def run(self):
        while True:
            Menu.show_main()
            choice = input("\nEnter Choice : ").strip()
            
            if choice == "1":
                self.validate_one_package()

            elif choice == "2":
                self.validate_folder()

            elif choice == "3":
                Search.search_reports()

            elif choice == "4":
                Filters.filter_quality()

            elif choice == "5":
                Filters.failed_reports()

            elif choice == "6":
                self.replay_validation()

            elif choice == "0":
                print("\nExited.")
                break

            else:
                print("\nInvalid Choice.")

    # ----------------------------------------------------

    def validate_one_package(self):
        files = sorted(self.output_folder.glob("*.json"))

        if not files:
            print("\nNo intelligence packages found.")

            return

        print("\nAvailable Packages\n")

        for index, file in enumerate(files, start=1):
            print(f"{index}. {file.name}")

        try:
            selection = int(input("\nSelect Package : "))

            package_file = files[selection - 1]
        except:
            print("\nInvalid Selection.")

            return

        with open(package_file, "r", encoding = "utf-8") as f:
            package = json.load(f)

        validation_report = (
            self.validation_engine.validate(package)
            )

        quality_report = (
            self.quality_engine.generate(validation_report)
        )

        Display.show_validation_summary(validation_report)

        Display.show_quality_report(quality_report)

        base_name = (package_file.stem.replace("_intelligence", ""))

        Exporter.export_report(
            validation_report,
            f"{base_name}_validation_report.json"
        )

        Exporter.export_report(
            quality_report,
            f"{base_name}_quality_report.json"
        )

    # ----------------------------------------------------

    def validate_folder(self):
        batch_report = (self.batch_validator.validate_folder())
       
        Display.show_batch_summary(batch_report)

        Exporter.export_report(batch_report, "batch_report.json")

    def replay_validation(self):
        files = sorted(self.output_folder.glob("*.json"))

        if not files:
            print("\nNo intelligence packages found.")

            return

        print("\nAvailable Packages\n")

        for index, file in enumerate(files, start = 1):
            print(f"{index}. {file.name}")

        try:
            selection = int(input("\nSelect Package : "))

            package_file = files[selection - 1]

        except:
            print("\nInvalid Selection.")

            return

        with open(package_file, "r", encoding = "utf-8") as f:
            package = json.load(f)

        replay_report = (
            self.replay_validator.verify(package)
        )

        print()

        print(json.dumps(
                replay_report,
                indent=4
            )
        )

        Exporter.export_report(replay_report, "replay_report.json")