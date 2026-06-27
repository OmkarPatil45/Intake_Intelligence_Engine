# Universal Intake Intelligence & Validation Framework

A production-oriented, deterministic, and explainable document intelligence framework capable of transforming heterogeneous documents into structured intelligence packages and validating their quality using a standalone validation framework.

The project was developed incrementally through three engineering phases:

* **Phase 1 – Universal Intake Intelligence Engine**
* **Phase 2 – Explainable Intelligence & Evidence Framework**
* **Phase 3 – Universal Intelligence Validation Framework**

The framework emphasizes modularity, explainability, deterministic execution, extensibility and production-ready software engineering practices.

---

# Features

## Universal Document Intake

Supports multiple document formats:

* PDF, DOCX, TXT, CSV, JSON

---

## Content Understanding

Automatically analyzes incoming documents and extracts:

* Document Type
* Word Count
* metadata

---

## Entity Intelligence

Extracts structured entities including:

* Person
* Organization
* Technology
* Skills
* Location
* Dates
* Email
* Phone Number

Enhancements include:

* spaCy Large NER Model (`en_core_web_lg`)
* Resume Header Detection
* PDF-specific preprocessing
* Pattern-based validation

---

## Explainable Intelligence

Generates:

* Validated Entities
* Rejected Entities
* Entity Evidence
* Confidence Score
* Classification Explanation
* Recommendation Report
* Relationship Graph

Every intelligence decision includes deterministic reasoning.

---

## Universal Validation Framework

Validates generated intelligence packages using:

* Schema Validation
* Required Field Validation
* Data Type Validation
* Entity Consistency
* Classification Consistency
* Confidence Validation
* Evidence Completeness

---

## Quality Assessment

Generates:

* Quality Score (0–100)
* PASS / WARNING / FAIL
* Error List
* Warning List
* Improvement Suggestions
* Deterministic Explanation

---

## Batch Validation

Supports validation of an entire directory of intelligence packages.

Produces:

* Total Packages
* Successful Packages
* Failed Packages
* Average Quality Score
* Aggregate Validation Report

---

## Replay Verification

Verifies deterministic execution by validating identical intelligence packages multiple times.

Produces:

* Replay Report
* Stable Quality Verification
* Stable Validation Verification

---

## Interactive Review Console

Supports:

* Validate One Package
* Validate Entire Folder
* Search Validation Reports
* Filter by Quality Score
* View Failed Reports
* Replay Verification

---

# System Architecture

```text
                 Input Documents
        PDF | DOCX | TXT | CSV | JSON
                    │
                    ▼
            Universal Intake Loader
                    │
                    ▼
            Content Analyzer
                    │
                    ▼
            Entity Extractor
                    │
                    ▼
            Entity Validator
                    │
                    ▼
             Evidence Engine
                    │
                    ▼
           Confidence Engine
                    │
                    ▼
         Classification Engine
                    │
                    ▼
       Recommendation Engine
                    │
                    ▼
      Intelligence Package Builder
                    │
                    ▼
          Relationship Engine
                    │
                    ▼
        Intelligence Package (.json)
                    │
                    ▼
     Universal Validation Framework
                    │
     ┌──────────────┼──────────────┐
     ▼              ▼              ▼
Schema       Consistency      Quality
Validator     Validator       Assessment
                    │
                    ▼
           Batch Validation
                    │
                    ▼
           Replay Validation
                    │
                    ▼
        Interactive Review CLI
```

---

# Project Structure

```text
Intake_Intelligence_Engine/

│
├── app.py
├── validation_app.py
│
├── intake/
│
├── analysis/
│
├── processing/
│
├── package/
│
├── search/
│
├── validation/
│
│   ├── schema_validator.py
│   ├── consistency_validator.py
│   ├── validation_engine.py
│   ├── quality_engine.py
│   ├── batch_validator.py
│   ├── replay_validator.py
│   ├── validation_rules.py
│   ├── report_builder.py
│   └── utils.py
│
├── review/
│
│   ├── review_cli.py
│   ├── menu.py
│   ├── display.py
│   ├── search.py
│   ├── filters.py
│   └── exporter.py
│
├── dataset/
├── outputs/
├── validation_reports/
├── review_packets/
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository.

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Install the spaCy model.

```bash
python -m spacy download en_core_web_lg
```

---

# Technology Stack

* Python 3.11+
* PyMuPDF
* python-docx
* pandas
* spaCy (`en_core_web_lg`)
* pathlib
* JSON
* Regular Expressions

---

# Running the Project

## Intelligence Engine

```bash
python app.py
```

Generates:

* Intelligence Packages
* Relationship Graph
* Evidence Reports
* Confidence Reports

---

## Validation Framework

```bash
python validation_app.py
```

Launches the interactive validation console.

---

# Generated Outputs

## Intelligence Outputs

```text
outputs/

resume.pdf_intelligence.json

project.docx_intelligence.json

relationship_graph.json
```
{
    "source": "resume.pdf",
    "target": "project.docx",
    "relationship": "same_technology",
    "entity": "python"
}
```

---

## Validation Reports

```text
validation_reports/

resume_validation_report.json

resume_quality_report.json

batch_report.json

replay_report.json
```
```
Select Package : 1

{
    "replay_count": 3,
    "validation_reports_identical": true,
    "quality_reports_identical": true,
    "quality_scores": [
        95,
        95,
        95
    ],
    "overall_status": "PASS",
    "explanation": "Replay verification successful."
}
 replay_report.json exported.
 ```
---

# Deterministic Execution

The framework is entirely deterministic.

It uses:

* Rule-based entity validation
* Rule-based classification
* Rule-based confidence scoring
* Rule-based quality assessment
* Rule-based replay verification

No external APIs are used.

No LLM dependency exists during execution.

Identical inputs always produce identical outputs.

---

# Future Enhancements

* Weighted Validation Rules
* Validator Registry
* Web Dashboard
* Semantic Search
* Vector Retrieval
* Multi-language Processing
* REST API
* Docker Deployment
* CI/CD Pipeline
* Unit & Integration Testing

---

# Demo Video

A complete project demonstration is available on YouTube.

**Demo Link:**

```text
https://www.youtube.com/watch?v=uOuFA8z2c7E
```

---

# Author

**Omkar Patil**

Universal Intake Intelligence & Validation Framework

Production-oriented, explainable, deterministic document intelligence system developed as part of a multi-stage engineering evaluation focused on modular software architecture, validation, and explainable AI.
