from abc import ABC, abstractmethod
import numpy as np
from typing import Any

class BaseFeature(ABC):
    name: str = ""
    description: str = ""

    @abstractmethod
    def compute(self, dem: np.ndarray, meta: dict[str, Any]) -> np.ndarray:
        """
        Compute the feature raster.

        Args:
            dem: 2D numpy array of elevation values (GLO-30 or similar)
            meta: rasterio-style metadata dict (crs, transform, nodata, etc.)

        Returns:
            2D numpy array, same shape as dem
        """
        ...
