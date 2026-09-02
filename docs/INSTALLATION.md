Installation — Using these pets locally

This repository intentionally does not include the pet asset files discovered on the local machine. Use these instructions to install pets you legally own or have permission to redistribute.

Install a single pet

1. On your machine, locate the pet folder you own (example):

   ~/.codex/pets/solidsnake

2. Copy the folder to your Codex pets directory:

   cp -R /path/to/your/local/copy/solidsnake ~/.codex/pets/

3. Restart the Codex/OpenPets app (or the companion pet runner) so it detects the new pet.

Install the entire collection from a local copy

1. If you have a local archive or zipped collection of pet folders, extract it somewhere, then copy every pet folder into `~/.codex/pets/`:

   cp -R /path/to/extracted/pet-collection/* ~/.codex/pets/

2. Restart the pet host app.

Updating an installed pet

- Replace the pet subfolder inside `~/.codex/pets/<pet-name>/` with the updated folder. Keep a backup of the previous version.

Removing a pet

- To remove a pet: rm -rf ~/.codex/pets/<pet-name>

Compatibility notes

- The inspected manifests report `spriteVersionNumber: 2` (Codex v2 style). Confirm your pet host supports v2 before installing.
- This repository does not claim compatibility with third-party pet ecosystems (OpenPets, Hermes, Petdex) unless you verify those ecosystems accept `spriteVersionNumber: 2` and the same spritesheet layout.

Verifying a pet

- Check the pet folder contains `pet.json` and a spritesheet (PNG or WEBP) sized for `192x208` cells (typical Codex v2). If unsure, inspect `pet.json` for `spriteVersionNumber` and `spriteDimensions`.

Legal / licensing

- Only copy and distribute pets if you have the rights to do so. This repo's documentation and scripts are MIT-licensed, but that does not apply to third-party pet art.
