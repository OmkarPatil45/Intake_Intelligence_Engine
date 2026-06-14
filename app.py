from intake.intake_loader import IntakeLoader

loader = IntakeLoader()

result = loader.load(
    "dataset/Data.csv"
)

print(result)