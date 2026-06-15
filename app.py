# from intake.intake_loader import IntakeLoader

# loader = IntakeLoader()

# result = loader.load(
#     "dataset/Data.csv"
# )

# print(result)

from intake.intake_loader import IntakeLoader
from analysis.content_analyzer import ContentAnalyzer

loader = IntakeLoader()
analyzer = ContentAnalyzer()

result = loader.load("dataset/resume.pdf")
content = result["extraction"]["content"]

analysis_result = analyzer.analyze(content)

print(analysis_result)