"""
Centralized validation rules used across the
Universal Intelligence Validation Framework.

Every validator imports this file instead of
hardcoding rules.
"""

REQUIRED_FIELDS = [
    "source",
    "metadata",
    "analysis",
    "entities",
    "classification",
    "confidence",
    "recommendations",
    "processing_trace"
]

#3 EXPECTED DATA TYPES
EXPECTED_TYPES = {
    "source": dict,
    "metadata": dict,
    "analysis": dict,
    "entities": dict,
    "classification": dict,
    "confidence": dict,
    "recommendations": dict,
    "processing_trace": dict
}

QUALITY_THRESHOLDS = {
    "PASS": 90,
    "WARNING": 70,
    "FAIL": 0
}

MIN_CONFIDENCE_SCORE = 0

MAX_CONFIDENCE_SCORE = 100

VALIDATION_STATUS = {
    "PASS",
    "WARNING",
    "FAIL"
}

SUGGESTION_RULES = {
    "Required Field Check":
        "Ensure all required fields are present before packaging.",

    "Data Type Check":
        "Verify that every field matches the expected data type.",

    "Empty Value Check":
        "Populate empty fields before generating the intelligence package.",

    "Duplicate Entity Check":
        "Remove duplicate entities before packaging.",

    "Entity Consistency":
        "Verify extracted entities and ensure entity lists are populated.",

    "Classification Consistency":
        "Review document classification logic and category assignment.",

    "Confidence Check":
        "Verify confidence score calculation and explanation.",

    "Evidence Check":
        "Generate evidence for every important classification and entity.",

    "Processing Trace":
        "Record every processing step for complete explainability."

}