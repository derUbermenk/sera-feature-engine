import numpy as np
from .base import BaseFeature

class BathtubFeature(BaseFeature):
    name = "bathtub_flood"
    description = "Binary flood mask from bathtub inundation model (1=flood, 0=dry)"

    def __init__(self, slr_scenario: float = 0.0):
        self.slr_scenario = slr_scenario

    def compute(self, dem: np.ndarray, meta: dict) -> np.ndarray:
        # TODO: wire in connected-component bathtub logic from SERA core
        raise NotImplementedError
