from pathlib import Path

## defining class with supported filetype
class SourceDetector:
    SUPPORTED_TYPES = {
        ".pdf": "pdf",
        ".docx": "docx",
        ".txt": "txt",
        ".csv": "csv",
        ".json": "json"
    }

## detect file extension with error handling
    @classmethod
    def detect(cls, file_path: str) -> str:
        extension = Path(file_path).suffix.lower()

        if extension not in cls.SUPPORTED_TYPES:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return cls.SUPPORTED_TYPES[extension]