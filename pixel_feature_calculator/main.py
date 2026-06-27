import yaml
import argparse
from pixel_feature_calculator.pipeline import run


def main():
    parser = argparse.ArgumentParser(description="Compute pixel feature rasters")
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    with open(args.config) as f:
        cfg = yaml.safe_load(f)

    run(
        dem_path=cfg["dem_path"],
        output_path=cfg["output_path"],
        features=cfg.get("features"),
    )

if __name__ == "__main__":
    main()
