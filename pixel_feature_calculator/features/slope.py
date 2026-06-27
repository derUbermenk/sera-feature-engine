import numpy as np
from .base import BaseFeature

class SlopeFeature(BaseFeature):
    name = "slope"
    description = "Terrain slope in degrees derived from DEM"

    def compute(self, dem: np.ndarray, meta: dict) -> np.ndarray:
        # TODO: implement using richdem or numpy gradient
        raise NotImplementedError
