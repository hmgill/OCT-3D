import numpy as np


def validate(volume):

    report = {}

    report["shape"] = volume.shape

    report["dtype"] = volume.intensity.dtype

    report["min"] = float(np.min(volume.intensity))
    report["max"] = float(np.max(volume.intensity))

    report["mean"] = float(np.mean(volume.intensity))

    report["std"] = float(np.std(volume.intensity))

    report["nan_count"] = int(np.isnan(volume.intensity).sum())

    report["empty_slices"] = int(
        sum(
            np.all(slice == 0)
            for slice in volume.intensity
        )
    )

    return report
