Contributing

This project is a documented snapshot of a local Codex pet collection. Because many discovered pets reference third-party IP, contributions must follow these rules:

- Only submit pets you created yourself or have explicit written redistribution rights for.
- Each contributed pet must include:
  - a valid `pet.json` manifest with `spriteVersionNumber` and `id`/`displayName`
  - the spritesheet files (PNG or WEBP) matching the manifest
  - an optional preview GIF or PNG named `preview.*`
  - a short `README.md` describing provenance and author/contact info
- Do not submit pets that are direct copies of copyrighted characters unless you provide proof of redistribution rights.
- Keep individual PRs small: one pet per PR when possible.
- Tests and validation: visually inspect the spritesheet at the expected cell size and verify `pet.json` is present.

If uncertain about licensing, open an issue and attach the `pet.json` for review before submitting assets.
