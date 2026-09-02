# Contributing

This repository is a Codex v2 pet pack. Keep additions in the same layout as the existing pets.

## Pet folder layout

```text
pets/<pet-id>/
├── pet.json
├── spritesheet.png
└── spritesheet.webp
```

`pet.json` should include at least:

- `id` matching the folder name
- `displayName` or `name`
- `spriteVersionNumber`: `2`
- `spritesheetPath` when the pet uses `spritesheet.webp`

Spritesheets should be `1536x2288` (`192x208` cells, 8 columns × 11 rows).

## Pull requests

- Prefer one pet per pull request
- Do not regenerate or restyle existing pets unless the change is a requested fix
- Update `README.md`, `INVENTORY.md`, and `pets/README.md` when adding or removing a pet
- Still previews belong in `docs/previews/<pet-id>.png`
- Pose slideshow GIFs (idle / waving / waiting) belong in `docs/previews/<pet-id>.gif`

## Disclaimer

This is an unofficial fan-made pack. See [NOTICE.md](NOTICE.md).
