#!/usr/bin/env python3
"""Validate the on-disk structure of the MGS pet pack."""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PET_ROOT = ROOT / "pets"
errors = []
pets = sorted(p for p in PET_ROOT.iterdir() if p.is_dir() and not p.name.startswith("."))

for pet in pets:
    manifest = pet / "pet.json"
    if not manifest.exists():
        errors.append(f"{pet.name}: missing pet.json")
        continue
    try:
        data = json.loads(manifest.read_text())
    except Exception as exc:
        errors.append(f"{pet.name}: invalid JSON ({exc})")
        continue
    if data.get("id") != pet.name:
        errors.append(f"{pet.name}: id does not match folder")
    if data.get("spriteVersionNumber") != 2:
        errors.append(f"{pet.name}: spriteVersionNumber is not 2")
    if not (data.get("name") or data.get("displayName")):
        errors.append(f"{pet.name}: missing name/displayName")
    for filename in ("spritesheet.png", "spritesheet.webp"):
        if not (pet / filename).exists():
            errors.append(f"{pet.name}: missing {filename}")
    try:
        with Image.open(pet / "spritesheet.png") as image:
            if image.size != (1536, 2288):
                errors.append(f"{pet.name}: PNG dimensions are {image.size}")
    except Exception as exc:
        errors.append(f"{pet.name}: unreadable PNG ({exc})")
    for suffix in ("png", "gif"):
        if not (ROOT / "docs" / "previews" / f"{pet.name}.{suffix}").exists():
            errors.append(f"{pet.name}: missing docs/previews/{pet.name}.{suffix}")

if len(pets) != 25:
    errors.append(f"expected 25 pets, found {len(pets)}")
if errors:
    print("Pack validation failed:")
    print("\n".join(f"- {error}" for error in errors))
    raise SystemExit(1)
print(f"Pack validation passed: {len(pets)} pets, v2 atlases, and previews verified.")
