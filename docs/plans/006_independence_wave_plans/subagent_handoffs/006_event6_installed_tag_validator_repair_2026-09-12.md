# Event 006 installed country/tag validator repair — 2026-09-12

Status: implemented.

The legacy full installed-universe validator now follows the consolidated Event 006 registries instead of requiring the removed `common/countries/006_independence_wave_formable_cosmetics.txt` file.

## Changed source

- `.tools/archive/audit_hoi4_country_tags.py` now reads `common/countries/cosmetic.txt` and extracts the Event 006 consolidated block by its source marker.
- The formable identity table includes the existing FORM-09 `BLX` Balkan Federation cosmetic identity alongside KCX, NUX, LCX, RLX, MIX, PFX, and MFX.
- The all-length custom cosmetic check retains the 17 identities from the consolidated former registry and rejects missing or unreviewed entries.
- The non-Event 006 scan excludes only the exact Event 006 definitions in the shared `common/countries/cosmetic.txt` and `common/countries/colors.txt` surfaces; same-tag definitions in another file remain collision evidence.
- The history scan recognizes the 17 inert `Unresearched Reservation` files by their exact Event 006 header and still treats same-tag files with unrelated identities as collisions.

## Validation

Command: `python -B .tools/archive/audit_hoi4_country_tags.py --repo-root . --game-root "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Hearts of Iron IV"`.

The installed-universe scan completed with exit code 0 across the vanilla game directory, 23 Workshop directories, five ZIP archives, and seven sibling local-mod directories.

- Candidate registry rows: 206.
- Reserved Event 006 tags: 102.
- Formable/cosmetic country identities: 8, including BLX/FORM-09.
- Consolidated all-length custom cosmetic identities: 17, with 17 matching call sites.
- Event 006-owned history filenames: 102, including all inert reservation shells.
- External and local collision count: 0.
- Custom cosmetic collision count: 0.

This repair changes audit tooling and evidence only; it does not widen Event 006 admission, alter gameplay, or promote any blocked visual, provenance, portrait, emblem, audio, or runtime claim.

## Remaining limits

The validator proves installed tag-surface and identity collision safety only; it does not replace live engine, save/load, MCP event-route, provenance, asset-rights, or package-admission evidence.
