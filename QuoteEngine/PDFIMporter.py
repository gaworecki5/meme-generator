from .QuoteModel import QuoteModel
from .ImportInterface import ImportInterface
from typing import List
import os
import random
import subprocess


class PDFImporter(ImportInterface):
    """Realized class to parse quotes from .pdf files"""

    allowed_extensions = ["pdf"]

    @classmethod
    def can_ingest(cls, filepath: str) -> bool:
        ext = filepath.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, filepath: str) -> List[QuoteModel]:
        """Parse .pdf files and return list of QuoteModel objects"""

        if not cls.can_ingest(filepath):
            raise Exception("Cannot injest this file type")

        quotes = []
        tmp = f"./tmp/{random.randint(0,10000)}.txt"
        # call pdftotext with CLI
        call = subprocess.call(["pdftotext", filepath, tmp])
        with open(tmp, "r") as f:
            for line in f.readlines():
                line = line.strip("/n/r").strip()
                if len(line) > 10 and len(line.split("\xad")) == 2:
                    body, author = line.split("\xad")
                    author = author.strip("\n\r")
                    body = body.strip("/n/r").strip().strip('"')
                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)

        os.remove(tmp)
        return quotes
