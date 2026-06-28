class Display:

    @staticmethod
    def show_validation_summary(validation_report):

        summary = validation_report["validation_summary"]

        print("\n" + "=" * 50)
        print("VALIDATION SUMMARY")
        print("=" * 50)

        print(f"Total Checks : {summary['total_checks']}")
        print(f"Passed       : {summary['passed_checks']}")
        print(f"Failed       : {summary['failed_checks']}")
        print(f"Warnings     : {summary['warning_checks']}")

    # ----------------------------------------------------

    @staticmethod
    def show_quality_report(quality_report):
        print("\n" + "=" * 50)
        print("QUALITY REPORT")
        print("=" * 50)

        print(f"Quality Score : {quality_report['quality_score']}")

        print(f"Status        : {quality_report['validation_status']}")

        print(f"Explanation   :")

        print(quality_report["explanation"])

    # ----------------------------------------------------

    @staticmethod
    def show_batch_summary(batch_report):
        summary = batch_report["batch_summary"]

        stats = batch_report[
            "processing_statistics"
        ]

        print("\n" + "=" * 50)
        print("BATCH SUMMARY")
        print("=" * 50)

        print(f"Packages          : {summary['total_packages']}")

        print(f"PASS              : {summary['successful_packages']}")

        print(f"WARNING           : {summary['warning_packages']}")

        print(f"FAIL              : {summary['failed_packages']}")

        print()

        print(f"Average Quality   : {stats['average_quality_score']}")

        print(f"Highest Quality   : {stats['highest_quality_score']}")

        print(f"Lowest Quality    : {stats['lowest_quality_score']}")