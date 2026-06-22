class ConfidenceEngine:
    """
    Generates explainable confidence scores.

    Confidence Factors:
    - Supporting evidence count
    - Entity coverage
    - Document completeness
    - Contradictory evidence (future support)
    """

    def calculate(self, evidence_report: dict,
        validated_entities: dict, classification: dict):

        evidence_count = sum(
            len(evidences)
            for evidences in evidence_report.values()
        )

        entity_count = sum(
            len(values)
            for values in validated_entities.values()
        )

        populated_sections = sum(
            1
            for values in validated_entities.values()
            if len(values) > 0
        )

        total_sections = max(len(validated_entities), 1)

        document_completeness = round(
            populated_sections / total_sections, 2
        )

        evidence_score = min(evidence_count * 5, 50)

        entity_score = min(entity_count * 2, 30)

        completeness_score = (document_completeness * 20)

        final_score = round(evidence_score +entity_score +completeness_score)

        final_score = min(final_score, 100)

        explanation = (
            f"Confidence derived from "
            f"{evidence_count} supporting evidences, "
            f"{entity_count} validated entities, "
            f"and document completeness of "
            f"{document_completeness * 100:.0f}%."
        )

        return {
            "score": final_score,
            "supporting_evidence_count": evidence_count,
            "validated_entity_count": entity_count,
            "document_completeness": document_completeness,
            "contradictory_evidence_count": 0,
            "explanation": explanation
        }