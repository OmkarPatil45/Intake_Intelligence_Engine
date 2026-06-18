# Universal Intake Intelligence Engine v1

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
│      Phase 1: Universal Intake       │
│                                      │
│ • Intake Loader                      │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│    Phase 2: Content Understanding    │
│                                      │
│ • Document Type Detection            │
│ • Category Detection                 │
│ • Subject Area Identification        │
│ • Language Detection                 │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│     Phase 3: Entity Intelligence     │
│                                      │
│ • Organizations                      │
│ • Skills                             │
│ • Locations                          │
│ • Dates                              │
│ • Emails                             │
│ • Phone Numbers                      │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│      Phase 4: Classification         │
│                                      │
│ • Primary Category                   │
│ • Secondary Category                 │
│ • Confidence Score                   │
│ • Classification Explanation         │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│      Phase 5: Recommendation         │
│                                      │
│ • Recommendation Report              │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│   Phase 6: Processing Visibility     │
│                                      │
│ • Execution Summary                  │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│  Phase 7: Intelligence Package       │
│                                      │
│ • Source Information                 │
│ • Recommendations                    │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│    Phase 8: Search & Retrieval       │
│                                      │
│ • Search by Keyword                  │
│ • Search by Category                 │
│ • Search by Entity                   │
│ • Search by Source Type              │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│     Phase 9: Review Interface        │
│                                      │
│ • Interactive CLI                    │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│           Final Output               │
│                                      │
│ Intelligence Package JSON            │              
│ Processing Trace                     │
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
|   ├── entity_filters.py
│   ├── classification_engine.py
│   └── recommendation_engine.py
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

## Processing Trace Example

### Execution Information

| Field               | Value               |
| ------------------- | ------------------- |
| Execution Timestamp | 2026-06-17 15:44:04 |
| Overall Status      | SUCCESS             |

### Processing Workflow

```text
[1/8] File Received
      → abc.txt received

[2/8] Source Detection
      → Detected source type: txt

[3/8] Content Extraction
      → 127 characters extracted

[4/8] Content Understanding
      → Detected Technical Document

[5/8] Entity Extraction
      → 1 entities extracted

[6/8] Classification
      → Primary Category: AI

[7/8] Recommendation Generation
      → 5 tags recommended

[8/8] Intelligence Package
      → Final intelligence package generated
```

### Processing Summary

```text
Input File
    ↓
Source Detection
    ↓
Content Extraction
    ↓
Content Understanding
    ↓
Entity Extraction
    ↓
Classification
    ↓
Recommendation Generation
    ↓
Intelligence Package Creation
```

The processing trace provides complete transparency into every stage of the intelligence pipeline, enabling reviewers to understand how raw information is transformed into structured intelligence records.

## Output

The system generates intelligence packages inside the outputs directory.

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
