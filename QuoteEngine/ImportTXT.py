from .QuoteModel import QuoteModel
from .ImportInterface import ImportInterface
from typing import List


class ImportTXT(ImportInterface):
    """Realized class to parse quotes from .txt files"""

    allowed_extensions = ["txt"]

    @classmethod
    def can_ingest(cls, filepath: str) -> bool:
        ext = filepath.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, filepath: str) -> List[QuoteModel]:
        """Parse .txt files and return list of QuoteModel objects"""

        quotes = []
        with open(filepath) as f:
            for line in f.readlines():
                if len(line) <= 0:
                    raise Exception("Quotes must be properly formatted for parsing")
                body, author = line.split(" - ")
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)
        return quotes
