from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class ImportInterface(ABC):
    """Abstract Class to build realized Importer methods from"""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, filepath: str) -> bool:
        """Method to determine if a file can be parsed or not"""
        ext = filepath.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, filepath: str) -> List[QuoteModel]:
        pass

