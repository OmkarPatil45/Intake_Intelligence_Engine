import json
from search.query_engine import (QueryEngine)

class ReviewCLI:
    def __init__(self):
        self.query_engine=(QueryEngine())

    def run(self):
        while True:
            print("\n")
            print("="*60)
            print("INTELLIGENCE REVIEW INTERFACE")
            print("="*60)

            print("1. Search by Keyword")
            print("2. Search by Category")
            print("3. Search by Entity")
            print("4. Search by Source Type")
            print("5. Exit")
            choice=input("\nEnter choice: ").strip()

            if choice=="1":
                keyword = input("Enter keyword: ")
                results = (self.query_engine.search_by_keyword(keyword))
                self.display_results(results)

            elif choice == "2":
                category = input("Enter category: ")
                results = (self.query_engine.search_by_category(category))
                self.display_results(results)

            elif choice == "3":
                entity = input("Enter entity: ")
                results = (self.query_engine.search_by_entity(entity))
                self.display_results(results)

            elif choice == "4":
                source_type = input("Enter source type: ")
                results = (self.query_engine.search_by_source_type(source_type))
                self.display_results(results)

            elif choice == "5":
                print("\nExiting...")
                break

            else:
                print("\nInvalid choice.")

    def display_results(self,results):
        print("\n")
        print("="*60)
        print(f"RESULTS FOUND: " f"{len(results)}")
        print("="*60)
        print(json.dumps(results,indent=4))