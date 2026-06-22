class IntelligencePackageBuilder:

    def build(self,intake_result:dict, analysis_result:dict,
        entities:dict, rejected_entities:list, evidence_report:dict,
        classification:dict, confidence_report:dict, recommendations:dict,
        processing_trace:list)->dict:

        package = {
            "source": {
                "source_type": intake_result.get("source_type")
            },

            "metadata": intake_result.get("metadata",{}),
            "analysis": analysis_result,
            "entities": entities,
            "rejected_entities": rejected_entities,
            "evidence_report": evidence_report, 
            "classification": classification,
            "confidence": confidence_report,
            "recommendations": recommendations,
            "processing_trace": processing_trace,

            "structured_output": {
                "document_type": analysis_result.get("document_type"),
                "primary_category": classification.get("primary_category"),
                "secondary_category": classification.get("secondary_category"),
                "classification_confidence": classification.get("confidence_score"),
                "overall_confidence": confidence_report.get("score"),
                "recommended_tags": recommendations.get("recommended_tags", []),
                "entity_count": self._count_entities(entities),
                "rejected_entity_count": len(rejected_entities),
                "evidence_count": self._count_evidence(evidence_report)
            }
        }

        return package

    def _count_entities(self,entities: dict) -> int:
        count = 0

        for value in entities.values():
            if isinstance(value,list):
                count += len(value)
        return count

    def _count_evidence(self,evidence_report: dict):
        count = 0
        for evidences in (evidence_report.values()):
            count += len(evidences)

        return count