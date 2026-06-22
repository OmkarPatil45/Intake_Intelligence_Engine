import json
from pathlib import Path


class RelationshipEngine:
    """
    Detects relationships between
    intelligence packages.
    """

    def build_graph(self, documents: list):
        nodes = []
        relationships = []

        for document in documents:
            nodes.append({
                "id": document["file_name"],
                "type": "document"})

        for i in range(len(documents)):
            for j in range(i + 1, len(documents)):
                doc_a = documents[i]
                doc_b = documents[j]

                relationships.extend(self._compare_documents(doc_a, doc_b))

        return {
            "nodes": nodes, "relationships": relationships
        }

    def _compare_documents(self, doc_a, doc_b):
        relationships = []

        relationship_rules = {
            "names": "same_person",
            "organizations": "same_organization",
            "technologies": "same_technology",
            "projects": "same_project"
        }

        entities_a = (doc_a.get("entities", {}))

        entities_b = (doc_b.get("entities", {}))

        for entity_group, relation_type in (relationship_rules.items()):
            values_a = set(entities_a.get(entity_group, []))

            values_b = set(entities_b.get(entity_group, []))

            shared_values = (values_a &values_b)
            for entity in (shared_values): relationships.append({
                    "source": doc_a["file_name"],
                    "target": doc_b["file_name"],
                    "relationship": relation_type,
                    "entity": entity
                })

        return relationships

    def build_from_outputs(self,output_folder="outputs"):
        documents = []
        output_path = Path(output_folder)
        for file in output_path.glob("*.json"):

            if (file.name == "relationship_graph.json"):
                continue

            try:
                with open(file, "r", encoding="utf-8") as f:
                    package = (json.load(f))
                
                documents.append({
                    "file_name": package["metadata"]["file_name"],

                    "entities": package.get("entities",{})})

            except Exception: 
                pass

        graph = (self.build_graph(documents))

        with open(
            output_path /
            "relationship_graph.json",
            "w",
            encoding="utf-8"
        ) as f:
            
            json.dump(graph, f, indent=4)

        return graph