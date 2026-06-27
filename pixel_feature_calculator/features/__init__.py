from .slope import SlopeFeature
from .twi import TWIFeature
from .bathtub import BathtubFeature

FEATURE_REGISTRY: dict = {
    "slope": SlopeFeature,
    "twi": TWIFeature,
    "bathtub_flood": BathtubFeature,
}
