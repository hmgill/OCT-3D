from abc import ABC, abstractmethod
from pathlib import Path
from .volume import OCTVolume


class OCTImporter(ABC):

    @abstractmethod
    def load(self, path: Path) -> OCTVolume:
        pass
