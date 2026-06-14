from intake.intake_loader import IntakeLoader

loader = IntakeLoader()

result = loader.load(
    "dataset/resume.pdf"
)

print(result)