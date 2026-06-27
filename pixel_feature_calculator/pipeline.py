"""
Pipeline: load DEM → compute features → stack bands → write multi-band GeoTIFF
"""
import numpy as np
import rasterio
from rasterio.enums import Resampling
from pathlib import Path
from pixel_feature_calculator.features import FEATURE_REGISTRY


def run(dem_path: str, output_path: str, features: list[str] | None = None) -> None:
    features = features or list(FEATURE_REGISTRY.keys())

    with rasterio.open(dem_path) as src:
        dem = src.read(1, resampling=Resampling.nearest).astype(np.float32)
        meta = src.meta.copy()

    bands = []
    band_names = []

    for name in features:
        if name not in FEATURE_REGISTRY:
            raise ValueError(f"Unknown feature: '{name}'. Available: {list(FEATURE_REGISTRY.keys())}")
        feature = FEATURE_REGISTRY[name]()
        print(f"  Computing {name}...")
        result = feature.compute(dem, meta)
        bands.append(result)
        band_names.append(name)

    stacked = np.stack(bands, axis=0)  # (n_bands, rows, cols)

    out_meta = meta.copy()
    out_meta.update({
        "count": len(bands),
        "dtype": "float32",
    })

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with rasterio.open(output_path, "w", **out_meta) as dst:
        dst.write(stacked)
        for i, name in enumerate(band_names, start=1):
            dst.update_tags(i, name=name)

    print(f"Written: {output_path}  ({len(bands)} bands: {and_names})")
