import re

# OCR / Extraction Artifacts

OCR_PATTERNS = [
    r"[a-z][A-Z]",
    r"\d{3,}",
    r".*[_]{2,}.*", 
    r".*[-]{2,}.*"
]

# File Names

FILE_PATTERNS = [
    r".*\.json$",
    r".*\.csv$",
    r".*\.pdf$",
    r".*\.docx$",
    r".*\.txt$"
]

# Technical Concepts

TECHNICAL_PATTERNS = [
    r".*classifier.*",
    r".*regressor.*",
    r".*encoder.*",
    r".*scaler.*",
    r".*algorithm.*",
    r".*curve.*",
    r".*heatmap.*",
    r".*visualization.*",
    r".*preprocessing.*",
    r".*feature.*",
    r".*dataset.*"
]

# Document Structure Terms

DOCUMENT_PATTERNS = {
    "chapter","references","contents","objective","conclusion",
    "objectives","summary","appendix","introduction","acknowledgement"
   
}

BUSINESS_INTELLIGENCE_TERMS = {
    "remaining useful life","distribution input","precision recall curve",
    "random forest","xgboost"
}
#3 
DOCUMENT_HEADING_PATTERNS = [
    r".*technical\s+skills.*",
    r".*programming\s+languages.*",
    r".*development\s+tools.*",
    r".*web\s+technologies.*",
    r".*machine\s+learning.*",
    r".*education.*",
    r".*experience.*",
    r".*professional\s+experience.*",
    r".*projects?.*",
    r".*certifications?.*",
    r".*summary.*",
    r".*objective.*",
    r".*skills.*"
]