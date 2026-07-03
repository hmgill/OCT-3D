from pathlib import Path

import numpy as np
from PIL import Image

from .importer import OCTImporter
from .volume import OCTVolume


class OCTA500Importer(OCTImporter):

    FOV_MM = (3.0, 3.0, 2.0)

    def load(self, path: Path) -> OCTVolume:

        bmp_files = sorted(path.glob("*.bmp"))

        if len(bmp_files) != 304:
            raise RuntimeError(
                f"Expected 304 BMP files, found {len(bmp_files)}"
            )

        bscans = []

        for file in bmp_files:

            img = np.array(Image.open(file))

            if img.shape != (640, 304):
                raise RuntimeError(
                    f"{file.name}: expected (640,304), got {img.shape}"
                )

            bscans.append(img)

        #
        # Raw stack:
        #
        # (304 B-scans, 640 depth, 304 A-scans)
        #
        stack = np.stack(bscans, axis=0)

        #
        # Convert to (Z,Y,X)
        #
        volume = np.transpose(stack, (1, 0, 2))

        dx = self.FOV_MM[0] / 304
        dy = self.FOV_MM[1] / 304
        dz = self.FOV_MM[2] / 640

        return OCTVolume(
            subject_id=path.name,

            intensity=volume,

            voxel_spacing_mm=(dz, dy, dx),

            field_of_view_mm=self.FOV_MM,

            metadata={
                "num_bscans":304,
                "dataset":"OCTA-500",
                "scan_type":"3M"
            }
        )
