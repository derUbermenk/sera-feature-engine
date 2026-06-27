# pixel-feature-calculator

Computes per-pixel feature rasters for ML flood modelling (SERA project).

## Output
Multi-band GeoTIFF where each band = one feature (slope, TWI, bathtub flood mask, ...).

## Usage
```bash
python -m pixel_feature_calculator.main --config config.yaml
```

## Adding a new feature
1. Create `pixel_feature_calculator/features/my_feature.py` inheriting `BaseFeature`
2. Register it in `pixel_feature_calculator/features/__init__.py`
3. Add the name to `config.yaml`
