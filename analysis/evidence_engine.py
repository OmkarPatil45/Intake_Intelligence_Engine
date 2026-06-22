import re


class EvidenceEngine:
    """
    Generates explainable evidence
    for extracted entities.
    """

    def generate(self,text: str,entities: dict):
        evidence_report = {}

        paragraphs = [
            p.strip()
            for p in text.split("\n")
            if p.strip()
        ]

        for entity_group, values in entities.items():
            for entity in values:
                entity_evidence = []
                for paragraph_index, paragraph in enumerate(paragraphs,start=1):
                    sentences = re.split(
                        r"(?<=[.!?])\s+",
                        paragraph
                    )

                    for sentence in sentences:
                        if (entity.lower()in sentence.lower()):
                            entity_evidence.append({
                                "paragraph":paragraph_index,
                                "sentence":sentence.strip(),
                                "keywords":[entity],
                                "reason":"Entity explicitly mentioned",

                                "confidence":1.0
                            })

                evidence_report[entity] = entity_evidence
        return evidence_report