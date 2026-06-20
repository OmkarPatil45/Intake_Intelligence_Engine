import json
from pathlib import Path
from search.query_engine import QueryEngine


class ReviewCLI:

    def __init__(self):

        self.query_engine = QueryEngine()

        self.output_folder = Path(
            "outputs"
        )

    def run(self):

        while True:

            print("\n")
            print("=" * 60)
            print("EXPLAINABLE INTELLIGENCE DASHBOARD")
            print("=" * 60)

            print("1. List Documents")
            print("2. View Document Intelligence")
            print("3. Search Intelligence")
            print("4. View Relationship Graph")
            print("5. Exit")

            choice = input(
                "\nEnter choice: "
            ).strip()

            if choice == "1":

                self.list_documents()

            elif choice == "2":

                self.view_document()

            elif choice == "3":

                self.search_menu()

            elif choice == "4":

                self.view_relationships()

            elif choice == "5":

                print("\nExiting...")
                break

            else:

                print(
                    "\nInvalid choice."
                )

    def list_documents(self):

        print("\n")
        print("=" * 60)
        print("AVAILABLE DOCUMENTS")
        print("=" * 60)

        documents = self._get_documents()

        for index, document in enumerate(
            documents,
            start=1
        ):

            print(
                f"{index}. {document}"
            )

    def view_document(self):

        documents = (
            self._get_documents()
        )

        if not documents:

            print(
                "\nNo documents available."
            )
            return

        print("\n")

        for index, document in enumerate(
            documents,
            start=1
        ):

            print(
                f"{index}. {document}"
            )

        choice = input(
            "\nSelect document: "
        )

        try:

            selected_document = (
                documents[
                    int(choice) - 1
                ]
            )

        except Exception:

            print(
                "\nInvalid selection."
            )

            return

        package = (
            self._load_document(
                selected_document
            )
        )

        if not package:

            print(
                "\nUnable to load document."
            )

            return

        self._display_document(
            package
        )

    def search_menu(self):

        print("\n")
        print("=" * 60)
        print("SEARCH")
        print("=" * 60)

        print("1. Entity")
        print("2. Technology")
        print("3. Organization")
        print("4. Classification")
        print("5. Confidence")

        choice = input(
            "\nEnter choice: "
        ).strip()

        results = []

        if choice == "1":

            query = input(
                "Entity: "
            )

            results = (
                self.query_engine
                .search_by_entity(
                    query
                )
            )

        elif choice == "2":

            query = input(
                "Technology: "
            )

            results = (
                self.query_engine
                .search_by_technology(
                    query
                )
            )

        elif choice == "3":

            query = input(
                "Organization: "
            )

            results = (
                self.query_engine
                .search_by_organization(
                    query
                )
            )

        elif choice == "4":

            query = input(
                "Classification: "
            )

            results = (
                self.query_engine
                .search_by_classification(
                    query
                )
            )

        elif choice == "5":

            score = int(
                input(
                    "Minimum Score: "
                )
            )

            results = (
                self.query_engine
                .search_by_confidence(
                    score
                )
            )

        print("\n")
        print("=" * 60)
        print(
            f"RESULTS FOUND: "
            f"{len(results)}"
        )
        print("=" * 60)

        for package in results:

            print(
                package.get(
                    "metadata",
                    {}
                ).get(
                    "file_name"
                )
            )

    def view_relationships(self):

        relationship_file = (
            self.output_folder
            /
            "relationship_graph.json"
        )

        if not (
            relationship_file.exists()
        ):

            print(
                "\nRelationship graph not found."
            )

            return

        with open(
            relationship_file,
            "r",
            encoding="utf-8"
        ) as f:

            graph = json.load(f)

        print("\n")
        print("=" * 60)
        print("RELATIONSHIPS")
        print("=" * 60)

        for relationship in (
            graph.get(
                "relationships",
                []
            )
        ):

            print(
                f"{relationship['source']} "
                f"--[{relationship['relationship']}]--> "
                f"{relationship['target']} "
                f"({relationship['entity']})"
            )

    def _display_document(
        self,
        package
    ):

        print("\n")
        print("=" * 60)
        print("DOCUMENT INTELLIGENCE")
        print("=" * 60)

        print(
            "File:",
            package["metadata"][
                "file_name"
            ]
        )

        print(
            "Category:",
            package[
                "classification"
            ][
                "primary_category"
            ]
        )

        print(
            "Confidence:",
            package[
                "confidence"
            ][
                "score"
            ]
        )

        print("\n")
        print("=" * 60)
        print("ENTITIES")
        print("=" * 60)

        for entity_type, values in (
            package[
                "entities"
            ].items()
        ):

            print(
                f"{entity_type}: "
                f"{len(values)}"
            )

        print("\n")
        print("=" * 60)
        print("REJECTED ENTITIES")
        print("=" * 60)

        print(
            len(
                package.get(
                    "rejected_entities",
                    []
                )
            )
        )

        print("\n")
        print("=" * 60)
        print("CLASSIFICATION REASONING")
        print("=" * 60)

        print(
            package[
                "classification"
            ].get(
                "classification_explanation"
            )
        )

        print("\n")
        print("=" * 60)
        print("CONFIDENCE EXPLANATION")
        print("=" * 60)

        print(
            package[
                "confidence"
            ].get(
                "explanation"
            )
        )

        print("\n")
        print("=" * 60)
        print("EVIDENCE SUMMARY")
        print("=" * 60)

        print(
            f"{len(package.get('evidence_report', {}))} "
            f"entities have supporting evidence."
        )

    def _get_documents(self):

        documents = []

        for file in (
            self.output_folder.glob(
                "*.json"
            )
        ):

            if (
                file.name
                ==
                "relationship_graph.json"
            ):
                continue

            documents.append(
                file.name
            )

        return sorted(
            documents
        )

    def _load_document(
        self,
        file_name
    ):

        try:

            with open(
                self.output_folder /
                file_name,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except Exception:

            return None