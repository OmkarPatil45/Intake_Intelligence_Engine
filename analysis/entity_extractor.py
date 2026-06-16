import re
import spacy
from analysis.entity_filters import ENTITY_BLACKLIST

class EntityExtractor:
    """
    Extracts structured entities from document content.

    Supported Entities:
    - Names
    - Organizations
    - Locations
    - Dates
    - Emails
    - Phone Numbers
    - Skills
    - Technologies
    """

    SKILLS = [
        "python","java","c++","c","javascript","typescript","html","css","bootstrap","react","react.js","node.js",
        "express","mongodb","mysql","sql","git","github","tensorflow","pytorch","machine learning","deep learning",
        "artificial intelligence","data science","pandas","numpy","scikit-learn","fastapi","django","flask"
    ]

    EMAIL_PATTERN = (
        r"[a-zA-Z0-9._%+-]+"
        r"@[a-zA-Z0-9.-]+"
        r"\.[a-zA-Z]{2,}"
    )

    PHONE_PATTERN = (
        r"(?:\+91[-\s]?)?"
        r"[6-9]\d{9}"
    )

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract(self, text: str) -> dict:

        if not text:
            return self._empty_result()

        doc = self.nlp(text)

        names = set()
        organizations = set()
        locations = set()
        dates = set()

        # Resume heuristic
        resume_name = self._extract_resume_name(text)

        if resume_name:
            names.add(resume_name)

        # spaCy extraction
        for entity in doc.ents:
            value = entity.text.strip()
            if (entity.label_ == "PERSON"and self._is_valid_entity(value,"PERSON")):
                names.add(value)

            elif (entity.label_ == "ORG"and self._is_valid_entity(value,"ORG")):
                organizations.add(value)

            elif (entity.label_ == "GPE"and self._is_valid_entity(value,"GPE")):
                locations.add(value)

            elif entity.label_ == "DATE":
                if not self._looks_like_phone(value):
                    dates.add(value)

        emails = self._extract_emails(text)

        phone_numbers = (self._extract_phone_numbers(text))

        skills = self._extract_skills(text)

        technologies = skills.copy()

        return {
            "names":sorted(list(names)),

            "organizations":sorted(list(organizations)),

            "technologies":sorted(list(technologies)),

            "skills":sorted(list(skills)),

            "locations":sorted(list(locations)),

            "dates":sorted(list(dates)),

            "emails":sorted(list(emails)),

            "phone_numbers":sorted(list(phone_numbers))
        }

    def _extract_resume_name(self,text: str):
        lines = text.split("\n")
        for line in lines[:10]:
            candidate = line.strip()

            if (candidate.isupper()and 2 <= len(candidate.split()) <= 4):
                return candidate
        return None

    def _extract_emails(self,text: str):
        return set(
            re.findall(self.EMAIL_PATTERN,text))

    def _extract_phone_numbers(self,text: str):

        return set(re.findall(self.PHONE_PATTERN,text))

    def _extract_skills(self,text: str):
        found_skills = set()

        normalized_text = (text.lower())

        for skill in self.SKILLS:
            pattern = (
                r"\b"
                + re.escape(skill)
                + r"\b"
            )

            if re.search(pattern,normalized_text):
                found_skills.add(skill)

        return found_skills

    def _is_valid_entity(self,entity_text: str, entity_type: str):

        candidate = (entity_text.lower().strip())

        blacklist = (ENTITY_BLACKLIST.get(
                entity_type,
                set()
            )
        )

        return (candidate not in blacklist)

    def _looks_like_phone(self,value: str):

        return bool(re.fullmatch(
                r"\d{10}",
                value))

    def _empty_result(self):
        return {
            "names": [],
            "organizations": [],
            "technologies": [],
            "skills": [],
            "locations": [],
            "dates": [],
            "emails": [],
            "phone_numbers": []
        }