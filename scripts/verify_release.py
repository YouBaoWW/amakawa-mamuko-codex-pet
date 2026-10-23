#!/usr/bin/env python3
"""Read-only checks for the three published pet packages (Python 3.9+, Pillow)."""

import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    from PIL import Image
except ImportError:
    sys.exit("Missing Pillow. Install with: python -m pip install Pillow")

ROOT = Path(__file__).resolve().parents[1]
FRAME_COUNTS = (6, 8, 8, 4, 5, 8, 6, 6, 6)
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def inside_root(path):
    try:
        path.resolve().relative_to(ROOT)
        return True
    except ValueError:
        return False


def check_file(path, sha256, size=None):
    check(inside_root(path) and path.is_file(), f"Missing/invalid file: {path.name}")
    if not inside_root(path) or not path.is_file():
        return
    data = path.read_bytes()
    check(digest(data) == sha256, f"SHA-256 mismatch: {path.relative_to(ROOT)}")
    if size is not None:
        check(len(data) == size, f"Size mismatch: {path.relative_to(ROOT)}")


def check_pet(pet):
    folder = ROOT / pet["directory"]
    config = read_json(folder / "pet.json")
    check(config.get("id") == pet["id"], f"Pet ID mismatch: {pet['id']}")
    check(config.get("displayName") == pet["displayName"], f"Display name mismatch: {pet['id']}")
    check(config.get("spriteVersionNumber") == 2, f"Expected v2: {pet['id']}")
    check(config.get("spritesheetPath") == "spritesheet.webp", f"Atlas path mismatch: {pet['id']}")
    atlas = folder / "spritesheet.webp"
    check_file(atlas, pet["atlasSha256"])
    with Image.open(atlas) as image:
        check(image.format == "WEBP" and image.size == (1536, 2288), f"Atlas format/size: {pet['id']}")
        alpha = image.convert("RGBA").getchannel("A")
        check("A" in image.getbands() and alpha.getextrema()[0] == 0, f"Transparency: {pet['id']}")
        cells = [(row, col) for row, count in enumerate(FRAME_COUNTS) for col in range(count)]
        cells += [(0, 6)] + [(9 + i // 8, i % 8) for i in range(16)]
        for row, col in cells:
            bbox = alpha.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208)).getbbox()
            check(bbox is not None, f"Empty frame: {pet['id']} row {row}, column {col}")

    archive = ROOT / pet["archive"]["path"]
    check_file(archive, pet["archive"]["sha256"], pet["archive"]["bytes"])
    with zipfile.ZipFile(archive) as package:
        check(package.testzip() is None, f"ZIP CRC failed: {archive.name}")
        entries = [item for item in package.infolist() if not item.is_dir()]
        names = [item.filename for item in entries]
        check(len(names) == len(set(names)), f"Duplicate ZIP paths: {archive.name}")
        if pet["archive"]["layout"] == "install-files":
            check(set(names) == {"pet.json", "spritesheet.webp"}, f"Unexpected ZIP content: {archive.name}")
        else:
            expected = {p.relative_to(ROOT).as_posix() for p in (ROOT / "mamuko-pass-v2").rglob("*") if p.is_file()}
            check(set(names) == expected, f"Complete ZIP file list mismatch: {archive.name}")
        for item in entries:
            source = folder / item.filename if pet["archive"]["layout"] == "install-files" else ROOT / item.filename
            check(inside_root(source) and source.is_file(), f"ZIP source missing: {item.filename}")
            if inside_root(source) and source.is_file():
                check(package.read(item) == source.read_bytes(), f"ZIP source differs: {item.filename}")
    print(f"Checked: {pet['displayName']}")


def check_existing_manifests():
    pass_root = ROOT / "mamuko-pass-v2"
    for item in read_json(pass_root / "package-manifest.json"):
        check_file(pass_root / item["path"], item["sha256"], item["bytes"])
    bond_root = ROOT / "mamuko-bond-v2"
    bond = read_json(bond_root / "package-manifest.json")
    check_file(bond_root / bond["atlas"]["path"], bond["atlas"]["sha256"])
    check_file(bond_root / bond["archive"]["path"], bond["archive"]["sha256"])


def check_links():
    for doc in ROOT.rglob("*.md"):
        if ".git" in doc.relative_to(ROOT).parts:
            continue
        for target in re.findall(r"\]\(([^)\s]+)(?:\s+[^)]*)?\)", doc.read_text(encoding="utf-8-sig")):
            url = urlsplit(target.strip("<>"))
            if url.scheme or url.netloc or not url.path:
                continue
            path = doc.parent / unquote(url.path)
            check(inside_root(path) and path.exists(), f"Broken link in {doc.relative_to(ROOT)}: {target}")


def main():
    manifest = read_json(ROOT / "release-manifest.json")
    pets = manifest["pets"]
    check(len(pets) == 3 and len({pet["id"] for pet in pets}) == 3, "Expected three distinct pets")
    for pet in pets:
        check_pet(pet)
    check_existing_manifests()
    check_links()
    if errors:
        for message in errors:
            print(f"FAIL: {message}", file=sys.stderr)
        return 1
    print("PASS: 3 pets, atlas frames, ZIP contents, checksums and local Markdown links.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        sys.exit(f"FAIL: {error}")
