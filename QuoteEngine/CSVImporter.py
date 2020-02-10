from .QuoteModel import QuoteModel
from .ImportInterface import ImportInterface
from typing import List

import pandas as pd


class CSVImporter(ImportInterface):
    """Realized class to parse quotes from .csv files"""

    allowed_extensions = ["csv"]

    @classmethod
    def can_ingest(cls, filepath: str) -> bool:
        ext = filepath.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, filepath) -> List[QuoteModel]:
        """Parse .csv files and return list of QuoteModel objects"""
        if not cls.can_ingest(filepath):
            raise Exception("Cannot injest this file type")

        quotes = []
        df = pd.read_csv(filepath)
        for index in df.index:
            new_quote = QuoteModel(df.iloc[index, 0], df.iloc[index, 1])
            quotes.append(new_quote)

        return quotes
