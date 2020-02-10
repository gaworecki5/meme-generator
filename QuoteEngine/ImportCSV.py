from .QuoteModel import QuoteModel
from .ImportInterface import ImportInterface
from typeing import List

import pandas as pd


class ImportCSV(ImportInterface):
    """Realized class to parse quotes from .csv files"""

    allowed_extensions = ["csv"]

    @classmethod
    def can_ingest(cls, filepath: str) -> bool:
        ext = filepath.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    def parse(cls, filepath) -> List[QuoteModel]:
        df = pd.read_csv(filepath)
        for row in df.iterrows():
            print(row)

