class RecommendationEngine:

    DOMAIN_RECOMMENDATIONS = {

        "AI": {
            "related_domains": [
                "Machine Learning","Data Science","Natural Language Processing",
                "Computer Vision"
            ],

            "recommended_tags": [
                "artificial-intelligence","machine-learning","deep-learning",
                "chatbot","automation"
            ],

            "recommended_use_cases": [
                "Intelligent Assistants","Predictive Analytics",
                "Document Intelligence","Recommendation Systems"
            ]
        },

        "Education": {
            "related_domains": [
                "E-Learning","Student Analytics","Academic Research"
            ],

            "recommended_tags": [
                "education","learning","students","academic"
            ],

            "recommended_use_cases": [
                "Learning Platforms","Student Evaluation","Course Recommendation"
            ]
        },

        "Healthcare": {
            "related_domains": [
                "Medical Analytics","Telemedicine","Health Informatics"
            ],

            "recommended_tags": [
                "healthcare","medical","patient-care"
            ],

            "recommended_use_cases": [
                "Disease Prediction","Patient Monitoring","Clinical Decision Support"
            ]
        },

        "Agriculture": {
            "related_domains": [
                "Smart Farming","AgriTech","Crop Analytics"
            ],

            "recommended_tags": [
                "agriculture","crop-management","farming"
            ],

            "recommended_use_cases": [
                "Crop Yield Prediction","Irrigation Planning","Farm Monitoring"
            ]
        },

        "Governance": {
            "related_domains": [
                "Public Administration","Citizen Services","Policy Analytics"
            ],

            "recommended_tags": [
                "governance","public-services","government"
            ],

            "recommended_use_cases": [
                "Citizen Portals","Policy Analysis","Grievance Management"
            ]
        },

        "Infrastructure": {
            "related_domains": [
                "Smart Cities","Transportation","Urban Planning"
            ],

            "recommended_tags": [
                "infrastructure","construction","urban-development"
            ],

            "recommended_use_cases": [
                "Road Planning","Traffic Analytics","Asset Management"
            ]
        },

        "Marine": {
            "related_domains": [
                "Ocean Analytics","Coastal Management","Fishery Systems"
            ],

            "recommended_tags": [
                "marine","ocean","coastal"
            ],

            "recommended_use_cases": [
                "Marine Monitoring","Fishery Forecasting","Environmental Analysis"
            ]
        }
    }

    def generate(self,classification_result: dict):

        primary_category = (classification_result.get("primary_category"))

        confidence_score = (classification_result.get("confidence_score", 0))

        recommendations = (self.DOMAIN_RECOMMENDATIONS.get(primary_category, {}))

        related_domains = (recommendations.get("related_domains",[]))

        recommended_tags = (recommendations.get("recommended_tags",[]))

        recommended_use_cases = (recommendations.get("recommended_use_cases",[]))

        recommendation_explanation = (
            f"The document was classified under '{primary_category}' with confidence score "
            f"{confidence_score}. Based on this classification, related domains, tags "
            f"and use cases have been recommended to enrich downstream intelligence processing."
        )

        intelligence_summary = (
            f"This document primarily belongs to the {primary_category} domain. "
            f"It is strongly associated with {', '.join(related_domains[:2])}. "
            f"The extracted intelligence can be used for classification, search, and knowledge management purposes. "
            f"Additional recommendations have been generated to enrich future analysis."
)

        return {

            "related_domains": related_domains,

            "recommended_tags": recommended_tags,

            "recommended_use_cases": recommended_use_cases,

            "recommended_classifications": [ primary_category],

            "recommendation_explanation": recommendation_explanation,

            "intelligence_summary": intelligence_summary
        }