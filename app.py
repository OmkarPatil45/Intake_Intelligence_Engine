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

result = loader.load("dataset/resume.pdf")
content = result["extraction"]["content"]

analysis_result = analyzer.analyze(content)
print("Analysis result:\n")
print(analysis_result)



#
from analysis.entity_extractor import EntityExtractor

extractor = EntityExtractor()

entities = extractor.extract(
    result["extraction"]["content"]
)

print("\nEntities:\n")
print(entities)

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
print("\nClassification_report:\n")
print(classification)