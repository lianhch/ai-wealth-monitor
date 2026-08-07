#!/usr/bin/env python3
"""Copy data JSON into public/data/ for preview & Pages build.

Usage: python scripts/build.py   (run from project root)
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
PUBLIC_DATA = ROOT / "public" / "data"

FILES = ["signals.json", "watchlist.json", "waves.json", "timeline.json", "tools.json"]
AUTO_DIR = DATA_DIR / "auto"


def copy_json(src: Path, dst: Path) -> None:
    json.loads(src.read_text(encoding="utf-8"))  # validate
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dst)
    print(f"COPIED: {src.relative_to(DATA_DIR)}")


def main() -> None:
    PUBLIC_DATA.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        src = DATA_DIR / name
        if not src.exists():
            print(f"SKIP (missing): {name}")
            continue
        copy_json(src, PUBLIC_DATA / name)
    if AUTO_DIR.exists():
        for src in AUTO_DIR.iterdir():
            if src.suffix == ".json":
                copy_json(src, PUBLIC_DATA / "auto" / src.name)
    print("build done")


if __name__ == "__main__":
    main()
