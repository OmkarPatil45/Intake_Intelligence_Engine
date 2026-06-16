class ClassificationEngine:

    DOMAIN_RULES = {
        "AI": {
            "keywords": [
                "machine learning","deep learning","artificial intelligence","tensorflow","pytorch",
                "neural network","llm","rag","chatbot","data science"
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

    def classify(self, text: str):
        normalized_text = text.lower()
        scores = {}

        for category, rule in (
            self.DOMAIN_RULES.items()
        ):

            score = 0

            for keyword in (rule["keywords"]):
                if keyword in normalized_text:
                    score += 1

            scores[category] = score

        sorted_categories = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        primary_category = (sorted_categories[0][0])

        secondary_category = (sorted_categories[1][0])

        top_score = (sorted_categories[0][1])

        total_keywords = len(
            self.DOMAIN_RULES[
                primary_category
            ]["keywords"]
        )

        confidence_score = round(
            top_score / total_keywords,2
        )

        matched_keywords = [
            keyword

            for keyword in
            self.DOMAIN_RULES[
                primary_category
            ]["keywords"]

            if keyword in normalized_text
        ]

        return {

            "primary_category": primary_category,

            "secondary_category": secondary_category,

            "confidence_score": confidence_score,

            "matched_keywords": matched_keywords,

            "classification_explanation":
                (
                    f"Detected keywords: "
                    f"{', '.join(matched_keywords)}"
                )
        }