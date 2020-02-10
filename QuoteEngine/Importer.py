from .QuoteModel import QuoteModel
from .ImportInterface import ImportInterface
from .DOCXImporter import DOCXImporter
from .CSVImporter import CSVImporter
from .TXTImporter import TXTImporter
from .PDFImporter import PDFImporter
from typing import List


class Importer(ImportInterface):
    """Class to automatically find the correct module to parse a file of any type"""

    importers = [TXTImporter, DOCXImporter, CSVImporter, PDFImporter]

    @classmethod
    def parse(cls, filepath: str) -> List[QuoteModel]:
        """Method cycles through available Importers and chooses the correct one for each file type"""
        for importer in cls.importers:
            if importer.can_ingest(filepath):
                return importer.parse(filepath)
