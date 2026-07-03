from dataclasses import dataclass
from pathlib import Path
import numpy as np


@dataclass
class OCTVolume:
    subject_id: str

    intensity: np.ndarray
    voxel_spacing_mm: tuple[float, float, float]
    field_of_view_mm: tuple[float, float, float]

    coordinate_system: str = "ZYX"

    metadata: dict | None = None

    @property
    def shape(self):
        return self.intensity.shape
