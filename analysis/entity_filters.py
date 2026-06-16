"""
Entity filtering rules.

Used to remove obvious false positives produced by generic NER models.
"""

ENTITY_BLACKLIST = {

    "PERSON": {
        "html","html5","css","css3","javascript","react","react.js","node.js","mongodb",
        "sql","python","c++","machine learning","chatbot","bootstrap"
    },

    "ORG": {
        "html","css","bootstrap","javascript","machine learning","database systems",
        "crud","roc","xgboost","random forest","classifier","precision recall curve",
        "recall curve"
    },

    "GPE": {
        "ai","python","numpy","c++","sql","roc"
    }
}