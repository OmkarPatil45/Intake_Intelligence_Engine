from intake.intake_loader import IntakeLoader
from analysis.content_analyzer import ContentAnalyzer
from package.intelligence_package_builder import IntelligencePackageBuilder
import json
from search.review_cli import ReviewCLI
from analysis.entity_extractor import EntityExtractor
from analysis.classification_engine import (ClassificationEngine)
from analysis.recommendation_engine import (RecommendationEngine)
from processing.processing_trace import ProcessingTrace


loader = IntakeLoader()
result = loader.load("dataset/Sample1.txt")

loader = IntakeLoader()
analyzer = ContentAnalyzer()

content = result["extraction"]["content"]

analysis_result = analyzer.analyze(content)

#
extractor = EntityExtractor()

entities = extractor.extract(result["extraction"]["content"])
#
classifier = ClassificationEngine()

classification = (classifier.classify(content))

# recommendation engine
recommender = RecommendationEngine()
recommendations = (recommender.generate(classification))

#
trace = ProcessingTrace()

# Intake Layer Trace
trace.add_step(
    "File Received",
    f"{result['metadata']['file_name']} received"
)

trace.add_step(
        "Source Detection",
        f"Detected source type: {result['source_type']}"
    )

content = result["extraction"]["content"]

trace.add_step(
        "Content Extraction",
        f"{len(content)} characters extracted"
    )

    # Source Specific Metadata
if result["source_type"] == "pdf":

        trace.add_step(
            "PDF Metadata",
            f"{result['extraction'].get('page_count', 0)} pages detected"
        )

elif result["source_type"] == "csv":

            trace.add_step(
                "CSV Metadata",
                f"{result['extraction'].get('row_count', 0)} rows, "
                f"{result['extraction'].get('column_count', 0)} columns"
            )

elif result["source_type"] == "docx":

        trace.add_step(
            "DOCX Metadata",
            f"{result['extraction'].get('paragraph_count', 0)} paragraphs detected"
        )

elif result["source_type"] == "json":

        trace.add_step(
            "JSON Metadata",
            "JSON structure loaded"
        )

# Content Understanding
trace.add_step(
        "Content Understanding",
        f"Detected {analysis_result['document_type']}"
    )

# Entity Extraction
entity_count = sum(
        len(value)
        for value in entities.values()
    )

trace.add_step(
        "Entity Extraction",
        f"{entity_count} entities extracted"
    )

# Classification
trace.add_step(
        "Classification",
        f"Primary Category: {classification['primary_category']}"
    )

# Recommendation
trace.add_step(
        "Recommendation Generation",
        f"{len(recommendations['recommended_tags'])} tags recommended"
    )

# intelligence 
trace.add_step(
    "Intelligence Package",
    "Final intelligence package generated"
)

package_builder=IntelligencePackageBuilder()
intelligence_package = package_builder.build(
    intake_result=result,
    analysis_result=analysis_result,
    entities=entities,
    classification=classification,
    recommendations=recommendations,
    processing_trace=trace.get_trace()
)

print("\n" + "=" * 60)
print("PROCESSING TRACE")
print("=" * 60)

trace.replay_trace(delay = 0.2)

print("\n" + "=" * 60)
print("TRACE SUMMARY")
print("=" * 60)

print(trace.get_summary())

print(result)
print("Analysis result:\n")
print(analysis_result)

print("\nEntities:\n")
print(entities)

print("\nClassification_report:\n")
print(classification)

print("\nRecommendation Report:\n")
print(recommendations)

print("\nIntelligence Package:\n")
print(json.dumps(intelligence_package,indent=4))

output_file=(
    f"outputs/"
    f"{result['metadata']['file_name']}"
    f"_intelligence.json"
)

with open(output_file,"w",encoding="utf-8") as file:
    json.dump(intelligence_package,file,indent=4)

print(
    f"\nIntelligence Package saved at:\n"
    f"{output_file}"
)

review = ReviewCLI()
review.run()