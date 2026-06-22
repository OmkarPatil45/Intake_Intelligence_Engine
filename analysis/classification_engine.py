class ClassificationEngine:

    DOMAIN_RULES = {
        "AI": {
            "keywords": [
                "machine learning","deep learning","artificial intelligence","tensorflow","pytorch",
                "neural network","llm","rag","chatbot","data science","deep learning"
            ]
        },

        "Education": {
            "keywords": [
                "student","college","university","course","curriculum",
                "learning","education","teacher"
            ]
        },

        "Healthcare": {
            "keywords": [
                "hospital","patient","medical","health",
                "treatment","diagnosis","doctor"
            ]
        },

        "Agriculture": {
            "keywords": [
                "crop","farmer","soil","irrigation",
                "agriculture","harvest"
            ]
        },

        "Governance": {
            "keywords": [
                "government","policy","citizen",
                "public service","administration","governance"
            ]
        },

        "Infrastructure": {
            "keywords": [
                "road","bridge","transport","construction","building","infrastructure"
            ]
        },

        "Marine": {
            "keywords": [
                "ocean","marine","fishery","coastal","ship","water resources"
            ]
        }
    }

    #v2
    def classify(self, text: str, evidence_report: dict = None):
        normalized_text = text.lower()
        scores = {}
        category_matches = {}

        for category, rule in (self.DOMAIN_RULES.items()):
            matched_keywords = []

            score = 0

            for keyword in rule["keywords"]:
                if keyword in normalized_text:
                    score += 1
                    matched_keywords.append(
                        keyword
                    )

            scores[category] = score

            category_matches[category] = matched_keywords

        sorted_categories = sorted(
            scores.items(),
            key = lambda item: item[1],
            reverse=True
        )

        primary_category = (sorted_categories[0][0])

        secondary_category = (sorted_categories[1][0])

        top_score = (sorted_categories[0][1])

        total_keywords = len( self.DOMAIN_RULES[primary_category]["keywords"] )

        confidence_score = round(top_score / max(total_keywords, 1), 2)

        evidence_used = []

        primary_keywords = category_matches[primary_category]

        for keyword in primary_keywords:
            evidence_used.append(
                {
                    "keyword": keyword,
                    "reason":
                        f"Keyword '{keyword}' found in document"
                }
            )

        rejected_categories = {}

        for category, score in (sorted_categories[1:]):
            if score == 0:
                rejected_categories[category] = ("No supporting keywords found")
            else:
                rejected_categories[category] = (
                    f"Only {score} supporting "
                    f"keyword(s) found"
                )

        return {
            "primary_category": primary_category,
            "secondary_category": secondary_category,
            "confidence_score": confidence_score,
            "matched_keywords": category_matches[primary_category],
            "evidence_used": evidence_used,
            "rejected_categories": rejected_categories,
            "classification_explanation": (
                    f"{primary_category} selected because it contains "
                    f"{top_score} supporting keyword(s): "
                    f"{', '.join(category_matches[primary_category])}"
                )
        }