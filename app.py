from intake.intake_loader import IntakeLoader
from analysis.content_analyzer import ContentAnalyzer
from package.intelligence_package_builder import IntelligencePackageBuilder
import json
import re
from search.review_cli import ReviewCLI
from analysis.entity_validator import EntityValidator #v2
from analysis.evidence_engine import EvidenceEngine #v2
from analysis.confidence_engine import ConfidenceEngine #v2
from analysis.relationship_engine import RelationshipEngine #v2
from analysis.entity_normalizer import (EntityNormalizer) #v2
from analysis.text_cleaner import TextCleaner #v2
from analysis.entity_extractor import EntityExtractor
from analysis.classification_engine import (ClassificationEngine)
from analysis.recommendation_engine import (RecommendationEngine)
from processing.processing_trace import ProcessingTrace



loader = IntakeLoader()
result = loader.load("dataset/user_device_.csv")

loader = IntakeLoader()
analyzer = ContentAnalyzer()
#3
raw_content = result["extraction"]["content"]
raw_content = re.sub(
    r"([A-Z]{2,}\s+[A-Z]{2,})(\s*/)",
    r"\1\n",
    raw_content
)

# -------> text cleaning
cleaner = TextCleaner()
#3 content--->cleaned_content
cleaned_content = cleaner.clean(raw_content)

analysis_result = analyzer.analyze(cleaned_content)

#v2 
extractor = EntityExtractor()
entities = extractor.extract(raw_content)

# v2 validating entities
validator = EntityValidator()
validation_result = (validator.validate(entities))

# increasing accuracy
normalizer = (EntityNormalizer())
validated_entities = (normalizer.normalize(validation_result["validated_entities"]))

rejected_entities = (validation_result["rejected_entities"])

# evidence engine v2
evidence_engine = EvidenceEngine()
evidence_report = (evidence_engine.generate(cleaned_content,validated_entities))

classifier = ClassificationEngine()
classification = classifier.classify(cleaned_content)

#v2 confidence engine
confidence_engine = (ConfidenceEngine())

confidence_report = (
    confidence_engine.calculate(evidence_report, validated_entities, classification)
)

# recommendation engine
recommender = RecommendationEngine()
recommendations = (recommender.generate(classification))

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

raw_content = result["extraction"]["content"]

trace.add_step(
        "Content Extraction",
        f"{len(raw_content)} characters extracted"
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
        for value in validated_entities.values() #v2 - modified entities to validated entities
    )

trace.add_step(
        "Entity Extraction",
        f"{entity_count} entities extracted"
    )

#v2
validated_count = sum(
    len(value)
    for value in validated_entities.values()
)

trace.add_step(
    "Entity Validation",
    (
        f"{validated_count} validated, "
        f"{len(rejected_entities)} rejected"
    )
)

trace.add_step(
    "Evidence Generation",
    (
        f"{len(evidence_report)} "
        f"evidence records generated"
    )
)

# Classification
trace.add_step(
        "Classification",
        f"Primary Category: {classification['primary_category']}"
    )

trace.add_step(
    "Confidence Scoring",
    (   f"Confidence Score: "
        f"{confidence_report['score']}"
    )
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

package_builder = IntelligencePackageBuilder()
intelligence_package = package_builder.build(
    intake_result = result,
    analysis_result = analysis_result,
    entities = validated_entities,
    rejected_entities = rejected_entities,
    evidence_report = evidence_report,
    classification = classification,
    confidence_report = confidence_report,
    recommendations = recommendations,
    processing_trace = trace.get_trace()
)

print("\n" + "=" * 60)
print("PROCESSING TRACE")
print("=" * 60)

trace.replay_trace(delay = 0.2)

print("\n" + "=" * 60)
print("TRACE SUMMARY")
print("=" * 60)

print(trace.get_summary())

print(result["metadata"]) # only metadata it wont print the entire content of doc file
print("\nAnalysis result:\n")
print(analysis_result)

print("\nEntities:\n")
print(validated_entities)

#v2
print("\nRejected Entities:\n")
print(rejected_entities)

print("\nClassification_report:\n")
print(classification)

#v2
print("\nConfidence Report:\n")
print(json.dumps(confidence_report, indent=4))


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

relationship_engine = (RelationshipEngine())
relationship_graph = (relationship_engine.build_from_outputs())

print(
    f"\nIntelligence Package saved at:\n"
    f"{output_file}"
)

review = ReviewCLI()
review.run()