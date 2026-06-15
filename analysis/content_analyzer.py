class ContentAnalyzer:
    # rules for doc mapping
    DOCUMENT_RULES = {
        "Resume": {
            "keywords": [
                "education",
                "skills",
                "experience",
                "project",
                "certification"
            ],
            "document_category": "Candidate Profile",
            "subject_area": "Information Technology"
        },

        "Research Paper": {
            "keywords": [
                "abstract",
                "methodology",
                "references",
                "conclusion",
                "literature review"
            ],
            "document_category": "Research",
            "subject_area": "Academic"
        },

        "Technical Document": {
            "keywords": [
                "architecture",
                "implementation",
                "system design",
                "api",
                "database"
            ],
            "document_category": "Technical",
            "subject_area": "Engineering"
        },

        "Project Submission": {
            "keywords": [
                "project",
                "objective",
                "technology",
                "features",
                "implementation"
            ],
            "document_category": "Project",
            "subject_area": "Technology"
        },

        "Application Form": {
            "keywords": [
                "full name",
                "address",
                "email",
                "phone",
                "date of birth"
            ],
            "document_category": "Form",
            "subject_area": "Administrative"
        },

        "Report": {
            "keywords": [
                "summary",
                "analysis",
                "findings",
                "recommendations",
                "report"
            ],
            "document_category": "Business Report",
            "subject_area": "General"
        },

        "News Article": {
            "keywords": [
                "reported",
                "according to",
                "published",
                "news",
                "breaking"
            ],
            "document_category": "Media",
            "subject_area": "Journalism"
        }
    }

    def analyze(self, text: str) -> dict:
        # Analyze document content and determine its type and purpose.
        if not text:
            return {
                "document_type": "Unknown",
                "document_category": "Unknown",
                "subject_area": "Unknown",
                "language": "Unknown",
                "confidence": 0.0,
                "matched_keywords": [],
                "explanation": "No content available."
            }

        normalized_text = text.lower()

        scores = {}

        for document_type, rule in self.DOCUMENT_RULES.items():

            score = 0

            for keyword in rule["keywords"]:
                if keyword.lower() in normalized_text:
                    score += 1

            scores[document_type] = score

        best_document_type = max(
            scores,
            key=scores.get
        )

        best_score = scores[best_document_type]

        if best_score == 0:
            return {
                "document_type": "Unknown",
                "document_category": "Unknown",
                "subject_area": "Unknown",
                "language": "English",
                "confidence": 0.0,
                "matched_keywords": [],
                "explanation": "No matching document patterns found."
            }

        matched_keywords = [
            keyword
            for keyword in self.DOCUMENT_RULES[
                best_document_type
            ]["keywords"]
            if keyword.lower() in normalized_text
        ]

        total_keywords = len(
            self.DOCUMENT_RULES[
                best_document_type
            ]["keywords"]
        )

        confidence = round(
            best_score / total_keywords,
            2
        )

        return {
            "document_type": best_document_type,

            "document_category":
            self.DOCUMENT_RULES[
                best_document_type
            ]["document_category"],

            "subject_area":
            self.DOCUMENT_RULES[
                best_document_type
            ]["subject_area"],

            "language": "English",

            "confidence": confidence,

            "matched_keywords": matched_keywords,

            "explanation":
            f"Detected document as "
            f"{best_document_type} "
            f"because the following "
            f"keywords were found: "
            f"{', '.join(matched_keywords)}"
        }