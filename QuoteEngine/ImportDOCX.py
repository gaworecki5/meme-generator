from .QuoteModel import QuoteModel
from .ImportInterface import ImportInterface
from typing import List

from docx import Document


class ImportDOCX(ImportInterface):
    """Realized class to parse quotes from .docx files"""

    allowed_extensions = ["docx"]

    @classmethod
    def can_ingest(cls, filepath: str) -> bool:
        ext = filepath.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, filepath: str) -> List[QuoteModel]:
        """Parse .docx files and return list of QuoteModel objects"""

        if not cls.can_ingest(filepath):
            raise Exception("Cannot injest this file type")

        quotes = []
        doc = Document(filepath)

        for paragraph in doc.paragraphs:
            try:
                body, author = paragraph.text.split(" – ")
            except:
                body, author = paragraph.text.split(" - ")
            body = body.strip("\n\r").strip("“”")
            author = author.strip("/n/r")

            new_quote = QuoteModel(body, author)
            quotes.append(new_quote)

        return quotes
