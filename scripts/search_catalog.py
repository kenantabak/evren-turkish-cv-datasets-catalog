#!/usr/bin/env python3
"""Search and filter the 316 EVREN Turkish Computer Vision datasets catalog."""
import argparse
import csv
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Search 316 open EVREN CV datasets.")
    parser.add_argument("--query", "-q", default="", help="Keyword to match dataset name or classes.")
    parser.add_argument("--min-images", type=int, default=0, help="Minimum image count filter.")
    parser.add_argument("--limit", type=int, default=20, help="Max rows to print.")
    args = parser.parse_args()

    csv_path = Path(__file__).resolve().parents[1] / "data" / "datasets_catalog_316.csv"
    rows = []
    with open(csv_path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            imgs = int(r["image_count"])
            hay = (r["name"] + " " + r["sample_classes"]).lower()
            if imgs >= args.min_images and (not args.query or args.query.lower() in hay):
                rows.append((imgs, r))

    rows.sort(key=lambda x: x[0], reverse=True)
    print(f"Found {len(rows)} matching datasets (showing top {min(args.limit, len(rows))}):\n")
    for imgs, r in rows[: args.limit]:
        print(f"[{imgs:7,d} imgs | {int(r['annotation_count']):9,d} anns] {r['name']}\n  -> {r['evren_url']}")


if __name__ == "__main__":
    main()
