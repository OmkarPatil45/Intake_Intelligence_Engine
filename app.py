# from intake.intake_loader import IntakeLoader

# loader = IntakeLoader()

# result = loader.load(
#     "dataset/BI_REPORT.pdf"
# )

# print(result)



from intake.intake_loader import IntakeLoader
from analysis.content_analyzer import ContentAnalyzer

loader = IntakeLoader()
analyzer = ContentAnalyzer()

result = loader.load("dataset/BI_REPORT.pdf")
content = result["extraction"]["content"]

analysis_result = analyzer.analyze(content)




#
from analysis.entity_extractor import EntityExtractor

extractor = EntityExtractor()

entities = extractor.extract(
    result["extraction"]["content"]
)



#
from analysis.classification_engine import (
    ClassificationEngine
)

classifier = ClassificationEngine()

classification = (
    classifier.classify(
        content
    )
)


# recommendation engine
from analysis.recommendation_engine import (RecommendationEngine)

recommender = RecommendationEngine()

recommendations = (recommender.generate(classification))


#

from processing.processing_trace import ProcessingTrace

trace = ProcessingTrace()

# Intake Layer Trace
trace.add_step(
    "File Received",
    "SUCCESS",
    f"{result['metadata']['file_name']} received"
)

trace.add_step(
        "Source Detection",
        "SUCCESS",
        f"Detected source type: {result['source_type']}"
    )

content = result["extraction"]["content"]

trace.add_step(
        "Content Extraction",
        "SUCCESS",
        f"{len(content)} characters extracted"
    )

    # Source Specific Metadata
if result["source_type"] == "pdf":

        trace.add_step(
            "PDF Metadata",
            "SUCCESS",
            f"{result['extraction'].get('page_count', 0)} pages detected"
        )

elif result["source_type"] == "csv":

            trace.add_step(
                "CSV Metadata",
                "SUCCESS",
                f"{result['extraction'].get('row_count', 0)} rows, "
                f"{result['extraction'].get('column_count', 0)} columns"
            )

elif result["source_type"] == "docx":

        trace.add_step(
            "DOCX Metadata",
            "SUCCESS",
            f"{result['extraction'].get('paragraph_count', 0)} paragraphs detected"
        )

elif result["source_type"] == "json":

        trace.add_step(
            "JSON Metadata",
            "SUCCESS",
            "JSON structure loaded"
        )

# Content Understanding
trace.add_step(
        "Content Understanding",
        "SUCCESS",
        f"Detected {analysis_result['document_type']}"
    )

# Entity Extraction
entity_count = sum(
        len(value)
        for value in entities.values()
    )

trace.add_step(
        "Entity Extraction",
        "SUCCESS",
        f"{entity_count} entities extracted"
    )

# Classification
trace.add_step(
        "Classification",
        "SUCCESS",
        f"Primary Category: {classification['primary_category']}"
    )

# Recommendation
trace.add_step(
        "Recommendation Generation",
        "SUCCESS",
        f"{len(recommendations['recommended_tags'])} tags recommended"
    )

print("\n" + "=" * 60)
print("PROCESSING TRACE")
print("=" * 60)

trace.replay_trace(delay=1)

print("\n" + "=" * 60)
print("TRACE SUMMARY")
print("=" * 60)

print(
    trace.get_summary()
)

print("Analysis result:\n")
print(analysis_result)

print("\nEntities:\n")
print(entities)

print("\nClassification_report:\n")
print(classification)

print("\nRecommendation Report:\n")
print(recommendations)