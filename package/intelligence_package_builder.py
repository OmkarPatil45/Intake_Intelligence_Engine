class IntelligencePackageBuilder:

    def build(self, intake_result:dict,
        analysis_result:dict,entities:dict,classification:dict,
        recommendations:dict,processing_trace:list
    )->dict:

        package={
            "source":{
                "source_type": intake_result.get("source_type")
            },

            "metadata": intake_result.get("metadata",{}),

            "analysis": analysis_result,

            "entities": entities,

            "classification": classification,

            "recommendations": recommendations,

            "processing_trace": processing_trace,

            "structured_output":{
                "document_type": analysis_result.get("document_type"),
                "primary_category": classification.get("primary_category"),
                "secondary_category": classification.get("secondary_category"),
                "confidence_score": classification.get("confidence_score"),
                "recommended_tags":recommendations.get("recommended_tags", []),
                "entity_count": self._count_entities(entities)
            }
        }

        return package

    def _count_entities(self,entities:dict)->int:
        count=0
        for value in entities.values():
            if isinstance(value,list):
                count+=len(value)

        return count