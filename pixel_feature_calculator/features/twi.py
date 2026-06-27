import numpy as np
from .base import BaseFeature

class TWIFeature(BaseFeature):
    name = "twi"
    description = "Topographic Wetness Index: ln(a / tan(slope))"

    def compute(self, dem: np.ndarray, meta: dict) -> np.ndarray:
        # TODO: implement using pysheds or richdem for flow accumulation
        raise NotImplementedError
