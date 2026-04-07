#!/usr/bin/env python3
"""Generate compressed raster copies for thesis images.

The output tree mirrors `images/` under `compressed-images/images/`.
LaTeX prefers that tree via `\\graphicspath`, so originals stay untouched.
"""

from __future__ import annotations

import argparse
import io
import shutil
from pathlib import Path

from PIL import Image, ImageOps
from PIL import UnidentifiedImageError


ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = ROOT / "images"
OUT_ROOT = ROOT / "compressed-images" / "images"
RASTER_EXTS = {".png", ".jpg", ".jpeg"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-side", type=int, default=1800)
    parser.add_argument("--jpg-quality", type=int, default=80)
    parser.add_argument("--png-colors", type=int, default=256)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def needs_refresh(src: Path, dst: Path, force: bool) -> bool:
    if force or not dst.exists():
        return True
    return src.stat().st_mtime > dst.stat().st_mtime


def resize_if_needed(img: Image.Image, max_side: int) -> Image.Image:
    width, height = img.size
    longest = max(width, height)
    if longest <= max_side:
        return img
    scale = max_side / longest
    size = (max(1, round(width * scale)), max(1, round(height * scale)))
    return img.resize(size, Image.Resampling.LANCZOS)


def png_has_alpha(img: Image.Image) -> bool:
    if "A" in img.getbands():
        return True
    return "transparency" in img.info


def save_best_png(img: Image.Image, dst: Path, colors: int) -> int:
    buffer = io.BytesIO()
    if png_has_alpha(img):
        quantized = img.quantize(colors=colors, method=Image.Quantize.FASTOCTREE)
    else:
        if img.mode not in ("RGB", "L", "P"):
            img = img.convert("RGB")
        quantized = img.quantize(colors=colors, method=Image.Quantize.MEDIANCUT)
    quantized.save(buffer, format="PNG", optimize=True, compress_level=9)
    dst.write_bytes(buffer.getvalue())
    return buffer.tell()


def save_best_jpeg(img: Image.Image, dst: Path, quality: int) -> int:
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    buffer = io.BytesIO()
    img.save(
        buffer,
        format="JPEG",
        quality=quality,
        optimize=True,
        progressive=True,
        subsampling="4:2:0",
    )
    dst.write_bytes(buffer.getvalue())
    return buffer.tell()


def compress_image(src: Path, dst: Path, args: argparse.Namespace) -> tuple[int, int, bool]:
    original_size = src.stat().st_size
    dst.parent.mkdir(parents=True, exist_ok=True)

    try:
        with Image.open(src) as opened:
            img = ImageOps.exif_transpose(opened)
            img.load()
    except (OSError, UnidentifiedImageError):
        shutil.copy2(src, dst)
        return original_size, original_size, False

    img = resize_if_needed(img, args.max_side)

    if src.suffix.lower() == ".png":
        compressed_size = save_best_png(img, dst, args.png_colors)
    else:
        compressed_size = save_best_jpeg(img, dst, args.jpg_quality)

    if compressed_size >= original_size:
        shutil.copy2(src, dst)
        compressed_size = original_size

    return original_size, compressed_size, True


def main() -> int:
    args = parse_args()
    OUT_ROOT.mkdir(parents=True, exist_ok=True)

    total_original = 0
    total_compressed = 0
    changed = 0
    compressed = 0
    skipped = 0

    for src in sorted(SRC_ROOT.rglob("*")):
        if not src.is_file():
            continue

        rel = src.relative_to(SRC_ROOT)
        dst = OUT_ROOT / rel

        if src.suffix.lower() not in RASTER_EXTS:
            dst.parent.mkdir(parents=True, exist_ok=True)
            if needs_refresh(src, dst, args.force):
                shutil.copy2(src, dst)
                changed += 1
            else:
                skipped += 1
            continue

        if not needs_refresh(src, dst, args.force):
            total_original += src.stat().st_size
            total_compressed += dst.stat().st_size
            skipped += 1
            continue

        original_size, compressed_size, was_compressed = compress_image(src, dst, args)
        total_original += original_size
        total_compressed += compressed_size
        changed += 1
        if was_compressed:
            compressed += 1

    print(
        "compressed-images refreshed: "
        f"changed={changed}, compressed={compressed}, skipped={skipped}"
    )
    print(
        "raster footprint: "
        f"{total_original / 1048576:.2f} MB -> {total_compressed / 1048576:.2f} MB"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
