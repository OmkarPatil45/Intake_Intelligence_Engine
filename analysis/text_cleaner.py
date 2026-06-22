import re


class TextCleaner:

    def clean(self,text: str):
        if not text:
            return ""

        # Remove excessive whitespace
        text = re.sub(r"\s+", " ", text)

        # Remove page artifacts
        text = re.sub(
            r"\bPage\s+\d+\b",
            "",
            text,
            flags=re.I
        )

        # Remove isolated bullets
        text = re.sub(r"[•●▪◦]", " ", text)

        # Collapse repeated punctuation
        text = re.sub(r"[-_]{2,}", " ", text)

        # Remove OCR line fragments
        text = re.sub(r"\n\s*\n+", "\n", text)

        return text.strip()