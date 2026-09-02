# Installation

These pets install into the Codex custom-pet directory:

```text
~/.codex/pets/
```

On most machines that expands to:

```text
$HOME/.codex/pets/<pet-id>/
```

Each included pet already uses that folder layout:

```text
pets/solidsnake/
├── pet.json
├── spritesheet.png
└── spritesheet.webp
```

Copy the pet folder as-is. Do not flatten the files into `~/.codex/pets/` itself.

## Get the pack

Clone the repository:

```bash
git clone https://github.com/VinceGuyMan/MGS1-Pet-Pack.git
cd MGS1-Pet-Pack
```

Or download a source ZIP from GitHub:

- [Latest source ZIP](https://github.com/VinceGuyMan/MGS1-Pet-Pack/archive/refs/heads/vinceguyman-publish-pet-pack.zip)
- [Releases](https://github.com/VinceGuyMan/MGS1-Pet-Pack/releases)

Create the destination directory if it does not exist:

```bash
mkdir -p ~/.codex/pets
```

## Install one pet

Copy a single pet folder into `~/.codex/pets/`:

```bash
cp -R pets/solidsnake ~/.codex/pets/
```

The result should look like:

```text
~/.codex/pets/solidsnake/pet.json
~/.codex/pets/solidsnake/spritesheet.webp
~/.codex/pets/solidsnake/spritesheet.png
```

Repeat with any other folder under `pets/`, for example `pets/ocelot` or `pets/metalgearrex`.

## Install the full pack

Copy every pet folder:

```bash
mkdir -p ~/.codex/pets
cp -R pets/*/ ~/.codex/pets/
```

That copies the 22 pet directories and leaves `pets/README.md` behind.

## Update pets

Replace an installed pet folder with the version from this repository. Keep a backup if you have local edits.

```bash
cp -R ~/.codex/pets/solidsnake ~/.codex/pets/solidsnake.bak
rm -rf ~/.codex/pets/solidsnake
cp -R pets/solidsnake ~/.codex/pets/
```

To refresh the whole pack from a newer clone or release:

```bash
cp -R pets/*/ ~/.codex/pets/
```

## Uninstall pets

Remove one pet:

```bash
rm -rf ~/.codex/pets/solidsnake
```

Remove the whole pack (only the folders from this repository):

```bash
rm -rf \
  ~/.codex/pets/campbell \
  ~/.codex/pets/decoyoctopus \
  ~/.codex/pets/emma \
  ~/.codex/pets/genomesoldier \
  ~/.codex/pets/genomesoldier_black \
  ~/.codex/pets/genomesoldier_hazmat \
  ~/.codex/pets/genomesoldier_woodland \
  ~/.codex/pets/grayfox \
  ~/.codex/pets/liquidsnake \
  ~/.codex/pets/meiling \
  ~/.codex/pets/meryl \
  ~/.codex/pets/metalgearray \
  ~/.codex/pets/metalgearrex \
  ~/.codex/pets/nastasha \
  ~/.codex/pets/ocelot \
  ~/.codex/pets/otacon \
  ~/.codex/pets/psychomantis \
  ~/.codex/pets/raiden \
  ~/.codex/pets/sniperwolf \
  ~/.codex/pets/solidsnake \
  ~/.codex/pets/solidussnake \
  ~/.codex/pets/vulcanraven
```

That command only deletes those named folders. It does not touch other custom pets you may have installed.

## After copying

Restart Codex so it rescans `~/.codex/pets/`. Then select the pet from Codex's custom pet / avatar options. Folder names match the pet ids: `solidsnake`, `ocelot`, `metalgearrex`, and so on.

## Compatibility

Included manifests use `spriteVersionNumber: 2`. Spritesheets are `1536x2288` with `192x208` cells.

This pack is documented for the Codex custom-pet path above. It does not claim support for other pet hosts unless those hosts read the same folder layout and v2 manifest fields.

## Verify a pet

A working pet folder should contain:

- `pet.json`
- `spritesheet.webp` (referenced by most manifests)
- `spritesheet.png` (included alongside the WebP)

Example `pet.json`:

```json
{
  "id": "solidsnake",
  "displayName": "Solid Snake (MGS1)",
  "spriteVersionNumber": 2,
  "spritesheetPath": "spritesheet.webp"
}
```
