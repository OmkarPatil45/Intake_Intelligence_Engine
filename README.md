# Universal Intake Intelligence Engine v2

Universal Intake Intelligence Engine is a standalone document intelligence system designed to transform unknown information sources into structured, explainable intelligence records.

The engine accepts multiple file formats, analyzes content, extracts entities, classifies information, generates recommendations, maintains processing transparency and produces deterministic intelligence packages.

The primary objective is to help users quickly understand incoming information through a transparent and traceable processing pipeline.



# Recommended Architecture
## Architecture Diagram

```text
┌──────────────────────────────────────┐
│          Input Documents             │
│                                      │
│ PDF | DOCX | TXT | CSV | JSON | Form │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│           Intake Loader              |
|                                      │         
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│         Content Analyzer             │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
|           Entity Extractor           |
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
|           Entity Validator           |
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
|           Evidence Engine            │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
|          Classification Engine       |
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│           Confidence Engine          │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│    Recommendation Engine             │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
|     Intelligence Package Builder     │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│       Relationship Engine            │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│       relationship_graph.json        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│            CLI DASHBOARD             │
└──────────────────────────────────────┘

```
# Sample Dataset
```
PDF
DOCX
TXT
CSV
JSON
Form Submission JSON
```
# Folder Structure
```
Intake_Intelligence_Engine/
│
├── app.py
│
├── intake/
│   ├── intake_loader.py
│   └── source_detector.py
│
├── analysis/
│   ├── content_analyzer.py
│   ├── entity_extractor.py
|   ├── entity_validator.py
│   ├── evidence_engine.py
|   ├── entity_filters.py
│   ├── confidence_engine.py
│   ├── classification_engine.py
│   | recommendation_engine.py
|   └── relationship_engine.py
│
├── trace/
│   └── processing_trace.py
│
├── package/
│   └── intelligence_package_builder.py
│
├── search/
│   ├── query_engine.py
|   └── review_cli.py
│
├── dataset/
│
├── outputs/
│
├── review_packets/
│   └── REVIEW_PACKET.md
|
├── requirement.txt
│
└── README.md

```
## Install Dependencies

```bash
pip install -r requirements.txt
```


## Install spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

## Technology Stack
Python 3.11+, 
PyPDF2, 
python-docx, 
pandas, 
spaCy, 
pathlib, 
json

## Execution Instructions
Clone repository
Create virtual environment

python -m venv .venv

Activate virtual environment

Windows:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run application

python app.py

Follow CLI prompts

## Output

The system generates intelligence packages inside the outputs directory.

Example Outputs :-
Confidence Report
``` 
{
    "score": 90,
    "supporting_evidence_count": 48,
    "validated_entity_count": 26,
    "document_completeness": 0.5,
    "contradictory_evidence_count": 0
}
```

Relationship Graph (check outputs/relationship_graph.json)
```
{
    "source": "resume.pdf",
    "target": "project.docx",
    "relationship": "same_technology",
    "entity": "python"
}
```

## Future Enhancements
Web Dashboard

Advanced NLP Models

Vector Search

Semantic Retrieval

Multi-language Support

LLM-assisted Recommendations

## Demo Video

A complete demonstration of the project can be viewed here:

🔗 YouTube Demo:
https://www.youtube.com/watch?v=uOuFA8z2c7E
